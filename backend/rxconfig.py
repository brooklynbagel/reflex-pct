import os
from urllib.parse import urljoin

import reflex as rx

api_url = os.getenv("API_URL", "http://localhost:8000")

if os.getenv("RSTUDIO_PRODUCT") == "CONNECT":
    api_url = urljoin(
        os.environ["CONNECT_SERVER"], f"content/{os.environ["CONNECT_CONTENT_GUID"]}"
    )

print(f"{api_url=}")

config = rx.Config(
    app_name="intro_reflex",
    api_url=api_url,
)
