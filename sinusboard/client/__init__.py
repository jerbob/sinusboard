"""Initialise the client for SinusBot operations."""

import itertools
from functools import lru_cache
from json import JSONDecodeError
from typing import Final, Optional

from requests import Session

session = Session()

AUTHORIZATION: Final[dict[str, str]] = {
    "botId": "68f1f867-32f7-431c-af97-7604ee4dcbf3",
    "password": "Meme",
    "username": "jerbob",
}

INSTANCE: Final[str] = "82faa775-298d-4c9f-9827-4dd8b91399b0"
API_ROOT: Final[str] = f"http://ix1game01.infernolan.co.uk:8087/api/v1/bot"

PLAY_URL: Final[str] = f"{API_ROOT}/i/{INSTANCE}/play/byId/{{uuid}}"
QUEUE_URL: Final[str] = f"{API_ROOT}/i/{INSTANCE}/queue/append/{{uuid}}"
TOKEN: Final[str] = session.post(f"{API_ROOT}/login", json=AUTHORIZATION).json().get("token")


CLIPS: Final[list[dict[str, str]]] = [
    {"name": "Certified Hood Classic", "uuid": "cdd5d14e-326e-4ede-ab77-a59483b06db9"},
    {"name": "See ya man", "uuid": "655907d2-c9b8-4eec-bd40-fdbf670a2921"},
    {"name": "Among Drip", "uuid": "02c48548-a728-4e4d-9288-52b1a72c0e57"},
    {"name": "Vine Thud", "uuid": "c979bcfb-4be2-4378-b03b-351261fe9ef0"},
    {"name": "Ring ding ding", "uuid": "b00bdfd6-b258-433f-9897-9357b5bb2aab"},
    {"name": "Dream", "uuid": "f84cffbe-5cfc-4ddf-b8d2-e6e4c3ab6c50"},
    {"name": "Ultra Instinct", "uuid": "434d85ad-25b9-4070-b4c6-0582dccefbaa"},
]

SAMPLES: Final[list[dict[str, str]]] = [
    {"name": "AA", "uuid": "3ec3646f-49fa-4b25-9292-3617c6ffdc03"},
    {"name": "EE", "uuid": "5b2fea02-e64d-4f1f-998b-8dae98602bb5"},
    {"name": "OO", "uuid": "8df22f9c-a0f1-45a2-b396-3849da724508"},
    {"name": "Audio Jungle", "uuid": "a30c69e9-6f74-4c06-8a9d-a08fe8a8f472"},
]

session.headers["Authorization"] = f"Bearer {TOKEN}"


@lru_cache
def get_clip(uuid: str) -> dict[str, str]:
    """Lookup the clip object, given a UUID."""
    try:
        return next(clip for clip in itertools.chain(CLIPS, SAMPLES) if clip["uuid"] == str(uuid))
    except StopIteration:
        return {"uuid": uuid}


def play_clip(uuid: str) -> dict:
    """Play the specified clip using SinusBot."""
    response = session.post(PLAY_URL.format(uuid=uuid))
    try:
        return response.json()
    except JSONDecodeError:
        print(f"[!] Invalid response from SinusBot:")
        print(response.content.decode())
        return {}


def queue_clip(uuid: str) -> dict:
    """Append the specified clip to the SinusBot queue."""
    response = session.post(QUEUE_URL.format(uuid=uuid))
    try:
        return response.json()
    except JSONDecodeError:
        print(f"[!] Invalid response from SinusBot:")
        print(response.content.decode())
        return {}
