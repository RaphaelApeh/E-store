## E-Store

Welcome to **E-Store** repository! This project is a fully functional e-commerce platform designed for selling sports gear and equipment. The website offers a seamless shopping experience with feature like product browsing, secure payments and image hosting.

## 🌟 Features
- **User-Friendly interface**: Clean and reponsive design using HTML and CSS for an optimal browsing experience.

- **Secure Payments**: Product images are stored and reliable transactions.

- **Dynamic Content**: Built with Django for robust backend functionality.

- **Cloud-Hosted Media**: Product images are stored and delivered via Cloudinary.

## 🚀Technologies Used
### Backend

- **Django**: A powerful Python web framework for managing the server-side logic and database interactions.

- **Stripe**: A payment gateway for handling secure online transaction.

### Frontend
- **HTML5 & CSS3**: For crafting a reponsive and user-friendly interface.

## Media Storage
- **Cloudinary**: Cloud-base storage for uploading and delivering product images.

## 🛠 Installation and Setup

1. Clone the Repository
```bash
git clone https://github.com/RaphaelApeh/E-store.git
```
2. Set Up Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate # For Linux/Mac
.venv\scripts\activate # Windows
```
3. Install Dependencies
```bash
pip install -r requirements.txt
```
4. #### Configure Environement Variables
Create a `.env` file and add the following:
```bash
DATABASE_URL=""
DEBUG=False
SECRET_KEY=""
STRIPE_SECRET_KEY=""
STRIPE_PUB_KEY=""
EMAIL=""
EMAIL_PASSWORD=""
USERNAME=""
PASSWORD=""
CLOUDINARY_API_KEY=""
CLOUDINARY_SECRET_KEY=""
CLOUDINARY_NAME=""
```
5. Make Migration and Migrate
```bash
python manage.py makemigrations
python manage.py migrate
```
6. Add the `Whitenoise` runserver for development.
```python
# settings.py
INSTALLED_APPS = [
    ...
    "whitenoise.runserver"
]
```
7. Start the Server
```bash
python manage.py runserver
```

## 🌐 Live Demo
Website [Link](https://e-store-f80f.onrender.com)

## 🤝 Contributing
Contributions are welcome Follow these steps:
1. Fork the repository.
2. Create a new branch (git checkout -b feature/name).
3. Commit your changes (git commit -m "Commit Commit")
4. Open a pull request.