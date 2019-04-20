from scipy.spatial import distance as dist
from imutils import paths
import numpy as np
import cv2


# Define the function to get the 3D histogram 
# Arguments: Image, Bins: Number of bins per channel (default=8)
def LabHistogram(image, bins=[8,8,8]):
	lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB) # Convert image from BRG to Lab
	hist = cv2.calcHist([lab], [0, 1, 2], None, bins, [0, 256, 0, 256, 0, 256]) # Compute 3D histogram
	hist = cv2.normalize(hist,hist).flatten() # Flatten the vector -> With 8 bins per channel: 8 x 8 x 8 = 512 elements of vector
	return hist

# Get file paths from a directory
imagePaths = sorted(list(paths.list_images("pics"))) # Pics is a folder containing your images; the folder is in your working directory
index = {}
index2 = {}

# Loop over images in directory
for imagePath in imagePaths:
	# load the image and extract the filename
	image = cv2.imread(imagePath)
	filename = imagePath[imagePath.rfind("/") + 1:]

	# Basic stats (mean and sd) of each color channel [concatenated]
	(means, stds) = cv2.meanStdDev(image)
	features = np.concatenate([means, stds]).flatten()
	index[filename] = features

	# Compute 3D histogram and print feature vector
	image2 = image.copy()
	hist3D = LabHistogram(image2)
	index2[filename] = hist3D
	print(hist3D)

# Set the baseline image for comparisons. In this case the first image listed in the list of files. You can set it to whatever you want
# This is the name of the file, not the image per se
baselineimg = imagePaths[0]
baselineimg2 = baselineimg.split("/")[1] # Retain only the name of the image without the folder path
print(baselineimg)

# display the query image and grab the sorted keys of the index dictionary
query = cv2.imread(baselineimg) # Query is your baseline image. 
cv2.imshow("Query (Baseline)", query)
keys = sorted(index.keys())

print(index2)

# loop over the filenames in the dictionary
for (i, k) in enumerate(keys):
	# if this is the query image, ignore it
	if k == baselineimg:
		continue

	# load the current image and compute the Euclidean distance between the
	# query image and the current image
	image = cv2.imread(imagePaths[i])
	d = dist.euclidean(index2[baselineimg2], index2[k])

	# display the distance between the query image and the current image
	cv2.putText(image, "%.2f" % (d), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)
	#cv2.imwrite(imagePaths[i], image) # Optional: to overwrite the image with the annotations.
	cv2.imshow(k, image) # Move them around because the windoes are stacked

# wait for a keypress: once you see the images, stay in the  window showing them and press any key to escape it
cv2.waitKey(0)