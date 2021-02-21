"""Initialise the client for SinusBot operations."""

from json import JSONDecodeError
from typing import Final, Optional

from requests import Session

session = Session()

AUTHORIZATION: Final[dict[str, str]] = {
    "botId": "68f1f867-32f7-431c-af97-7604ee4dcbf3",
    "password": "Meme",
    "username": "jerbob",
}
API_ROOT: Final[str] = "http://ix1game01.infernolan.co.uk:8087/api/v1/bot"
PLAY: Final[str] = f"{API_ROOT}/i/82faa775-298d-4c9f-9827-4dd8b91399b0/play/byId/{{uuid}}"
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
    {"name": "AA", "uuid": "004221e9-5c8c-4282-8565-cdf3b5aec683"},
    {"name": "EE", "uuid": "6e0a434f-0ffb-424a-bb6f-a233de59b782"},
    {"name": "OO", "uuid": "c4fe3674-2698-4793-93dc-3ad89cba5dbc"},
    {"name": "Audio Jungle", "uuid": "a30c69e9-6f74-4c06-8a9d-a08fe8a8f472"},
]

session.headers["Authorization"] = f"Bearer {TOKEN}"


def play_clip(uuid: str) -> dict:
    """Play the specified clip using SinusBot."""
    response = session.post(PLAY.format(uuid=uuid))
    try:
        return response.json()
    except JSONDecodeError:
        print(f"[!] Invalid response from SinusBot:")
        print(response.content.decode())
        return {}
