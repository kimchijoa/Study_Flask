import sqlalchemy as db
import models.connection as conn

metadata = db.MetaData()
conn = conn.connection_engine.engine()

select_test_table = db.Table('test_table', metadata, autoload_with=conn)