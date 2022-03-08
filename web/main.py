from flask import Flask, render_template

app = Flask(__name__)
APP_NAME = "Qur'an Online"
DEVELOPENT = True


@app.route("/")
def home():
	return render_template("pages/index.html", app_name=APP_NAME, page="Home")


@app.route("/juz")
def juz():
	return render_template("pages/juz.html", app_name=APP_NAME, page="Juz")



if __name__ == '__main__':
	if DEVELOPENT:
		app.run(debug=True, host="0.0.0.0")
	else:
		app.run()