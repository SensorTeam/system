mv scanner-mk* scanner
mv finder-mk* finder
mv classifier-mk* classifier

pip install -r scanner/requirements.txt
pip install -r finder/requirements.txt
pip install -r classifier/requirements.txt

mkdir input
mkdir input/images
mkdir input/training
mkdir input/csv
mkdir output

