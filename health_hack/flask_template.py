import json

from urllib import request
from flask import Flask, render_template, request, redirect, jsonify
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__, template_folder='templateFiles', static_folder='staticFiles')
#app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///donros.sqlite3'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)
#db.init_app(app)

class donors(db.Model):
    uname = db.Column('user_name', db.String(30), primary_key=True)
    email = db.Column(db.String(30), unique=False, nullable=False)
    passwd = db.Column(db.String(30), unique=False, nullable=False)
    cpasswd = db.Column(db.String(30), unique=False, nullable=False)

def __init__(self, uname, email, passwd, cpasswd):
    self.uname = uname
    self.email=email
    self.passwd = passwd
    self.cpasswd = cpasswd

#db.create_all()

#db.session.add(model object)

   
    

@app.route('/', methods=["GET","POST"])
def index():
    if request.method == "POST":
        user_name = request.index.get("uname")
        print(user_name)
        return user_name
    return render_template('index.html')





 
if __name__=='__main__':
    db.create_all()
    app.run(debug = True)

quit()