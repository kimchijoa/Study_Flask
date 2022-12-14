import sys, os
import configparser as propser
import sqlalchemy as db
import sqlalchemy.orm as db_orm
from sqlalchemy.ext.declarative import declarative_base

prop = propser.ConfigParser()
prop.read(r'C:/Users/amsmd/Downloads/Study_Flask-master/Study_Flask-master/config.ini', encoding='utf-8')
DB_CONF = prop['DB_SET']

#각각 Session, Engine, Base 반환
class connection:
    def getSeesion():
        #python mysql 접근시 pymysql 의존성이 필요
        #mysql+pymysql://{유저명}:{패스워드}@{ip}:{port}/{schema}?charset=utf8', convert_unicode=False
        engin = db.create_engine('%s' %(DB_CONF['full_host']))
        Session = db_orm.sessionmaker()
        Session.configure(bind=engin)
        return Session

    def getEngine():
        engine = db.create_engine('%s' %(DB_CONF['full_host']))
        return engine

    def getBase():
        return declarative_base()

