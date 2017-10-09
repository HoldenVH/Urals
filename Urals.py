#Team Urals
#Karina Ionkina and Holden Higgins
#SoftDev1 pd7
#HW08-
#2017-10-06


from flask import Flask, render_template, request, session, redirect, url_for
import os #for secret key

app = Flask(__name__)

#hard coded username and password combo :(
user = "JohnSmith"
pwd = "abc123"

#we need a secret key
app.secret_key = os.urandom(32)

#assign following fxn to run when
#root route requested
@app.route("/")
def hello_world():
    print(session)
    #this only activates if a session is active
    if 'username' in session:
        return "Welcome John <br> <a href = '/logout'> logout </a>"
    else:
        return render_template("login.html")
    

#page to process form submission    
@app.route("/auth")
def authenticate():
    #diag:
    print (request.method)
    print (request.args)
    if request.args['username'] == user:
        if request.args['password'] == pwd:
            session['username'] = request.args['username']
            return redirect(url_for(hello_world))
        else:
            return "Error: wrong password"
    else:
        return "Error: wrong username"

#page to logout, will be accessible through link    
@app.route("/logout")
def end_session():
    session.pop('username')
    return "You have been logged out"

if __name__ == "__main__":
    app.debug = True
    app.run()

