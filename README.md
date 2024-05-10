## Project Title: DreamyTales AI

## Project Description

DreamyTales AI is an innovative web application designed to ignite the imaginations of children through personalized stories. Utilizing the advanced capabilities of OpenAI's GPT models, this project offers a unique storytelling experience that adapts to the personal interests and characteristics of each child. Whether a child is fascinated by fairy tales, adventures in space, or magical mysteries, DreamyTales AI crafts stories that are not only engaging but also encouraging and educational.

The application allows users (parents, teachers, or the children themselves) to input specific details such as the child’s name, age, location, and hobbies. These inputs are then used to generate customized stories that resonate more personally with the reader, enhancing their reading enjoyment and engagement.

Built with Django and Django REST Framework, DreamyTales AI exemplifies how technology can be used to enhance traditional storytelling and educational methods. The application is designed to be straightforward and user-friendly, ensuring accessibility for users of all tech skill levels. It also includes robust API documentation to facilitate easy integration with other applications or services.

By fostering a love for reading and stimulating creative thinking, DreamyTales AI aims to contribute positively to child development and education, making learning both fun and inspiring.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7 or higher installed. [Download Python](https://www.python.org/downloads/)
- pip (Python Package Installer), included with Python.
- Virtual environment (recommended): `pip install virtualenv`
- An OpenAI API key. You need to sign up at [OpenAI](https://platform.openai.com/signup) and subscribe to an API plan.

## Installation

Follow these steps to get your development environment set up:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/yourproject.git
   cd yourproject
   ```

2. **Set Up a Python Virtual Environment (Optional but Recommended)**
   - For Windows:
     ```bash
     python -m venv env
     env\Scripts\activate
     ```
   - For macOS and Linux:
     ```bash
     python3 -m venv env
     source env/bin/activate
     ```

3. **Install Required Python Packages**
   ```bash
   pip install -r requirements.txt


   ```

   The `requirements.txt` file should include at least:
   ```
   Django>=3.2.25
   djangorestframework
   django-cors-headers
   openai
   ```

4. **Create a `.env` file for Environment Variables**

   Create a `.env` file in the root of your project directory and add your OpenAI API key:
   ```plaintext
   OPENAI_API_KEY='your_openai_api_key_here'
   ```

   You can use `python-decouple` or `django-environ` to manage environment variables securely. If you choose to use one, remember to install it via pip and import it in your settings.

## Configuration

1. **Django Settings**

   Update the `settings.py` file in your Django project to include installed apps and middleware:
   ```python
   INSTALLED_APPS = [
       ...
       'rest_framework',
       'corsheaders',
       'yourappname',  # Replace 'yourappname' with the name of your Django app
   ]

   MIDDLEWARE = [
       ...
       'corsheaders.middleware.CorsMiddleware',
       ...
   ]
   ```

   Configure `CORS_ALLOWED_ORIGINS` if necessary:
   ```python
   CORS_ALLOWED_ORIGINS = [
       'http://localhost:3000',
   ]
   ```

2. **Database Migrations**

   Apply database migrations:
   ```bash
   python manage.py migrate
   ```

## Running the Project

1. **Start the Django Development Server**
   ```bash
   python manage.py runserver
   ```

   This will start the server on `http://127.0.0.1:8000/` by default.

2. **Accessing the API**

   Use Postman or any HTTP client to make requests to your API. For example, to access the story API:
   ```
   POST http://127.0.0.1:8000/talesapi/story/
   Content-Type: application/json

   {
       "kid_name": "Alice",
       "location": "Wonderland",
       "age": 10,
       "hobbies": ["exploring", "reading", "playing chess"]
   }
   ```
## Contact

(https://www.linkedin.com/in/chaitanya-srk/)
