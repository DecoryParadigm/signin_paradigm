
import os
from flask import Flask, jsonify, request
from app.task import Vistor
from database import models, crud
from dependencies.tokenization import Token
import dependencies.decorators as decor



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=f"{os.getenv()}/{os.getenv()}/{os.getenv()}/{os.getenv()}"
db=models.db(app)

with app.app_context():
    db.create_all()

@app.route("/", methods=['GET'])
def authenticate_request(): 
    envGlobal = Token.create()
    return envGlobal


@app.route("/submission-request", methods=['POST'])
@decor.handshake
def data_submission(data): 
    if data: 
        customer = Vistor(request.get_json(force=True))

        crud.visitor_info.submit(customer)
    return jsonify({"errorRaised":"Invalid handshake, please try again."})



if __name__ == "__main__":
    app.run(debug=True)
