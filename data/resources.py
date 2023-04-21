from flask import jsonify
from flask_restful import Resource

from data import db_session
from data.results.results import Results
from data.results.results_dog import Results_Dog
from data.results.results_drink import Results_Drink
from data.results.results_cat import Results_Cat
from data.results.results_chin import Results_Chin


class ResultsResource(Resource):
    def get(self):
        session = db_session.create_session()
        results = session.query(Results).all()
        return jsonify({'results': [item.to_dict(
            only=('dog', 'drink', 'cat', 'chinchilla', 'user_id')) for item in results]})


class Results_DogListResource(Resource):
    def get(self):
        session = db_session.create_session()
        results = session.query(Results_Dog).all()
        return jsonify({'results_dog': [item.to_dict(
            only=('dog_1', 'dog_2', 'dog_3', 'dog_4', 'dog_5' 'user_id')) for item in results]})


class Results_DrinkListResource(Resource):
    def get(self):
        session = db_session.create_session()
        results = session.query(Results_Drink).all()
        return jsonify({'results_drink': [item.to_dict(
            only=('drink_1', 'drink_2', 'drink_3', 'drink_4', 'drink_5' 'user_id')) for item in results]})


class Results_CatListResource(Resource):
    def get(self):
        session = db_session.create_session()
        results = session.query(Results_Cat).all()
        return jsonify({'results_cat': [item.to_dict(
            only=('cat_1', 'cat_2', 'cat_3', 'cat_4', 'cat_5' 'user_id')) for item in results]})


class Results_ChinchillaListResource(Resource):
    def get(self):
        session = db_session.create_session()
        results = session.query(Results_Chin).all()
        return jsonify({'results_chinchilla': [item.to_dict(
            only=('chin_1', 'chin_2', 'chin_3', 'chin_4', 'chin_5', 'user_id')) for item in results]})