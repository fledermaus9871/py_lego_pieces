import zipfile

from lxml import etree

class ParseLegoLXF(object):
	
	def __init__(self, lxf_pathname, extract_path, lxfml_name='IMAGE100.LXFML'):
		
		self.lxf = lxf_pathname
		self.extract = extract_path
		self.lxfml = lxfml_name
		
	def unzip_lxf(self):
		
		with zipfile.ZipFile(self.lxf, 'r') as z:
			z.extractall(self.extract)
			
	def parse_lxfml(self):
		
		self.unzip_lxf()
		lxfml_path = '%s/%s' % (self.extract, self.lxfml)
		xml_doc = etree.parse(lxfml_path)
		print xml_doc

if __name__ == '__main__':
	
	lxf_path = '/home/andrewyan/Desktop/tmp/bus_lf_variant_hybrid.lxf'
	extract_dest = '/home/andrewyan/Desktop/tmp/bus_unzip'
	
	lxf = ParseLegoLXF(lxf_path, extract_dest)
	lxf.parse_lxfml()
