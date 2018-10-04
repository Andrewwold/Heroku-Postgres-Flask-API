from flask import Flask, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy

from flask.ext.heroku import Heroku

app = Flask(__name__)                                               #enter desired data base here
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://dwzbepecelznac:d2a5da13e4526615275c87861219d0a1edd953678c46b49ab1bbc1d4caabfb8c@ec2-75-101-153-56.compute-1.amazonaws.com:5432/ddvnnv3uogu6aa'
heroku = Heroku(app)
db = SQLAlchemy(app)

# Create our database model
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, email):
        self.email = email

    def __repr__(self):
        return '<E-mail %r>' % self.email

# Set "homepage" to index.html
@app.route('/')
def index():
    return render_template('index.html')

# Save e-mail to database and send to success page
@app.route('/prereg', methods=['POST'])
def prereg():
    email = None
    if request.method == 'POST':
        email = request.form['email']
        # Check that email does not already exist (not a great query, but works)
        if not db.session.query(User).filter(User.email == email).count():
            reg = User(email)
            db.session.add(reg)
            db.session.commit()
            return render_template('success.html')
    return render_template('index.html')

@app.route('/return_emails', methods=['GET'])
    db.session.query(User)
    


if __name__ == '__main__':
    app.debug = True
    app.run()