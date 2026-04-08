#!/usr/bin/env bash
set -e

ZIP_URL="https://github.com/gncorpseo-commits/AICE_ASSOCIATE/archive/refs/heads/main.zip"
TMP_DIR="${TMPDIR:-/tmp}/AICE_ASSOCIATE"
ZIP_PATH="${TMPDIR:-/tmp}/AICE_ASSOCIATE.zip"
EXTRACTED_NAME="AICE_ASSOCIATE-main"

echo "Downloading project zip..."
curl -L "$ZIP_URL" -o "$ZIP_PATH"

echo "Extracting project zip..."
rm -rf "$TMP_DIR"
rm -rf "${TMPDIR:-/tmp}/${EXTRACTED_NAME}"
unzip -q "$ZIP_PATH" -d "${TMPDIR:-/tmp}"
mv "${TMPDIR:-/tmp}/${EXTRACTED_NAME}" "$TMP_DIR"

echo "Installing server requirements..."
python3.11 -m pip install -r "$TMP_DIR/server/requirements.txt"

echo "Starting frontend server..."
cd "$TMP_DIR"
python3.11 -m http.server 8000 &
FRONT_PID=$!

echo "Starting FastAPI server..."
python3.11 -m uvicorn server.app:app --host 0.0.0.0 --port 8001 &
BACK_PID=$!

sleep 1
if command -v open >/dev/null 2>&1; then
  open "http://localhost:8000/practice/df_training.html"
elif command -v xdg-open >/dev/null 2>&1; then
  xdg-open "http://localhost:8000/practice/df_training.html"
else
  echo "Open http://localhost:8000/practice/df_training.html in your browser."
fi

echo "Servers are running. Press Ctrl+C to stop."
wait $BACK_PID

cleanup() {
  kill "$FRONT_PID" "$BACK_PID" >/dev/null 2>&1 || true
}
trap cleanup EXIT
