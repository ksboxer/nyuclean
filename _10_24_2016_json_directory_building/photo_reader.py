import logging
import os 

logging.basicConfig(filename='default.log',level=logging.DEBUG)

class YamlMissingValue(Exception):
	def __init__(self, yaml_parameters_needed):
		self.message = ("One the needed parameters is missing from the following: , {}").format(str(yaml_parameters_needed))


class PhotoReader():

	def __init__(self, configs):
		self.configs = configs

	def check_file_health(self, f):
		if f[0:2] == '._':
			return False
		else:
			return True

	def get_directory_dictionary(self):
		logging.info("test")
		yaml_parameters_needed = ['root_directory', 'current_data_version_folder', 'internal_folder', 'photo_folder']


		if len(list(set(yaml_parameters_needed) - set(self.configs.keys()))) > 0: 
			raise(YamlMissingValue)

		photo_directoy_path = "{}\\{}\\{}\\{}\\".format(self.configs[yaml_parameters_needed[0]],self.configs[yaml_parameters_needed[1]],
			self.configs[yaml_parameters_needed[2]], self.configs[yaml_parameters_needed[3]])
		logging.debug(photo_directoy_path)

		directory_dictionary = {}
		for path, dirs, files in os.walk(photo_directoy_path):
  			path_arr = path.split('\\')
  			location = path_arr[-2]

  			standardized_name = location.lower().replace(" ", "")
  				
  			if standardized_name not in directory_dictionary.keys():
  				#standardized_name = location.lower().replace(" ", "")
  				directory_dictionary[standardized_name] = {}
  				directory_dictionary[standardized_name]['unstandardized_name'] =  location
  			
  			location = standardized_name

  			setting = path_arr[-1]
  			setting_standardized = setting.lower().replace(" ","")
  			
  			if setting_standardized not in directory_dictionary[location].keys():
  				directory_dictionary[location][setting_standardized] = {}
  				directory_dictionary[location][setting_standardized]['unstandardized_setting'] = setting
  			
  			setting = setting_standardized
  			directory_dictionary[location][setting_standardized]['jpg_paths'] = {}
  			#directory_dictionary[location][setting][files]
  			for f in files:
  				if self.check_file_health(f):
  					directory_dictionary[location][setting_standardized]['jpg_paths']['{}\\{}'.format(path,f)] = {}
		return directory_dictionary