import sqlalchemy as db
import connection as conn

conn = conn.connection_engine.engine()
metadata = db.MetaData()
user_table = db.Table(
     'test_table',  # 데이터베이스에 저장될 table 이름입니다.
     metadata,
     db.Column('id', db.Integer, primary_key=True),  # 이 테이블에 들어갈 컬럼입니다.
     db.Column('name', db.String(30)),
     db.Column('fullname', db.String(30)),
 )

metadata.create_all(conn)
