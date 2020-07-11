import os
import subprocess
import win32com
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from pathlib import Path
from win32com.client import Dispatch

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

@app.route("/")
def teste():
    path = './users/user1/'
    
    if(not os.path.exists(path)):
        print("teste")
        os.makedirs(path)
    
    fileName = "routes1.py"
    fileBD = "db.sqlite"
    fileObj = Path(path + fileName)
   
    if(fileObj.is_file()):
        
        #f = open("./users/user1/routes1.py", "+")
        with open("./users/user1/routes1.py", "r") as in_file:
            buf = in_file.readlines()
            
        with open("./users/user1/routes1.py", "w") as out_file:
            for line in buf:
                #print("##CREATEMETHOD##" in line)
                if("##CREATEMETHOD##" in line):
                    line = line + "\n\n"
                    out_file.write(line)
                    out_file.write('@app.route("/get", methods=["GET"])\n')
                    out_file.write("def methodGet1():\n")
                    out_file.write("    path = './users/user1/'")
                else:
                    out_file.write(line)
        out_file.close()    
    else:
        template = """
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


if __name__  == '__main__':
    app.run(host="localhost", port=8000, debug=True)
        """
        outF = open(path+fileName, "w")
        outF.write(template) 
        outF.close()
        
        outB = open( path + fileBD, "w")
        outB.close()
    return render_template("route.html")
    
@app.route("/index")
def index():
    return render_template("route.html")

@app.route("/cadastrar")
def cadastrar():
    return render_template("cadroute.html")

@app.route("/cadastro", methods = ['GET', 'POST'])
def cadastro():
    if request.method == "POST":
        name = request.form.get("name")
        type= request.form.get("type")
        print('1')
        if name and type:
            print('2')
            r = Route(name, type)
            db.session.add(r)
            db.session.commit()
    return redirect(url_for("index"))

@app.route("/list")
def lista():
    routes = Route.query.all()
    
    return render_template("listroute.html", routes = routes)


@app.route("/app")
def teste10():
    WshShell = win32com.client.Dispatch("WScript.Shell")
    WshShell.run("cmd ", "cmd") 

if __name__  == '__main__':
    app.run(debug= True)
