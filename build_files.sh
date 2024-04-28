# build_files.sh

echo "Building the project..."
pip3 install -r requirements.txt

echo "Make migration and collect static..."
python3.9 manage.py makemigrations --noinput
python3.9 manage.py migrate --noinput
python3.9 manage.py collectstatic --noinput --clear