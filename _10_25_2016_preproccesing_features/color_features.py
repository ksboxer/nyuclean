import cv2
import logging
import numpy

logging.basicConfig(filename='default.log',level=logging.DEBUG)

class HsvColorHistogram():
	def run(self, path):
		img = cv2.imread(path)
		if img != None:
			hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
			h, s, v = cv2.split(img)
			#logging.debug(s)
			#logging.debug(h[:] /(int(45)))
			c = h[:]/(int(45)) + s[:] /(int(64)) + v[:] / (int(64))
			logging.debug(c.shape)
			#hist = cv2.calcHist([c], None, None, [16], [0,256])
			hist, edges = numpy.histogram(c, bins=16, density = True)
			logging.debug(hist)
			return list(hist)

class GreyScaleHistogram():
	def run(self, path):
		img = cv2.imread(path,0)
		if img != None:
			hist, edges = numpy.histogram(img, bins=16, density = True)
			return list(hist)


		#logging.debug(hsv)
		#hist = cv2.calcHist( [hsv], [0,1], None, [180, 256], [0,180,0,256])
		#logging.debug('hsv color hist')