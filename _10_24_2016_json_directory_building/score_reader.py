import logging
import os
import xlrd


logging.basicConfig(filename='default.log',level=logging.DEBUG)

class YamlMissingValue(Exception):
	def __init__(self, yaml_parameters_needed):
		self.message = ("One the needed parameters is missing from the following: , {}").format(str(yaml_parameters_needed))

class ScoreReader():
	def __init__(self, configs, image_file_dict):
		self.configs = configs
		self.image_file_dict = image_file_dict

	def add_scores_to_image_file_dict(self):
		yaml_parameters_needed = ['root_directory', 'current_data_version_folder', 'internal_folder', 'score_folder', 'score_excel_file']

		if len(list(set(yaml_parameters_needed) - set(self.configs.keys()))) > 0: 
			raise(YamlMissingValue)

		score_file_path =   "{}\\{}\\{}\\{}\\{}".format(self.configs[yaml_parameters_needed[0]],self.configs[yaml_parameters_needed[1]],
		self.configs[yaml_parameters_needed[2]], self.configs[yaml_parameters_needed[3]],
		self.configs[yaml_parameters_needed[4]])

		logging.debug(score_file_path)

		work_book = xlrd.open_workbook(score_file_path)
		sheet_names = work_book.sheet_names()
		logging.debug(sheet_names)

		logging.debug(self.image_file_dict.keys())
		for idx,sheetname in enumerate(sheet_names):
			sheet = work_book.sheet_by_index(0)
			standardized_sheetname = sheetname.lower().replace(" ","")
			if standardized_sheetname not in self.image_file_dict.keys():
				logging.warning(standardized_sheetname)
			else:
				excel_arr = []
				for row_idx in range(0, sheet.nrows):
					row = []
					for col_idx in range(0, sheet.ncols):
						cell_obj = sheet.cell_value(row_idx, col_idx)
						row.append(cell_obj)
					excel_arr.append(row)
				#logging.debug(excel_arr)
				header = excel_arr[0]
				del excel_arr[0]

				pic_settings = self.image_file_dict[standardized_sheetname].keys()
				logging.debug(str(pic_settings))
				for row in excel_arr:
					location = row[0]
					del row[0]
					standardized_location = location.lower().replace(" ","")
					if standardized_location not in pic_settings:
						self.image_file_dict[standardized_sheetname][standardized_location] = {}
						self.image_file_dict[standardized_sheetname][standardized_location]['unstandardized_name'] = location
					for idx, col in enumerate(header[1:]):
						self.image_file_dict[standardized_sheetname][standardized_location][col] = row[idx]
		return self.image_file_dict
				