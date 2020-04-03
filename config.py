import os
# - Путь к файлу БД в данной папке
db_path = 'sqlite:///mydatabase.db'


class Config:
    DEBUG = True
    SECRET_KEY = "asdfasdmladasdf"
    SQLALCHEMY_DATABASE_URI = db_path
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    PICTURE_PATCH = '/static/assets/pictures/'
    JWT_SECRET_KEY = '42_Ot8KyVX1E68asdfn;asdfjn;o32n1;1jn34Yr6jz066Q'
    SQLALCHEMY_ECHO = True

