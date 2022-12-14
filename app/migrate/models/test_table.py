import sqlalchemy as db
import db_connection as conn

session = conn.connection.getSeesion()
base = conn.connection.getBase()

class TestTable(base):
    __tablename__ = "mobile"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    fullname = db.Column(db.String(30))
# class TestTable(base):
#     def select_tb():

# metadata = db.MetaData()
# user_table = db.Table(
#      'test_table',  # 데이터베이스에 저장될 table 이름입니다.
#      metadata,
#      db.Column('id', db.Integer, primary_key=True),  # 이 테이블에 들어갈 컬럼입니다.
#      db.Column('name', db.String(30)),
#      db.Column('fullname', db.String(30)),
#  )

# metadata.create_all(conn)
