from flask import Flask
import sys
from pathlib import Path
import os

sys.path.insert(0, str(Path(__file__).parent.parent))
from src.controller import controller

app = Flask(__name__)

app.register_blueprint(controller)

if __name__ == "__main__":
    app.run(debug=True)