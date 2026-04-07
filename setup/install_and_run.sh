#!/usr/bin/env bash
set -e

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
echo "Using project root: $ROOT_DIR"

python --version

echo "Installing server requirements..."
python -m pip install -r "$ROOT_DIR/server/requirements.txt"

echo "Starting frontend server (http://localhost:8000)..."
(
  cd "$ROOT_DIR"
  python -m http.server 8000
) &

echo "Starting FastAPI server (http://localhost:8001)..."
python -m uvicorn server.app:app --host 0.0.0.0 --port 8001

if command -v open >/dev/null 2>&1; then
  open "http://localhost:8000/index.html"
elif command -v xdg-open >/dev/null 2>&1; then
  xdg-open "http://localhost:8000/index.html"
fi
