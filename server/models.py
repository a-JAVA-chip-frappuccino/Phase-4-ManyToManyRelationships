from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Restaurant(db.Model, SerializerMixin):
    pass

class Food(db.Model, SerializerMixin):
    pass

class FoodAtRestaurant(db.Model, SerializerMixin):
    pass