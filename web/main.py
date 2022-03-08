from utils import *
from flask import Flask, render_template, request

app = Flask(__name__)
APP_NAME = "Qur'an Online"
DEVELOPENT = True


@app.route("/")
def home():
	return render_template(
		"pages/index.html", 
		app_name=APP_NAME, 
		page="Home"
	)


@app.route("/juz")
def juz():
	if "juz" in request.args:
		juz = request.args.get('juz')
		return render_template(
			"pages/isi_juz.html", 
			app_name=APP_NAME, 
			page=f"Juz {juz}", 
			juz=juz
		)

	else:
		all_juz = list_divider(6, [i for i in range(1, 31)])
		return render_template(
			"pages/juz.html", 
			app_name=APP_NAME, 
			page="Juz", 
			all_juz=all_juz
		)



if __name__ == '__main__':
	if DEVELOPENT:
		app.run(debug=True, host="0.0.0.0")
	else:
		app.run()