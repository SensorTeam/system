# CONFIG for classify.py
# ------------------------------

PATH_RESULTS = 'output/results.txt'

# CONFIG for train.py
# ------------------------------

PATH_TRAINING_DATA = 'input/csv/results_jpg.csv'
PATH_TRAINING_IMAGES = 'input/training'

# CONFIG for scanner
# ------------------------------

URL_SERVER = 'http://flashair'
PATH_SERVER = 'DCIM/100__TSB'
PATH_DOWNLOADS = 'input/images'

# CONFIG for finder
# ------------------------------

# CONFIG for classifier
# ------------------------------

BIT = 8 					# 8 or 14 (jpg or raw)

COLORSPACE = "RGB" 			# RGB or HSV
N_CLASSES = 5 				# number of classes

# RGB COLORSPACE
NORMALISED = True			# True gives R/t, G/t, B/t and 2D projection onto (r-g, 2b-r-g)
							# False is original rgb values classified in 3D

# FOR HSV COLORSPACE
COORD_SYSTEM = "polar"		# polar or cartesian

# Training
N_NEIGHBOURS = 8			# number of neighbours
WEIGHT = "uniform" 			# or "distance"

# Model paths
PATH_KNN_MODEL = "output/knn_model.sav"
PATH_SCALER_TRANSFORM = "output/scaler_transform.sav"