import config

import scanner
import finder
import classifier

# Functions
# -----------------------------

def save(result):
	with open(config.OUTPUT_PATH, 'a') as output_file:
		output_file.write(result)

def main():
	while True:
		if scanner.is_connected():
			print('CAMERA CONNECTED')
			if scanner.has_new_image():
				print('NEW IMAGE DETECTED')

				# Download the image from the camera and return the path of the file minus the extension (e.g. images/IMG_0001)
				path = scanner.download_image()
				print('NEW IMAGE TRANSFERRED')

				# Extract the necessary data
				data = finder.extract_data_from(path)
				print('DATA EXTRACTED')

				# Classify the data
				result = classifier.classify(data)
				print('CLASSIFIED')

				save(result)
		else:
			print('CAMERA NOT CONNECTED...')

# Start the show...
# -----------------------------

if __name__ == '__main__':
	main()

