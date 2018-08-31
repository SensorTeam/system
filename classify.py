import config

import scanner
import finder
import classifier

# Functions
# ------------------------------

def save(result):
	# Appends the contents of `result` to a file
	with open(config.PATH_RESULTS, 'a') as output:
		output.write(result)

def main():
	# Downloads, extracts data from and classifies images
	count = 0

	while scanner.is_connected():
		new_count = len(scanner.get_image_list())
		if new_count > count:
			count = new_count
			print('📸 NEW IMAGE DETECTED')

			latest_image = scanner.download_latest_image()
			print('⬇️ NEW IMAGE TRANSFERRED')

			data = finder.extract_data_from(latest_image, 0)
			print('👀 DATA EXTRACTED')

			if len(data) > 0:
				print('FINDER OUTPUT', data)

				result = classifier.classify(data[0])
				print('✅ CLASSIFICATION COMPLETE')
				save(result)
			else:
				print('❌ NO EYES FOUND')

# Start the show...
# ------------------------------

if __name__ == '__main__':
	main()

