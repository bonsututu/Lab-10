from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    conn = sqlite3.connect('poems.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM poems')
    poems = cursor.fetchall()
    conn.close()
    return render_template('index.html', poems=poems)

if __name__ == '__main__':
    app.run(debug=True)
