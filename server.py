from flask import Flask
from flask import render_template
from flask import send_from_directory
import sys
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('map.html')


@app.route('/js/<path:path>')
def send_js(path):
	return send_from_directory('./static/js', path)

@app.route('/css/<path:path>')
def send_css(path):
	return send_from_directory('./static/css', path)

if __name__ == "__main__":
	app.run()