#Team Urals                                                                
#Karina Ionkina and Holden Higgins                                          
#SoftDev1 pd7                                                                 
#HW08-  Do I Know You?                                                      
#2017-10-11  

from flask import Flask,flash, render_template, request, session, redirect, url_for
import os

app = Flask(__name__)

user = "soft"
paswd = "diva"
 

app.secret_key = os.urandom(32)


# root route renders welcome.html and login.html
@app.route("/")
def root():
    if "username" in session:
        return render_template("welcome.html")
    else: 
        return render_template("login.html")


# action from form, redirects to root
@app.route("/auth", methods = ["POST", "GET"])
def authenticate():
    if request.form != {}:
        if request.form["user"] != user:
            flash('Thy username is incorrect. Tryeth Again?')
        elif request.form["paswd"] != paswd:
            flash('Thy password is incorrect. Tryeth Again?')
        elif request.form["user"] == user and request.form["paswd"] == paswd:
            session['username'] = request.form["user"]
    else:
        ""
    return redirect(url_for("root"))
    
# logs out and redirects to root
@app.route("/logout")
def logout():
    session.pop("username")
    return redirect(url_for("root"))

if __name__ == "__main__":
    app.debug = True
    app.run()
