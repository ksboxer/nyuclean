import logging
import feature_map

logging.basicConfig(filename='default.log',level=logging.DEBUG)

class FeatureGenerator():
	def __init__(self, configs, pic_listing):
		self.configs = configs
		self.pic_listing = pic_listing

	def get_feature_list(self):
		feature_list = []
		for feature in self.configs['features'].keys():
			if self.configs['features'][feature]:
				feature_list.append(feature)
		return feature_list

	def generate_features(self):
		features_to_process = self.get_feature_list()
		logging.debug(features_to_process)

		for feature in features_to_process:
			for file in self.pic_listing['data']:
				logging.debug(file)
				if 'path' in file.keys():
					path = file['path']		
					feature_value = feature_map.getFeature(path, feature)
					file[feature] = feature_value
		return self.pic_listing