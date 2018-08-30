import config

import scanner
import finder
import classifier

# Functions
# ------------------------------

def save(result):
	# Appends the contents of `result` to a file
	with open(config.PATH_OUTPUT, 'a') as output:
		output.write(result)

def main():
	# Classify new photos
	while True:
		if scanner.is_connected():
			print('CAMERA CONNECTED')

			if scanner.has_new_image():
				print('NEW IMAGE DATECTED')

				image = scanner.download_latest_image()
				print('NEW IMAGE TRANSFERRED')

				data = finder.extract_data_from(image)
				print('DATA EXTRACTED')

				result = classifier.classify(data)
				print('CLASSIFICATION COMPLETE')

				save(result)
		else:
			print('CAMERA NOT CONNECTED')

# Start the show...
# ------------------------------

if __name__ == '__main__':
	main()