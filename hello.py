import os

import django
from django.contrib.auth import get_user_model

from decouple import config

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "src.settings")

django.setup()

User = get_user_model()

USERNAME = config("ADMIN_USERNAME")
EMAIL = config("EMAIL")
PASSWORD = config("PASSWORD")

def main():

    if User.objects.filter(username=USERNAME).exists():
        return
    else:
        User.objects.create_superuser(username=USERNAME, email=EMAIL, password=PASSWORD)


if __name__ == "__main__":
    main()
