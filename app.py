from flask import Flask, request, redirect, url_for, render_template, session, flash, g, jsonify
import sqlite3
import bcrypt
from deepseek import deepseek

app = Flask(__name__)
app.secret_key = 'your_secret_key'
model = deepseek()

DATABASE = 'chatbot_users.db'
port = 9090

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row  
    return g.db

@app.teardown_appcontext
def close_connection(exception):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_db():
    with app.app_context():
        db = get_db()
        db.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT UNIQUE NOT NULL,
                        password TEXT NOT NULL
                      )''')
        db.commit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if not all([username, password]):
            flash('All fields are required!')
            return redirect(url_for('register'))

        db = get_db()
        existing_user = db.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()

        if existing_user:
            flash('Username already taken. Please log in.')
            return redirect(url_for('login'))

        # Hash the password before storing it
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        try:
            db.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
            db.commit()
            flash('Registration successful! Please log in.')
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            db.rollback()
            flash('An error occurred. Please try again.')

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if not all([username, password]):
            flash('All fields are required!')
            return redirect(url_for('login'))

        db = get_db()
        user = db.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()

        if user and bcrypt.checkpw(password.encode('utf-8'), user['password']):
            session['username'] = user['username']
            flash('Login successful!')
            return redirect(url_for('chat'))
        else:
            flash('Invalid username or password.')

    return render_template('login.html')

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        user_input = request.form['message']
        bot_response = chatbot_response(user_input)
        return jsonify({'response': bot_response})
    
    return render_template('chat.html')

def chatbot_response(user_input):
    respond = model.get_message(user_input)
    return respond

if __name__ == '__main__':
    init_db()
    app.run(host="0.0.0.0", port=9090, debug=True)

