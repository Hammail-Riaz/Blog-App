from flask import Flask, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv
import os

load_dotenv()

bcrypt = Bcrypt()
db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__, template_folder="Templates", static_folder="Statics")
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    
    from routes import register_routes
    from models import Users_Data, Notes
    
    @login_manager.user_loader
    def load_user(uid):
        return Users_Data.query.get(uid)
    @login_manager.unauthorized_handler
    def unauthorized_callback():
        flash("You are unauthorized. First login to continue!", "danger")
        return redirect(url_for('login'))
    
    register_routes(app)
    
    migrate = Migrate(app, db)
    
    return app
    