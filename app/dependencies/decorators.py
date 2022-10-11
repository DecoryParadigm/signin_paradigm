from functools import wraps
from flask import jsonify, request
from dotenv import load_dotenv
import jwt
import os
load_dotenv()

SECRET_KEY = os.environ.get('SECRET_KEY')


def handshake(f):
    wraps(f)
    def shake(*args, **kwargs): 
        if 'token-access' in request.headers:
            token = request.headers['token-access']
            if not token:
                return jsonify({'msg':"missing-token"})
            handshake_val = jwt.decode(token, SECRET_KEY)
            if handshake_val['test'] == "Jenkins":
                return f(True, *args, **kwargs)
        else:
            return f(False,  *args, **kwargs)
    return shake