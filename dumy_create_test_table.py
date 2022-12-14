# import sqlalchemy as db
# #import models.connection as conn
# from models import connection as conn

# if __name__ == "__main__":
#     conn = conn.connection.getEngine()
#     metadata = db.MetaData()
#     user_table = db.Table(
#         'test_table',  # 데이터베이스에 저장될 table 이름입니다.
#         metadata,
#         db.Column('id', db.Integer, primary_key=True),  # 이 테이블에 들어갈 컬럼입니다.
#         db.Column('name', db.String(30)),
#         db.Column('fullname', db.String(30)),
#     )

#     metadata.create_all(conn)
