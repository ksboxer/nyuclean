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
    elif '.jpg' in f:
      return True

  def get_directory_dictionary(self):
    logging.info("test")
    yaml_parameters_needed = ['root_directory', 'current_data_version_folder', 'internal_folder', 'photo_folder']
    
    if len(list(set(yaml_parameters_needed) - set(self.configs.keys()))) > 0: 
      raise(YamlMissingValue)

    photo_directoy_path = ("{}\\{}\\{}\\{}\\").format(self.configs[yaml_parameters_needed[0]],
      self.configs[yaml_parameters_needed[1]],
      self.configs[yaml_parameters_needed[2]], 
      self.configs[yaml_parameters_needed[3]])

    logging.debug(photo_directoy_path)
    directory_dictionary = []
    for path, dirs, files in os.walk(photo_directoy_path):
      path_arr = path.split('\\')
      location = path_arr[-2]

      standardized_name = location.lower().replace(" ", "")


      setting = path_arr[-1]
      setting_standardized = setting.lower().replace(" ","")

      for f in files:
        data_dict = {}

        data_dict['setting_unstandardized'] = setting
        data_dict['setting_standardized'] = setting_standardized
        data_dict['standardized_location'] = standardized_name
        data_dict['unstandardized_location'] = location

        if self.check_file_health(f):
          data_dict['path'] = ('{}\\{}').format(path,f)
  				#directory_dictionary[location][setting_standardized]['jpg_paths']['{}\\{}'.format(path,f)] = {}
          directory_dictionary.append(data_dict)

    return directory_dictionary