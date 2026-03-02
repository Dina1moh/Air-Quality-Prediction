# main.py
from flask import Flask
from src.controller import routes
import os

template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "src", "templates")
app = Flask(__name__, template_folder=template_dir)

app.register_blueprint(routes)

if __name__ == "__main__":
    app.run(debug=True)