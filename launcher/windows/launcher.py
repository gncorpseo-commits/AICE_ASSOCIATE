import os
import shutil
import signal
import subprocess
import sys
import tempfile
import time
import urllib.request
import webbrowser
import zipfile

ZIP_URL = "https://github.com/gncorpseo-commits/AICE_ASSOCIATE/archive/refs/heads/main.zip"
TEMP_DIR = os.path.join(tempfile.gettempdir(), "AICE_ASSOCIATE")
ZIP_PATH = os.path.join(tempfile.gettempdir(), "AICE_ASSOCIATE.zip")
EXTRACTED_NAME = "AICE_ASSOCIATE-main"
FRONTEND_PORT = "8000"
BACKEND_PORT = "8001"
FRONTEND_URL = f"http://localhost:{FRONTEND_PORT}/practice/df_training.html"


def log(message: str) -> None:
    print(message, flush=True)


def download_zip() -> None:
    log("Downloading project zip...")
    urllib.request.urlretrieve(ZIP_URL, ZIP_PATH)


def extract_zip() -> None:
    log("Extracting project zip...")
    if os.path.exists(TEMP_DIR):
        shutil.rmtree(TEMP_DIR, ignore_errors=True)
    with zipfile.ZipFile(ZIP_PATH, "r") as zip_ref:
        zip_ref.extractall(tempfile.gettempdir())
    extracted = os.path.join(tempfile.gettempdir(), EXTRACTED_NAME)
    if os.path.exists(TEMP_DIR):
        shutil.rmtree(TEMP_DIR, ignore_errors=True)
    os.rename(extracted, TEMP_DIR)


def find_py_launcher() -> list[str]:
    return ["py", "-3.11"]


def install_requirements(py_cmd: list[str]) -> None:
    log("Installing server requirements...")
    requirements = os.path.join(TEMP_DIR, "server", "requirements.txt")
    subprocess.check_call(py_cmd + ["-m", "pip", "install", "-r", requirements], cwd=TEMP_DIR)


def start_servers(py_cmd: list[str]) -> tuple[subprocess.Popen, subprocess.Popen]:
    log("Starting frontend server...")
    frontend = subprocess.Popen(
        py_cmd + ["-m", "http.server", FRONTEND_PORT],
        cwd=TEMP_DIR,
        creationflags=subprocess.CREATE_NEW_PROCESS_GROUP,
    )
    log("Starting FastAPI server...")
    backend = subprocess.Popen(
        py_cmd
        + [
            "-m",
            "uvicorn",
            "server.app:app",
            "--host",
            "0.0.0.0",
            "--port",
            BACKEND_PORT,
        ],
        cwd=TEMP_DIR,
        creationflags=subprocess.CREATE_NEW_PROCESS_GROUP,
    )
    return frontend, backend


def open_browser() -> None:
    time.sleep(1.2)
    webbrowser.open(FRONTEND_URL)


def main() -> int:
    try:
        download_zip()
        extract_zip()
        py_cmd = find_py_launcher()
        install_requirements(py_cmd)
        frontend, backend = start_servers(py_cmd)
        open_browser()

        log("Servers are running. Close this window to stop.")
        backend.wait()
        return 0
    except KeyboardInterrupt:
        log("Stopping servers...")
        return 0
    except Exception as exc:  # noqa: BLE001
        log(f"Launcher error: {exc}")
        return 1
    finally:
        for proc in [p for p in locals().values() if isinstance(p, subprocess.Popen)]:
            try:
                proc.send_signal(signal.CTRL_BREAK_EVENT)
                time.sleep(0.5)
                proc.kill()
            except Exception:
                pass


if __name__ == "__main__":
    sys.exit(main())
