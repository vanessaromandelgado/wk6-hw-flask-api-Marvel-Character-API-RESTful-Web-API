from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin
from datetime import datetime, timezone
from werkzeug.security import generate_password_hash
from uuid import uuid4
from secrets import token_hex

login = LoginManager()
db = SQLAlchemy()

@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id= db.Column(db.String, primary_key=True)
    username=db.Column(db.String(),  nullable =False,unique=True)
    email=db.Column(db.String(), nullable =True)
    first_name= db.Column(db.String(), nullable =True,default='')
    last_name=db.Column(db.String(), nullable =True,default='')
    password=db.Column(db.String(), nullable =False)
    created_on= db.Column(db.DateTime, nullable= False, default=datetime.now(timezone.utc))
    apitoken=db.Column(db.String(32),nullable=True,default='None')

    def __init__(self, username, email, first_name, last_name, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
        self.first_name = first_name
        self.last_name = last_name
        self.id = str(uuid4())
        self.apitoken = token_hex(16)
       


class Marvel_char(db.Model):
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String(),  nullable =False,unique=True)
    description = db.Column(db.String(), nullable =True, default=None)
    comics_appeared_in = db.Column(db.Integer, nullable =False) 
    super_power = db.Column(db.String(), nullable =True, default=None)
    date_created = db.Column(db.DateTime, nullable= False, default=datetime.now(timezone.utc))

    def to_dict(self):
        return{
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'comics_appeared_in': self.comics_appeared_in,
            'super_power': self.super_power         
        }
    
    def from_dict(self,dict):
        if not self.id:
            self.id = str(uuid4())
        if dict.get('name'):
            self.name = dict['name']
        if dict.get('comics_appeared_in'):   
            self.comics_appeared_in = dict['comics_appeared_in']              
        
        if dict.get('description'):
            self.description = dict['description']
        
        
        if dict.get('super_power'):
            self.super_power = dict ['super_power']  
