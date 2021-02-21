"""Web dashboard for playing soundboard content."""

from flask import Flask
from flask.templating import render_template
from whitenoise import WhiteNoise

from sinusboard import client

app = Flask(__name__)


def get_duration(milliseconds: int) -> str:
    """Get a displayable label for duration given milliseconds."""
    seconds = int(milliseconds * 0.001)
    minutes, seconds = divmod(seconds, 60)
    return f"{minutes:02d}:{seconds:02d}"


@app.route("/")
def index():
    """Route for the dashboard template."""
    files = (
        {
            "name": file.get("title"),
            "uuid": file.get("uuid"),
            "length": get_duration(file.get("duration", 0)),
        }
        for file in client.session.get(f"{client.API_ROOT}/files").json()
    )
    return render_template("index.html", clips=client.CLIPS, samples=client.SAMPLES, files=files)


@app.route("/service-worker.js")
def service_worker():
    return app.send_static_file("service-worker.js")


@app.route("/play/<uuid:uuid>")
def play(uuid: str):
    return client.play_clip(uuid)


@app.route("/queue/<uuid:uuid>")
def queue(uuid: str):
    return client.queue_clip(uuid)


app.wsgi_app = WhiteNoise(app.wsgi_app, root="sinusboard/server/static/")
