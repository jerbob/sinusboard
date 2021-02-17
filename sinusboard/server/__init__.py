"""Web dashboard for playing soundboard content."""

from flask import Flask
from flask.templating import render_template


app = Flask(__name__)


@app.route("/")
def index():
    """Route for the dashboard template."""
    return render_template("index.html")


@app.route("/service-worker.js")
def service_worker():
    return app.send_static_file("service-worker.js")
