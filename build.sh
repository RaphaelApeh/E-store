set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --oninput

python manage.py makemigrations

python manage.py migrate

python hello.py