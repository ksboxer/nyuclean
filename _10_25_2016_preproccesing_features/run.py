import yaml
import logging
import sys
import json
import feature_generator as fg
import time

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
	with open(yaml_file_path, 'r') as f:
		configs = yaml.load(f)

	logging.debug(str(configs))

	json_path = ("{}\\{}").format(configs['directory_json_location'],
		configs['json_file_name'])
	logging.debug(json_path)

	with open(json_path, 'r') as f:
		pic_listings = json.load(f)

	feature_generator = fg.FeatureGenerator(configs, pic_listings)
	feature_pic_listing = feature_generator.generate_features()

	with open('pics_features\\features_'+str(time.time())+'.json', 'w') as f:
		json.dump(feature_pic_listing, f)

	#logging.debug(pic_listings)


if __name__ == '__main__':
	cmd_arg_list = sys.argv
	yaml_file_path = cmd_arg_check(cmd_arg_list)
	main(yaml_file_path)
