from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Pet(db.Model):
    '''Creates Pet model for SQLAlchemy'''

    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key= True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text, default='https://mylostpetalert.com/wp-content/themes/mlpa-child/images/nophoto.gif')
    age = db.Column(db.Integer, nullable=True)
    notes = db.Column(db.Text, nullable=True)
    available = db.Column(db.Boolean, default= True)


def connect_db(app):
    '''Connect to database'''
    db.app = app
    db.init_app(app)
