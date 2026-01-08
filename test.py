# import os
# from dotenv import load_dotenv

# load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))

# print("Environment variables loaded from .env file")
# print(os.getenv("VERCEL_URL"))

import requests

def test_vercel_url():
    vercel_url = "https://school-pilot-api.vercel.app/"
    try:
        response = requests.get(vercel_url)
        assert response.status_code == 200
        print("Vercel URL is reachable and returned status code 200.")
    except requests.RequestException as e:
        print(f"Failed to reach Vercel URL: {e}")

def create_user():
    vercel_url = "http://127.0.0.1:8000/api/accounts/register/"
    user_data = {
        "username": "testuser",
        "email": "test@gmail.com",
        "first_name": "Test",
        "last_name": "User",
        "password": "TestPassword123"
    }
    try:
        response = requests.post(vercel_url, json=user_data)
        if response.status_code == 201:
            print("User created successfully.")
        else:
            print(f"Failed to create user. Status code: {response.status_code}, Response: {response.text}")
    except requests.RequestException as e:
        print(f"Error occurred while creating user: {e}")

def login_user():
    vercel_url = "http://127.0.0.1:8000/api/accounts/token/"
    login_data = {
        "email": "admin@gmail.com",
        "password": "123456@Ad"
    }
    try:
        response = requests.post(vercel_url, json=login_data)
        if response.status_code == 200:
            print("User logged in successfully.")
            print(f"Response: {response.json()}")
        else:
            print(f"Failed to log in. Status code: {response.status_code}, Response: {response.text}")
    except requests.RequestException as e:
        print(f"Error occurred while logging in: {e}")
# test_vercel_url()
# login_user()
create_user()