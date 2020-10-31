"""
Redirect:- Redirects user from one page to another
url_for:- Generates a URL to the given endpoint with the method provided.

flask.session:- flask.session is like a dictionary. Whatever key-value pair is used in session dictionary is saved in cookies and 
so anyone can read it. Hence app.config['SECRET_KEY] = True is required so that even though they can read it, they cannot modify it.

"""


from flask import Flask, jsonify, request,redirect, url_for, session

app = Flask(__name__) #Flask instance
app.config['DEBUG'] = True #instead of wrinting app.run(debug=True) you can use this dictionary
app.config['SECRET_KEY'] = "1234567" 


@app.route('/')
def index():
    session.pop('name',None)
    return "Hello World"

@app.route('/home',methods=["GET","POST"],defaults={"name" : "Default_name"})
@app.route('/home/<name>',methods=["GET","POST"])
def home(name):
    session['name'] = name # Now it can be used and called from any function
    return f"<h1>Hi {name}. You are in the home page</h1>"


@app.route('/theform',methods = ['GET','POST'],)
def theform():
    if request.method == "GET":    

        return '''
        <form method="POST" action="/theform">    
        <input type ="text" name="name">
        <input type ="text" name ="location">
        <input type ="submit" value = "Submit">
        </form>
        '''
    else:
        name = request.form['name']
        location = request.form['location']

        return redirect(url_for('home',name = name,location = location))


@app.route('/json',methods=['POST','GET'])
def json():

    if 'name' in session:
        name = session['name']
    else:
        name = "NameNotAvailable"

    return jsonify({'key': 'value', 
                    'name' : name})

if __name__=="__main__":
    app.run()


