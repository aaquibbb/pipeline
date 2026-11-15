import sqlite3
from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/user")
def get_user():
    user_id = request.args.get("id")
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    return render_template_string("<h1>User: {{ uid }}</h1>", uid=user_id)

if __name__ == "__main__":
    app.run(debug=True)