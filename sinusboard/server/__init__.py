"""Web dashboard for playing soundboard content."""

import json

from flask import Flask, request
from flask.templating import render_template
from whitenoise import WhiteNoise

from sinusboard import client

app = Flask(__name__)


@app.route("/")
def index():
    """Route for the dashboard template."""
    files = (
        {
            "name": file.get("title"),
            "uuid": file.get("uuid"),
            "length": client.get_duration(file.get("duration", 0)),
        }
        for file in reversed(client.session.get(f"{client.API_ROOT}/files").json())
    )
    return render_template(
        "index.html",
        clips=client.CLIPS,
        samples=client.SAMPLES,
        files=files,
        instances=sorted(
            client.get_instances()["instances"], key=lambda instance: instance["name"]
        ),
    )


@app.route("/service-worker.js")
def service_worker():
    return app.send_static_file("service-worker.js")


@app.route("/favicon.ico")
def favicon():
    return app.send_static_file("favicon.ico")


@app.route("/<uuid:instance_uuid>/play/<uuid:uuid>")
def play(instance_uuid: str, uuid: str):
    return client.play_clip(uuid, instance_uuid)


@app.route("/<uuid:instance_uuid>/queue/<uuid:uuid>")
def queue(instance_uuid: str, uuid: str):
    return client.queue_clip(uuid, instance_uuid)


@app.route("/upload/", methods=["POST"])
def upload():
    link = json.loads(request.data).get("link", "")
    return client.upload_clip(link)


@app.route("/delete/<uuid:uuid>")
def delete(uuid: str):
    return client.delete_clip(uuid)


@app.route("/instances/")
def instances():
    return client.get_instances()


app.wsgi_app = WhiteNoise(app.wsgi_app, root="sinusboard/server/static/")
