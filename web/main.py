from flask import Flask, render_template

app = Flask(__name__)
APP_NAME = "Qur'an Online"


@app.route("/")
def home():
	return render_template("pages/index.html", app_name=APP_NAME)



if __name__ == '__main__':
	app.run(debug=True, host="0.0.0.0")