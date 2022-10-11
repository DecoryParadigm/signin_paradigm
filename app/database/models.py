from dataclasses import dataclass
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()



'''
This needs to be a sqlalchemy model when the project is finish. 
'''
@dataclass
class Visitor(db.Model): 
    firstname:str
    lastname:str
    company:str
    phone:str
    time:str
    duration:str
