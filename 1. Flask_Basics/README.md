## Activating Virtual Environment (For Ubuntu-20.04 LTS)

**It is important to do, so that whatever package you install for this project doesn't affect others**

**Install Pip**

`sudo apt install python3-pip`

**Installing Virtual Environment**

`sudo apt-get install python3-venv`

**Creating Virtual Environment**

`python3 -m venv flask_env` 

(flask_env is just the name of the environment. You can use whatever you want as a name.)

**Activating Virtual Environment**

`source flask_env/bin/activate` 

**Installing Flask**

`pip3 install flask` 

**Dectivating Virtual Environment**

`deactivate` 

---

## Required Info for simple_app.py 

### Decorator (@)

`@app.route('/')` 

  Decorator is like you are extending "app" instance with below function. ex: You are adding hello_world() function that you wrote
with the app instance. So basically you added extra feature.

### Route

**Route Method**

Route function routes the request to the particular function. By default it approves only GET request. for other you have to write 
it like this - 

  `@app.route('/api/go',methods=['POST','GET'])`

  The following function will approve both GET and POST request. 

**Route Variable**

`@app.route('/api/<name>')`

here "name" is a placeholder. You can use this in the function as a variable. We can also specify the type of the placeholder like this:-

`@app.route('/api/<string: name>')` or `@app.route('/api/<int: name>')`

---

## Required Info for request_app.py 

**Request Query String**`

```
@app.route('/query')
def query():
    n = request.args.get('name')
    l = request.args.get('location')

    return f"Your name is {n} and your location is {l}"
```

add this at the end of the URL to see the output:- _?name=Something&location=place_name_

**Request Form Data**

```
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

```

request comes to the '/theform'. When the form is filled up and submitted as action="/process" the url will change to the "/process" and execute that route logic. 
request.form['name'] is the way data is received from form.

**Request JSON Data**

```
@app.route('/processjson',methods=['POST'])
def jsonprocess():

    data = request.get_json() 
    
    name = data['name']
    loc = data['location']
    random_list = data['randomlist']


    return jsonify({'Result':'Success', 
                    'Name' : name, 
                '    location' : loc,
                     'A_List' : random_list[1] })


```

converts JSON data to python dictionary and processes it.



---


## Required Info for Redirection

**redirect()**

Redirects user from one page to another

**url_for()** :

Generates a URL to the given endpoint with the method provided.


**flask.session**

flask.session is like a dictionary. Whatever key-value pair is used in session dictionary is saved in cookies and 
so anyone can read it. Hence _app.config['SECRET_KEY] = True_ is required so that even though they can read it, they cannot modify it.

**flask.session**

Always keep _app.config['DEBUG']=True_ for debug purpose and when app goes live turn it off.

---