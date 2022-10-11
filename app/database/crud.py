from flask import jsonify
from app.main import db
from database.models import Visitor

class visitor_info:
    def submit(self, info):
        try:
            db.session.add(Visitor(info))
            db.session.commit()
            return jsonify(status=200, message=f"{info['firstname']} submission successful")
        except Exception as e: 
            return jsonify(status=422, error="Vistor not added, please try again.")

