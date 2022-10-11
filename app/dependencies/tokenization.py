'''
CRUD FUNCTIONS ON TOKEN CLASS
'''
from dotenv import load_dotenv
import jwt
import os

load_dotenv()
SECRET_KEY = os.environ.get('SECRET_KEY')


class Token(): 
    def create():
        dummy_token = jwt.encode({"test":'Jenkins'}, f'{SECRET_KEY}')
        return dummy_token


    def read(): 
        ...