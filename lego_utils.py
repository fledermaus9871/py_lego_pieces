import csv

def write_dict_to_csv(csv_filepath, dict_list, keys=['design_id', 'item_no', 'count']):
	
	"""
	Write a list of dicitionaries to a csv file.
	The ordering of the columns is defined by the
	keys argument and represents a list of dictionary
	keys.
	"""
	
	with open(csv_filepath, 'w') as f:
		csv_writer = csv.DictWriter(f, keys)
		csv_writer.writeheader()
		csv_writer.writerows(dict_list)
