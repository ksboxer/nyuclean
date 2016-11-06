import yaml
import sys
import logging
import json
import time

import photo_reader as pr
import score_reader as sr

logging.basicConfig(filename='default.log',level=logging.DEBUG)

class YamlMissing(Exception):
	def __init__(self, message):
		self.message = message

def cmd_arg_check(cmd_arg_list):
	if len(cmd_arg_list) < 2:
		raise YamlMissing('First Input for cmd needs to be yaml file.  For example run program as python run.py default.yaml')
	else:
		yaml_file_path = cmd_arg_list[1]
		return yaml_file_path

def main(yaml_file_path):
	pass
	with open(yaml_file_path, 'r') as f:
		configs = yaml.load(f)

	logging.debug(str(configs))
	photo_reader = pr.PhotoReader(configs)
	photo_directory = photo_reader.get_directory_dictionary()
	logging.debug("PHOTO DIRECTORY:   {}".format(str(photo_directory)))

	score_reader = sr.ScoreReader(configs, photo_directory)
	updated_lst = score_reader.add_scores_to_image_file_dict()
	with open('data_json\\sample_output'+str(time.time())+'.json', 'w') as f:
		json.dump({'data': updated_lst}, f)
	#logging.debug(updated_lst)

if __name__ == "__main__":
	cmd_arg_list = sys.argv
	yaml_file_path = cmd_arg_check(cmd_arg_list)
	main(yaml_file_path)
