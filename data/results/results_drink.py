import datetime
import sqlalchemy
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy_serializer import SerializerMixin
from data.db_session import SqlAlchemyBase
from sqlalchemy import orm


class Results_Drink(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'results_drink'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    drink_1 = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    drink_2 = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    drink_3 = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    drink_4 = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    drink_5 = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    user_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("users.id"))

    user = orm.relationship('User')
