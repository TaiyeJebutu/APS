# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, redirect, url_for, request
from database import database


# Flask constructor takes the name of
# current module (__name__) as argument.

app = Flask(__name__)

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
def helloWorld():
    return "Hello World !!"

@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name


@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if checkUsernameAndPassword(username,password):
            return redirect(url_for('success', name=username))
        else:


    else:
        username = request.args.get('username')
        return redirect(url_for('success', name =username))



def checkUsernameAndPassword(username:str, password:str) -> bool:
    aps_database = database()
    aps_database.loadDatabase("APS_Database.json")

    isValid = aps_database.checkUsernameAndPassword(username, password)
    return isValid



#Main driver function

if __name__ == "__main__":

    # run() method of Flask class runs the application
    # on the local development server.
    app.run()









