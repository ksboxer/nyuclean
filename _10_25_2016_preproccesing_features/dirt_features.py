import cv2
import logging
import numpy as np

logging.basicConfig(filename='default.log',level=logging.DEBUG)

class FourRegionDirtDetection():
	def run(self, path):
		image = cv2.imread(path)
		if image != None:
			mask = cv2.inRange(image, np.array([61, 43, 0]) , np.array([153, 121, 93]))
			res = cv2.bitwise_and(image,image, mask= mask)
			width, height, t = res.shape
			incre_w = int(width / 2)
			incre_h = int(height / 2)
			range_w = [(0,incre_w), (incre_w, 2* incre_w)]
			range_h = [(0,incre_h), (incre_h, 2* incre_h)]
			grid_images = []
			for (w_0, w_1) in range_w:
				for (h_0, h_1) in range_h:
					im = res[w_0:w_1, h_0:h_1]
					im_b= cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
					grid_images.append([[(w_0, w_1), (h_0, h_1)], cv2.countNonZero(im_b)/im.size])
			return grid_images
		return None

class NineRegionDirtDetection():
	def run(self, path):
		image = cv2.imread(path)
		if image != None:
			mask = cv2.inRange(image, np.array([61, 43, 0]) , np.array([153, 121, 93]))
			res = cv2.bitwise_and(image,image, mask= mask)
			width, height, t = res.shape
			incre_w = int(width / 3)
			incre_h = int(height / 3)
			range_w = [(0,incre_w), (incre_w, 2* incre_w), (2*incre_w, 3*incre_w)]
			range_h = [(0,incre_h), (incre_h, 2* incre_h), (2*incre_h, 3*incre_h)]
			grid_images = []
			for (w_0, w_1) in range_w:
				for (h_0, h_1) in range_h:
					im = res[w_0:w_1, h_0:h_1]
					im_b= cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
					grid_images.append([[(w_0, w_1), (h_0, h_1)], cv2.countNonZero(im_b)/im.size])
			return grid_images
		return None