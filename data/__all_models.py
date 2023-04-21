from flask_restful import Api
from werkzeug.utils import redirect
from data import db_session, constants
from flask import Flask, render_template, redirect, request
from data.diagrams.dog_diagrams import *
from data.diagrams.cat_diagrams import *
from data.diagrams.chin_diagrams import *
from data.diagrams.drink_diagrams import *
from data.users import User
from data.results.results_dog import Results_Dog
from data.results.results_drink import Results_Drink
from data.results.results_cat import Results_Cat
from data.results.results_chin import Results_Chin
from data.results.results import Results
from forms.user import RegisterForm, LoginForm, RequestsForm
from flask_login import LoginManager, logout_user, login_required
from data.resources import Results_DogListResource, Results_DrinkListResource, ResultsResource, Results_CatListResource, \
    Results_ChinchillaListResource
