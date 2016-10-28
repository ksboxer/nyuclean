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
			for location in self.pic_listing.keys():
				for settings in self.pic_listing[location]:
					if 'jpg_paths' in self.pic_listing[location][settings]:
						for idx,jpg_path in enumerate(self.pic_listing[location][settings]['jpg_paths'].keys()):
							print(('{} out of {}').format(idx, len(self.pic_listing[location][settings]['jpg_paths'].keys())))
							#jpg_path = jpg_path.encode('ascii', 'ignore')
							#print(jpg_path)
							logging.debug(jpg_path)
							feature_value = feature_map.getFeature(jpg_path, feature)
							self.pic_listing[location][settings]['jpg_paths'][jpg_path][feature] = feature_value
		return self.pic_listing