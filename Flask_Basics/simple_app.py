"""

Simplest Flask App that uses decorator and routes

Decorator( @ ) :- Decorator is like you are extending "app" instance with below function. ex: You are adding hello_world() function that you wrote
with the app instance. So basically you added extra feature.

Route Method:- route function routes the request to the particular function. By default it approves only GET request. for other you have to write 
it like this - 
@app.route('/api/go',methods=['POST','GET']) 

The following function will approve both GET and POST request. 

Route Variables:- 
@app.route('/api/<name>')

here name is a placeholder. You can use this in the function as a variable

we can specify the type of the placeholder like this:-
@app.route('/api/<string: name>')

Request Query String:-

@app.route('/query')
def query():
    n = request.args.get('name')
    l = request.args.get('location')

    return f"Your name is {n} and your location is {l}"

add query?name=Something&location=place_name to get the output

"""

from flask import Flask, jsonify, request

app = Flask(__name__) #Flask instance

@app.route('/') #decorator 
def hello_world():
    return "Hello World"


@app.route('/api/go',methods=['GET','POST']) #The go function can be accessed with both GET and POST request
def go():
    return "<h1>go</h1>"


@app.route('/pname',methods=['GET','POST'],defaults={'<string:name>': 'Default_name'}) #default value for <name>
@app.route('/pname/<string:name>',methods=['GET','POST'])    # Here <name> is a kind of variable
def printing_name(name):
    return f"Hello {name}"


@app.route('/query')
def query():
    n = request.args.get('name')
    l = request.args.get('location')

    return f"Your name is {n} and your location is {l}"

@app.route('/json')
def json():
    return jsonify({'key1' : 'value1', 'key2' : 'value2'}) #converts dictionary to JSON

if __name__=="__main__":
    app.run(debug = True)


