from __future__ import print_function
from sklearn.metrics import classification_report
from sklearn.model_selection import GridSearchCV
from sklearn.svm import LinearSVC
import numpy as np
import argparse
import h5py
import cv2
import csv

ap = argparse.ArgumentParser()
ap.add_argument("-f", "--features-db", required=True,
	help="Path the features database")
ap.add_argument("-b", "--bovw-db", required=True,
	help="Path to where the bag-of-visual-words database")
ap.add_argument("-o", "--output", required=True,
	help="Path to the file where the ImgVisWordMat would be exported")

args = vars(ap.parse_args())

# open the features and bag-of-visual-words databases
featuresDB = h5py.File(args["features_db"])
bovwDB = h5py.File(args["bovw_db"])
exportFile = args['output']


ids = list(featuresDB['image_ids'])
print("[INFO] loading data...")

flds = ['id']
for i in range(0,len(bovwDB['bovw'][0])):
	flds.append('vis_'+str(i))


vwmat = bovwDB['bovw']


with open(exportFile, 'w') as f:
	my_writer = csv.DictWriter(f, fieldnames=flds)
	my_writer.writeheader()
	for i in range(0,len(ids)):
		temp = {'id':ids[i]}
		for k in range(1, len(flds)):
			temp[flds[k]] = bovwDB['bovw'][i][k-1]
		my_writer.writerow(temp)

