"""

Request Query String:-

@app.route('/query')
def query():
    n = request.args.get('name')
    l = request.args.get('location')

    return f"Your name is {n} and your location is {l}"

add query?name=Something&location=place_name to get the output

Request Form Data:-

The way data is received from HTML form:- 

@app.route('/process',methods=['POST'])
def process():
    name = request.form['name']
    location = request.form['location']

"""


from flask import Flask, jsonify, request

app = Flask(__name__) #Flask instance


@app.route('/query')
def query():
    n = request.args.get('name')
    l = request.args.get('location')

    return f"Your name is {n} and your location is {l}"

@app.route('/theform')
def theform():
    return '''
        <form method="POST" action="/process">
        <input type ="text" name="name">
        <input type ="text" name ="location">
        <input type ="submit" value = "Submit">
        </form>
    '''

@app.route('/process',methods=['POST'])
def process():
    name = request.form['name']
    location = request.form['location']

    return f"<h1>Hi {name}. You are from {location}<h2>"



if __name__=="__main__":
    app.run(debug = True)


