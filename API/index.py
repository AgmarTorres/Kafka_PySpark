import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True

fruits = ["apple", "banana", "cherry"]
TYPES = ["GET", "GET", "POST"]
for x in range(len(fruits)):
    if x == 0:
        @app.route('/{}'.format(fruits[x]), methods=[TYPES[x]])
        def a():
            return 'apple'
    if x == 1:
        @app.route('/{}'.format(fruits[x]), methods=[TYPES[x]])
        def b():
            return 'banana'
        
    if x == 2:
        @app.route('/{}'.format(fruits[x]), methods=[TYPES[x]])
        def c():
            return 'cherry'
    

app.run()
