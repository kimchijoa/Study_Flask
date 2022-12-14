import sqlalchemy as db
import db_connection as conn

session = conn.connection.getSeesion()
base = conn.connection.getBase()

class TestTable(base):
    __tablename__ = "test_table"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    fullname = db.Column(db.String(30))
