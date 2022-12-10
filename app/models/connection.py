import sys, os
import configparser as propser
import sqlalchemy as db
import sqlalchemy.orm as db_orm

prop = propser.ConfigParser()
prop.read('config.ini', encoding='utf-8')
DB_CONF = prop['DB_SET']
class connection_engine:
    def engine():
        #python mysql 접근시 pymysql 의존성이 필요
        #mysql+pymysql://{유저명}:{패스워드}@{ip}:{port}/{schema}?charset=utf8', convert_unicode=False
        return db.create_engine('%s' %(DB_CONF['full_host']), convert_unicode=False)

    def session():
        Session = db_orm.sessionmaker(connection_engine.engine())
        return Session()
