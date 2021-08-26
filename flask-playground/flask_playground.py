# from the docs
# https://flask.palletsprojects.com/en/2.0.x/quickstart/#sessions

from flask import Flask, session, redirect, request, url_for

app = Flask(__name__)

app.config['DEBUG'] = True
app.secret_key = 'radnomint1919382929283'


@app.route('/')
def index():
    # <SecureCookieSession {}> is empty by default
    print(session)
    if 'username' in session:
        return f'Logged in as {session["username"]}'
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))
