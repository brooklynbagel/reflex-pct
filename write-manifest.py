from pathlib import Path

from rsconnect.bundle import Manifest
from rsconnect.models import AppModes

manifest = Manifest(app_mode=AppModes.STATIC)

for root, _, files in Path("frontend").walk():
    for file in files:
        if file == "manifest.json":
            continue
        manifest.add_file(root / file)

with open("frontend/manifest.json", "wt") as fp:
    fp.write(manifest.json)
