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

	if scanner.is_connected():
		count = len(scanner.get_image_list())

	while scanner.is_connected():
		new_count = len(scanner.get_image_list())
		while new_count > count:
			count = count + 1
			print('📸 NEW IMAGE DETECTED')

			# latest_image = scanner.download_one_image(count)
			latest_image = scanner.download_latest_jpg(count)
			print('⬇️ NEW IMAGE TRANSFERRED')

			data = finder.extract_data_from(latest_image, None)
			print('👀 DATA EXTRACTED')

			if len(data) > 0:
				print('FINDER OUTPUT', data)
				for entry in data:
					result = str(classifier.classify(entry))
					print('✅ CLASSIFICATION COMPLETE')
					save(result)
			else:
				print('❌ NO EYES FOUND')

# Start the show...
# ------------------------------

if __name__ == '__main__':
	main()

