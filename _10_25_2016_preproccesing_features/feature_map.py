import color_features

feature_map = {
	'hsv_color_histogram': color_features.HsvColorHistogram(),
	'gray_color_histogram': color_features.GreyScaleHistogram()
	}

def getFeature(path, feature_name):
	feature_obj = feature_map[feature_name]
	return feature_obj.run(path)

