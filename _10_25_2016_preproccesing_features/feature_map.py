import color_features
import dirt_features

feature_map = {
	'hsv_color_histogram': color_features.HsvColorHistogram(),
	'gray_color_histogram': color_features.GreyScaleHistogram(),
	'dirt_feature_processing': dirt_features.FourRegionDirtDetection()
	}

def getFeature(path, feature_name):
	feature_obj = feature_map[feature_name]
	return feature_obj.run(path)

