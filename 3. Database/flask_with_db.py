"""

"""


from flask import Flask, jsonify, request,redirect, url_for, session, render_template,g
import sqlite3

app = Flask(__name__) #Flask instance
app.config['DEBUG'] = True #instead of wrinting app.run(debug=True) you can use this dictionary
app.config['SECRET_KEY'] = "1234567" 

def connect_db():
    """
        Connects Flask App with Database
    """

    sql = sqlite3.connect('/mnt/c/Users/dipon/Documents/Python Flask/data.db')
    sql.row_factory = sqlite3.Row #converts row tuples into row dictionary
    
    return sql

def get_db():
    if not hasattr(g, 'sqlite3'):
        g.sqlite_db = connect_db() # g is a global object
    return g.sqlite_db

@app.teardown_appcontext #automatically called when route returns
def close_db(error ):
    if hasattr(g,'sqlite_db'):
        g.sqlite_db.close(  )


@app.route('/')
def index():
    session.pop('name',None)
    return "Hello World"

@app.route('/home',methods=["GET","POST"],defaults={"name" : "Default_name"})
@app.route('/home/<name>',methods=["GET","POST"])
def home(name):
    session['name'] = name # Now it can be used and called from any function
    return render_template('home_page.html',html_name = name, display = True,
                            mylist = ['one','two','three'],
                            my_dict = [{'name' : 'Dipon'}, {'name' : 'Srijon'}])


@app.route('/theform',methods = ['GET','POST'],)
def theform():
    if request.method == "GET":    

        #return render_template('form_page.html')
        return render_template('form_page_2.html')
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


