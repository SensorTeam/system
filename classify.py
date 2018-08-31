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
	# Downloads, extracts data from and classifies images
	count = 0

	try:
		while scanner.is_connected():
			new_count = len(scanner.get_image_list())
			if new_count > count:
				count = new_count
				print('📸 NEW IMAGE DETECTED')

				latest_image = scanner.download_latest_image()
				print('⬇️ NEW IMAGE TRANSFERRED')

				data = finder.extract_data_from(latest_image)
				print('👀 DATA EXTRACTED')

				result = classifier.classify(data)
				print('✅ CLASSIFICATION COMPLETE')

				save(result)
	except:
		print('CAMERA DISCONNECTED')

# Start the show...
# ------------------------------

if __name__ == '__main__':
	main()

