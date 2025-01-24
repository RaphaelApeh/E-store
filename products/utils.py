import cloudinary
from decouple import config

CLOUDINARY_NAME = config("CLOUDINARY_NAME")
CLOUDINARY_API_KEY = config("CLOUDINARY_API_KEY")
CLOUDINARY_SECRET_KEY = config("CLOUDINARY_SECRET_KEY")

def load_cloudinary():
          
    cloudinary.config( 
        cloud_name = CLOUDINARY_NAME, 
        api_key = CLOUDINARY_API_KEY, 
        api_secret = CLOUDINARY_SECRET_KEY 
    )