"""Initialise the client for SinusBot operations."""

from typing import Final
from requests_html import HTMLSession


API_ROOT: Final[str] = "http://ix1game01.infernolan.co.uk:8087/api/v1/bot"

AUTHORIZATION: Final[str] = (
    "ugHwuXsiaSI6ImE5ZGQyZmM2LWQ4NWMtNDUyNS1iZWE0LTk4MGExYTA4NDQ0NSIsImIiOiI2OGYxZjg2Ny0zMmY3LTQzMWMtYW"
    "Y5Ny03NjA0ZWU0ZGNiZjMiLCJ1IjoiamVyYm9iIiwidCI6MTYxMzUyMTg3MCwicyI6IjQ3OGY1Y2M2ODkwNDk4NDA4ZGI5OWVl"
    "ZWQxYTQ4NDk1ZGVmMmJjNTI0MzM0NDliZWQzNjlkYTU5MTA3NTk5YTcifQ=="
).replace("\n", "")


session = HTMLSession()
session.headers["Authorization"] = f"Bearer {AUTHORIZATION}"

playlists = session.get(f"{API_ROOT}/files")
