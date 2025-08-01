
from flask import Flask, render_template, request, redirect, send_from_directory, session, url_for
import os
import json

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load user credentials
with open('users.json') as f:
    USERS = json.load(f)

# Ensure upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        uname = request.form['username']
        passwd = request.form['password']
        if uname in USERS and USERS[uname] == passwd:
            session['user'] = uname
            return redirect('/dashboard')
        else:
            return render_template('login.html', error='Invalid credentials')
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect('/')
    files = os.listdir(UPLOAD_FOLDER)
    return render_template('dashboard.html', files=files)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if 'user' not in session:
        return redirect('/')
    if request.method == 'POST':
        file = request.files['file']
        if file:
            file.save(os.path.join(UPLOAD_FOLDER, file.filename))
            return redirect('/dashboard')
    return render_template('upload.html')

@app.route('/download/<filename>')
def download(filename):
    if 'user' not in session:
        return redirect('/')
    return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True)

@app.route('/delete/<filename>')
def delete(filename):
    if 'user' not in session:
        return redirect('/')
    os.remove(os.path.join(UPLOAD_FOLDER, filename))
    return redirect('/dashboard')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
