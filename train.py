import config

import finder
import classifier

from glob import glob

# Functions
# ------------------------------

def get_training_images_from(path):
	# Returns an array of paths of images without the extension (e.g. images/IMG_0001)
	images = []
	files = glob(config.PATH_TRAINING_IMAGES + '/*.jpg')
	for file in files:
		try:
			images.append(file[:-4])
		except:
			print('ERROR LOADING IMAGES FROM', path)
	return images

def generate_training_data_from(images):
	# Creates an array where each row is the data extracted from an image
	training_data = []
	for image in images:
		data = finder.extract_data_from(image)
		training_data.append(data)
	return training_data

def save(training_data, path):
	# Creates a .csv full of the extracted training data
	with open(path, 'r+') as training_data_file:
		for data in training_data:
			training_data_file.write(data)

def load_images():
	# Trains the system
	images = get_training_images_from(config.PATH_TRAINING_IMAGES)
	print('IMAGES LOADED')
	training_data = generate_training_data_from(images)
	print('DATA EXTRACTED')
	save(training_data, config.PATH_TRAINING_DATA)
	print('DATA SAVED')

def main():
	classifier.train(config.PATH_TRAINING_DATA)
	print('TRAINING COMPLETE')

# Start the show...
# ------------------------------

if __name__ == '__main__':
	main()


