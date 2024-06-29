export API_URL := "https://neptune.brooklynbagel.xyz/pct/content/bef86a72-a955-4760-b302-abc0b415e217"
export FRONTEND_PATH := "/pct/content/44ecad29-5645-4887-a94b-0e2b52789024"

prepare-backend:
  cd intro_reflex && ../.venv/bin/reflex export --backend-only --zip-dest-dir ..
  rm -rf backend
  unzip -d backend backend.zip
  cp requirements.txt backend/.
  rsconnect write-manifest fastapi --entrypoint intro_reflex.intro_reflex:app.api backend

prepare-frontend:
  cd intro_reflex && ../.venv/bin/reflex export --frontend-only --zip-dest-dir ..
  rm -rf frontend
  unzip -d frontend frontend.zip
  .venv/bin/python write-manifest.py
