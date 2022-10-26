from re import A
from flask import Flask, render_template, request, url_for, redirect, session
from pymongo import MongoClient
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
login_manager = LoginManager()

import subprocess, bcrypt

#####################################################################

client = MongoClient(host = "localhost", port = 27017)
db = client.Project

#####################################################################

app=Flask(__name__)
app.secret_key = "app"
login_manager.init_app(app)
login_manager.session_protection = "strong"
login_manager.login_view = 'login'

#####################################################################

# global
USERNAME = ""

#####################################################################

class User(UserMixin):
    pass

@login_manager.user_loader
def user_loader(email):
	# if email not in users
	if len(list(db.USER.find({"email": email}))):
		user = User()
		user.id = email
		return user
	return


@login_manager.request_loader
def request_loader(request):
	email = request.form.get('email')
	
	if len(list(db.USER.find({"email": email}))):
		user = User()
		user.id = email
		return user
	return

#####################################################################

@app.route("/")
def index():
	print("username = " + USERNAME)
	return render_template("index.html", username = USERNAME)

@app.route("/login", methods=["GET", "POST"])
def login():

	if request.method == "GET":
		if current_user.is_authenticated:
			return redirect(url_for("index"))
		return render_template("login.html")
	
	email = request.form["email"]
	password = request.form["password"]

	if len(list(db.USER.find({"email": email}))):
		password_val = db.USER.find({"email": email})[0]["password"]
		if bcrypt.checkpw(password.encode('utf-8'), password_val):
			user = User()
			user.id = email
			login_user(user)
			global USERNAME
			USERNAME = db.USER.find({"email": current_user.id})[0]["username"]
			return redirect(url_for("index"))

	return render_template("login.html", msg = "invalid password or email")
	#subprocess.Popen("python3 ./mydatabase/test.py", shell=True)

# register
@app.route("/register", methods=["GET", "POST"])
def register():
	if request.method == "GET":
		return render_template("register.html")

	username = request.form["username"]
	email = request.form["email"]
	password = request.form["password"]

	if len(list(db.USER.find({"email": email}))) > 0:
		email_msg = "email is used"
		return render_template("register.html", email_msg = email_msg, username = username, password = password)
	
	db.USER.insert_one({"username": username, "email": email, "password": bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())})
	user = User()
	user.id = email
	login_user(user)
	global USERNAME
	USERNAME = db.USER.find({"email": current_user.id})[0]["username"]
	return redirect(url_for("index"))

# logout
@app.route("/logout")
def logout():
	logout_user()
	global USERNAME
	USERNAME = ""
	return render_template('index.html')

# product
@app.route("/product")
def product():
	return render_template('product.html', username = USERNAME)




## v
# @app.route("/VMDinfo")
# def vmdinfo():
# 	if password == None:
# 		return redirect(url_for("getPwd"))
# 	else:
# 		out = subprocess.Popen("sh VMDinfo.sh " + password, shell=True, stdout=subprocess.PIPE).stdout.read()
# 		out = out.decode().replace(""", "")
# 		cells = [out.split()]
# 		return render_template("test.html", cells = cells, len = len(cells))
# @app.route("/create-raid")
# def create():
# 	return render_template("create-raid.html")
# ## create volume v
# @app.route("/create-volume")
# def createVolume():
# 	if password == None:
# 		return redirect(url_for("getPwd"))
# 	else:
# 		return render_template("create-volume.html")
# ## volume-validate x
# @app.route("/generate-volume", methods=["POST"])
# def generateVolume():
# 	if password == None:
# 		return redirect(url_for("getPwd"))
# 	else:
# 		validate = subprocess.Popen("sh volume-validate.sh" + password, shell=True, stdout=subprocess.PIPE).stdout.read()
# 		if not validate:
# 			redirect(url_for("create-volume"))
# 		level = request.form["level"]
# 		count = request.form["count"]
# 		volName = request.form["volName"]
# 		disks = request.form["disks"]
# 		out = subprocess.Popen("sh genVolume.sh " + password, shell=True, stdout=subprocess.PIPE).stdout.read()
# 		out = out.decode().replace(""", "")
# 		return render_template("index.html")

# ## create container v
# @app.route("/create-container")
# def createContainer():
# 	if password == None:
# 		return redirect(url_for("getPwd"))
# 	else:
# 		return render_template("create-container.html")
# ## container-validate x
# @app.route("/generate-container", methods=["POST"])
# def generateContainer():
# 	if password == None:
# 		return redirect(url_for("getPwd"))
# 	else:
# 		# run validate shell
# 		validate = subprocess.Popen("sh container-validate.sh" + password, shell=True, stdout=subprocess.PIPE).stdout.read()
# 		if not validate:
# 			redirect(url_for("create-container"))
# 		# if pass, create raid
# 		out = subprocess.Popen("sh sample.sh" + password, shell=True, stdout=subprocess.PIPE).stdout.read()
# 		return render_template("index.html", out = out)

# ## dashboard x
# @app.route("/info")
# def getInfo():
# 	if password == None:
# 		return redirect(url_for("getPwd"))
# 	else:
# 		out = subprocess.Popen("sh example.sh" + password, shell=True, stdout=subprocess.PIPE).stdout.read()
# 		return render_template("index.html", out = out)

# ## delete
# @app.route("/delete/<deviceName>", methods=["POST"])
# def delete(deviceName):
# 	if password == None:
# 		return redirect(url_for("getPwd"))
# 	else:
# 		out = subprocess.Popen("sh delete.sh" + password + deviceName, shell=True, stdout=subprocess.PIPE).stdout.read()
# 		return render_template("index.html", out = out)



if __name__ == "__main__":
	app.run(host="127.0.0.1",port="5001",debug=True)