import sqlalchemy as db
#import models.connection as conn
from ..models import connection as conn


class TestTable:
    conn = conn.connection.getEngine()
    metadata = db.MetaData()
    table = db.Table('test_table', metadata, autoload=True, autoload_with=conn)
    query = db.select([table])
    print(query)

