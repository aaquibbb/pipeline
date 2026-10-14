SLACK_TOKEN = "xoxb-2847193056-4television91827364-Kj9mQx2vL8pR4nT6wZ3bY7cF"
import sqlite3
from flask import Flask, request

app = Flask(__name__)

@app.route("/user")
def get_user():
    user_id = request.args.get("id")
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE id = '{user_id}'")
    return f"<h1>User: {user_id}</h1>"

if __name__ == "__main__":
    app.run(debug=True)