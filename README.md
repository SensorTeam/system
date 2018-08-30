# The System

Runs everything.

## Requirements

* `python3`
* `pip`
* `virtualenv`

## Setup

1. Clone this repo
2. Clone the following repos within this repo:
	* `scanner`
	* `finder`
	* `classifier`
3. Run `setup.sh`

### Usage

#### `train.py`

1. Ensure the folder `input/training` exists and is full of images (in both `.CR2` and `.JPG` format)
2. Run `train.py` to train the system

#### `classify.py`

1. Ensure that the system has been trained
2. Connect to the SD card's WLAN
3. Run `classify.py`
4. Take photos
5. Observe results in `output/results.txt`