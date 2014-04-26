import csv

def write_dict_to_csv(csv_filepath, dict_list, keys=['design_id', 'item_no', 'count']):
	
	with open(csv_filepath, 'w') as f:
		csv_writer = csv.DictWriter(f, keys)
		csv_writer.writeheader()
		csv_writer.writerows(dict_list)
