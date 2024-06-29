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
