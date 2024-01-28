from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

def connect_db():
    try:
        connection = psycopg2.connect(
            dbname="sasepasser",
            user="postgres",
            password="123456",
            host="localhost",
            port="5432"
        )
        return connection
    except Exception as e:
        return str(e)

@app.route('/')
def index():
    connection = connect_db()
    if isinstance(connection, psycopg2.extensions.connection):
        return jsonify({"message": "Connected to PostgreSQL database successfully!"})
    else:
        return jsonify({"error": connection})

if __name__ == '__main__':
    app.run(debug=True)
