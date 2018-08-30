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

				path = scanner.download_image()
				print('NEW IMAGE TRANSFERRED')

				data = finder.extract_data_from(path)
				print('DATA EXTRACTED')

				result = classifier.classify(data)
				print('CLASSIFYING...')
				
				save(result)
		else:
			print('CAMERA NOT CONNECTED...')

# Start the show...
# -----------------------------

if __name__ == '__main__':
	main()

