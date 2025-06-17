import os
from flask import Flask
from sqlalchemy import create_engine
from config import DB_URI

engine = create_engine(DB_URI)

def create_app():
    app = Flask(__name__, template_folder=os.path.abspath("templates"), static_folder=os.path.abspath("static"))

    from app.views.employee_view import employee_bp
    app.register_blueprint(employee_bp)

    return app