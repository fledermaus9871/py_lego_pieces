from lego_lxf_parse import ParseLegoLXF
from lego_utils import write_dict_to_csv

def execute_parse(lxf_path, unzip_dest, csv_dest):
	
	lxf = ParseLegoLXF(lxf_pathname=lxf_path, extract_path=unzip_dest)
	inventory_list = lxf.get_summarized_piece_count()
	write_dict_to_csv(csv_filepath=csv_dest, dict_list=inventory_list)

if __name__ == '__main__':
	
	lxf_path = '/home/andrewyan/Desktop/tmp/bus_lf_variant_hybrid.lxf'
	unzip_dest = '/home/andrewyan/Desktop/tmp/bus_unzip'
	csv_dest = '/home/andrewyan/Desktop/lego_hybrid_bus.csv'
	
	execute_parse(lxf_path, unzip_dest, csv_dest)
