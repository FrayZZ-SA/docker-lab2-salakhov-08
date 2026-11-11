"""Учебный сервис по упаковке в Docker для лабораторной работы № 2."""
import os
import socket
from flask import Flask, jsonify

# Персональные поля варианта 08.
STUDENT = "Салахов Марат Ренатович"
GROUP = "БИСТ-23-ПО-2"
MARKER_DEFAULT = "netlab"
MARKER = os.environ.get("MARKER", MARKER_DEFAULT)
APP_PORT = int(os.environ.get("APP_PORT", "5008"))

app = Flask(__name__)
app.json.ensure_ascii = False

def version():
    try:
        with open("/app/VERSION", encoding="utf-8") as f:
            return f.read().strip() or "dev"
    except OSError:
        return "dev"

@app.get("/")
def index():
    return "probe: %s, хост %s\n" % (MARKER, socket.gethostname())

@app.get("/me")
def me():
    return jsonify(student=STUDENT, group=GROUP, marker=MARKER,
                   hostname=socket.gethostname(), version=version())

@app.get("/hostname")
def hostname():
    return jsonify(marker=MARKER, hostname=socket.gethostname())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=APP_PORT)
