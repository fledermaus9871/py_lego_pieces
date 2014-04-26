import zipfile

from lxml import etree

class ParseLegoLXF(object):
	
	def __init__(self, lxf_pathname, extract_path, lxfml_name='IMAGE100.LXFML'):
		
		self.lxf = lxf_pathname
		self.extract = extract_path
		self.lxfml = lxfml_name
		
	def unzip_lxf(self):
		
		"""
		Unzip the Lego Digitial Designer file located at lxf_pathname
		"""
		
		with zipfile.ZipFile(self.lxf, 'r') as z:
			z.extractall(self.extract)
			
	def parse_lxfml(self):
		
		"""
		Parse the lxfml file in the unzipped lxf file
		"""
		
		self.unzip_lxf()
		lxfml_path = '%s/%s' % (self.extract, self.lxfml)
		xml_doc = etree.parse(lxfml_path)
		
		return xml_doc
		
	def create_pieces_inventory(self, xml_doc=None):
		
		"""
		Create an inventory of pieces specified in the lxfml file
		"""
		
		if xml_doc:
			root = xml_doc
		else:
			root = self.parse_lxfml()
			
		

if __name__ == '__main__':
	
	lxf_path = '/home/andrewyan/Desktop/tmp/bus_lf_variant_hybrid.lxf'
	extract_dest = '/home/andrewyan/Desktop/tmp/bus_unzip'
	
	lxf = ParseLegoLXF(lxf_path, extract_dest)
	lxf.parse_lxfml()
