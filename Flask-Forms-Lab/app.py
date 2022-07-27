from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "llo2ay"
password = "123"
facebook_friends=["Loai","Yonathan","Adan", "George", "Fouad", "Celina"]


@app.route('/', methods=["GET", "POST"])  # '/' for the default page
def login():
	if request.method == "GET":
		return render_template('login.html')
	else:
		username1 = request.form["username"]
		password1 = request.form["password"]
		if username == username1 and password == password1:
			print("")
			return redirect(url_for('home'))
		else: 
			return render_template("login.html")

@app.route('/home', methods=["GET", "POST"])  # '/' for the default page
def home():
	if request.method == "GET":
		return render_template('home.html', ff = facebook_friends)

@app.route('/friend_exits/<string:name>', methods=["GET", "POST"])  # '/' for the default page
def the_friend_exits(name):
	check=False
	for x in facebook_friends:
		if x==name:
			check=True
	return render_template('friend_exists.html', name=name, check=check)




	




if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)