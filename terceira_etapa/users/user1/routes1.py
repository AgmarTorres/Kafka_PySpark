
import os
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from pathlib import Path

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(app)


class Route(db.Model):
    __tablename__ = 'route'
    _id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String)
    type = db.Column(db.String)
    
    def __init__(self, name, type):
        self.name = name
        self.type = type
            
#Cria no banco de dados
db.create_all()

@app.route("/", methods=['GET'])
def methodGet():
    path = './users/user1/'
    print("get")
        
    return render_template("index.html")

##CREATEMETHOD##


@app.route("/get", methods=["GET"])
def methodGet1():
    path = './users/user1/'

if __name__  == '__main__':
    app.run(host="localhost", port=8000, debug=True)
        