from flask import Flask, send_file
from psycopg2 import connect

app = Flask(__name__)

host = 'localhost'
port = 5432
dbname = 'rhy'
user = 'postgres'
password = 'a'

def get_connection():
    conn = connect (host=host, port=port, dbname=dbname, user=user, password=password)
    return conn

@app.route('/')
def index():
    return send_file('web/index.html')



if __name__ == '__main__':
    app.run(debug=True)