import sys
print(sys.path)
import db_connection as conn;
import test_table as test_tb;
from flask import Flask;
import sqlalchemy as db;
import json;
import pandas as df


app = Flask(__name__)
@app.route('/api/v1/select-test', methods=['GET'])
def api_v1_select():
    try:
        session = conn.connection.getSeesion()
        #base = conn.connection.getBase()
        test_table = test_tb.TestTable
        result = session.query(test_table).all()
        result = df.read_sql(session.query(test_table).all(), session.bind)
        print(json.loads(result.to_json()))
        return json.dumps(result)
    except:
        return 'Data Get failed'

@app.route('/api/v1/post-test', methods=['POST'])
def api_v1_post():
    try:
        session = conn.connection.getSeesion()
        #base = conn.connection.getBase()
        test_table = test_tb.TestTable
        session.add(test_table(name="김기환", fullname="부산 김기환"))
        session.commit()
        session.close()
        return 'Data Post Success'
    except:
        return 'Data Post failed'

if __name__ == '__main__':
    app.run(debug=True)