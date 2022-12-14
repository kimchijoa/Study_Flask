import sys
print(sys.path)
from ...migrate.models.db_connection import connection as conn;
from ...migrate.models import test_table as test_tb;
from flask import Flask
import sqlalchemy as db


app = Flask(__name__)
@app.route('/api/v1/select-test', methods=['GET'])
def api_v1_select():
    session = conn.connection.getSeesion()
    base = conn.connection.getBase()
    test_table = test_tb.TestTable(base)
    session.add(test_table(id=1, name="김기환", fullname="부산 김기환"))
    session.commit()
    session.close()
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)