import json
import jwt
from flask import Flask, request
from controlDados import retornarTiros as tiro
app = Flask(__name__)

SECRET_KEY = "hkBxrbZ9Td4QEwgRewV6gZSVH4q78vBia4GBYuqd09SsiMsIjH"

def token_required(something):
    def wrap(cantidad):
        try:
            token_passed = request.headers['TOKEN']
            if request.headers['TOKEN'] != '' and request.headers['TOKEN'] != None:
                try:
                    jwt.decode(token_passed,SECRET_KEY, algorithms=['HS256'])
                    tiros = tiro(cantidad)
                    data= {'dados':tiros}
                    return app.response_class(response=json.dumps(dict(data)), mimetype='application/json'),200
                except jwt.exceptions.ExpiredSignatureError:
                    return_data = {
                        "error": "1",
                        "message": "Token has expired"
                        }
                    return app.response_class(response=json.dumps(return_data), mimetype='application/json'),401
                except:
                    return_data = {
                        "error": "1",
                        "message": "Invalid Token"
                    }
                    return app.response_class(response=json.dumps(return_data), mimetype='application/json'),401
            else:
                return_data = {
                    "error" : "2",
                    "message" : "Token required",
                }
                return app.response_class(response=json.dumps(return_data), mimetype='application/json'),401
        except Exception as e:
            return_data = {
                "error" : "3",
                "message" : str(e)
                }
            return app.response_class(response=json.dumps(return_data), mimetype='application/json'),500

    return wrap