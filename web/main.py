from utils import *
from flask import Flask, render_template, request

app = Flask(__name__)
APP_NAME = "Qur'an Online"
DEVELOPENT = True


@app.route("/")
def home():
	return render_template(
		"pages/index.jinja", 
		app_name=APP_NAME, 
		page="Home"
	)


@app.route("/juz")
def juz():
	if "juz" in request.args:
		juz = request.args.get('juz')
		return render_template(
			"pages/isi_juz.jinja", 
			app_name=APP_NAME, 
			page=f"Juz {juz}", 
			juz=juz
		)

	else:
		all_juz = list_divider(6, [i for i in range(1, 31)])
		return render_template(
			"pages/juz.jinja", 
			app_name=APP_NAME, 
			page="Juz", 
			all_juz=all_juz
		)


@app.route("/surah")
def surah():
	if "surah" in request.args:
		surah = request.args.get('surah')
		return render_template(
			"pages/isi_surah.jinja", 
			app_name=APP_NAME, 
			page=f"Surah {surah}", 
			surah=surah
		)

	else:
		return render_template(
			"pages/surah.jinja", 
			app_name=APP_NAME, 
			page="Surah"
		)

@app.route("/cari")
def cari():
	return render_template(
		"pages/cari.jinja", 
		app_name=APP_NAME, 
		page="Cari Potongan Ayat"
	)


if __name__ == '__main__':
	if DEVELOPENT:
		app.run(debug=True, host="0.0.0.0")
	else:
		app.run()
