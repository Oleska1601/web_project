import datetime
import sqlalchemy
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy_serializer import SerializerMixin
from data.db_session import SqlAlchemyBase
from sqlalchemy import orm


class Results_Cat(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'results_cat'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    cat_1 = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    cat_2 = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    cat_3 = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    cat_4 = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    cat_5 = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    user_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("users.id"))

    user = orm.relationship('User')
