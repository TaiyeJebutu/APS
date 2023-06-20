# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, redirect, url_for, request


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
        user = request.form['username']
        return redirect(url_for('success', name = user))
    else:
        user = request.args.get('username')
        return redirect(url_for('success', name =user))



#Main driver function

if __name__ == "__main__":

    # run() method of Flask class runs the application
    # on the local development server.
    app.run(debug=True)









