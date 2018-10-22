# CONFIG for classify.py
# ------------------------------

PATH_RESULTS = 'output/results.txt'

# CONFIG for train.py
# ------------------------------

PATH_TRAINING_DATA = 'input/csv/demo_jpg.csv'
PATH_TRAINING_IMAGES = 'input/training'

# CONFIG for scanner
# ------------------------------

URL_SERVER = 'http://flashair'
PATH_SERVER = 'DCIM/100__TSB'
PATH_DOWNLOADS = 'input/images'

# CONFIG for finder
# ------------------------------
COLOUR_SOURCE = "JPG" 		# get colour from "JPG" or "RAW"

#Detecting
# MIN_THRESHOLD = 80
# MAX_THRESHOLD = 255
# MIN_NUM_PIXELS = 200
# MAX_NUM_PIXELS = 80000
# MIN_CIRCULARITY = 0.2
MIN_THRESHOLD = 80
MAX_THRESHOLD = 255
MIN_NUM_PIXELS = 200
MIN_CIRCULARITY = 0.4

MIN_SURROUNDING_CONTRAST = 40

#Pairing
MAX_ANGLE = 30
AVG_RADIUS_MULTIPLIER = 50
MIN_RADIUS_RATIO = 0.8
HU_MOMENT_DISTANCE = 0.2

# CONFIG for classifier
# ------------------------------

BIT = 8 					# 8 or 14 (jpg or raw)

COLORSPACE = "HSV" 			# RGB or HSV
N_CLASSES = 5 				# number of classes
CLASSES = ['cat', 'fox', 'cow', 'sheep', 'possum']

# RGB COLORSPACE
NORMALISED = True			# True gives R/t, G/t, B/t and 2D projection onto (r-g, 2b-r-g)
							# False is original rgb values classified in 3D

# FOR HSV COLORSPACE
COORD_SYSTEM = "polar"		# polar or cartesian

# Training
N_NEIGHBOURS = 6			# number of neighbours
WEIGHT = "uniform" 			# or "distance"

# Model paths
PATH_KNN_MODEL = "output/knn_model.sav"
PATH_SCALER_TRANSFORM = "output/scaler_transform.sav"
PATH_PLOT = "output/plot.sav"
