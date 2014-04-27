import zipfile

from lxml import etree

class ParseLegoLXF(object):
	
	def __init__(self, lxf_pathname, extract_path, lxfml_name='IMAGE100.LXFML'):
		
		"""
		lxf_pathname is the path to the lxf file (e.g /home/johndoe/lego_creations/bike.lxf),
		extract_path is the path where the lxf contents should be extracted (e.g. /home/johndoe/tmp/lego/)
		lxfml_name is the name of the xml file that is extracted from the lxf
		"""
		
		self.lxf = lxf_pathname
		self.extract = extract_path
		self.lxfml = lxfml_name
		
	def unzip_lxf(self):
		
		"""
		Unzip the Lego Digitial Designer file located at lxf_pathname.
		The contents are placed in the directory specifed in "extract_path"
		when instantiating a ParseLegoLXF object.
		"""
		
		with zipfile.ZipFile(self.lxf, 'r') as z:
			z.extractall(self.extract)
			
	def parse_lxfml(self):
		
		"""
		Parse the lxfml file in the unzipped lxf file
		using lxml.
		"""
		
		self.unzip_lxf()
		lxfml_path = '%s/%s' % (self.extract, self.lxfml)
		xml_doc = etree.parse(lxfml_path)
		
		return xml_doc
		
	def create_pieces_inventory(self, xml_doc=None):
		
		"""
		Create an inventory of pieces specified in the lxfml file.
		Look for all lxfml elements of 'Brick' and get their designID
		and itemNos attribute values. These values correspond to LEGO
		design IDs and element IDs repectively. These values are then
		placed in a tuple and appended to a list.
		"""
		
		if xml_doc:
			root = xml_doc
		else:
			root = self.parse_lxfml()
			
		inventory_list = []	
			
		brick_elements = root.findall(".//Brick")
		for brick_element in brick_elements:
			inventory_dict = {}
			brick_design_id = brick_element.attrib['designID']
			try:
				brick_item_no = brick_element.attrib['itemNos']
			except KeyError:
				brick_item_no = None
			brick_tuple = (brick_design_id, brick_item_no)
			inventory_list.append(brick_tuple)
			
		return inventory_list
		
		
	def get_unique_piece_designs(self, piece_inventory_list=None):
		
		"""
		Return a list of unique pieces used in the Lego model.
		"""
		
		if piece_inventory_list:
			pil = piece_inventory_list
		else:
			pil = self.create_pieces_inventory()
			
		unique_pieces_set = set(pil)
		unique_pieces_list = list(unique_pieces_set)
		
		return unique_pieces_list
		
		
	def get_summarized_piece_count(self):
		
		"""
		Get an inventory with the counts for
		each unique Lego piece in the model by
		using the unique pieces list and the full
		inventory list. A dictionary with design ID,
		item no, and count is returned.
		"""
		
		piece_inventory = self.create_pieces_inventory()
		unique_pieces = self.get_unique_piece_designs()
		
		piece_inventory_list = []
		
		for unique_piece in unique_pieces:
			piece = {}
			piece_count = piece_inventory.count(unique_piece)
			design_id, item_no = unique_piece
			piece['design_id'] = design_id
			piece['item_no'] = item_no
			piece['count'] = piece_count
			piece_inventory_list.append(piece)
			
		return piece_inventory_list
