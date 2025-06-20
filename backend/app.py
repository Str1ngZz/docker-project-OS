from flask import Flask
import os
import psycopg2

app = Flask(__name__)

@app.route('/')
def index():
    conn = psycopg2.connect(
        host='db',
        database='db_1',
        user='user1',
        password='user123'
    )
    cur = conn.cursor()
    cur.execute("SELECT 'ТОВА Е ТЕСТ!'")
    result = cur.fetchone()
    cur.close()
    conn.close()
    return result[0]

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
