from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from app.config import Config

# ==================================================
# Initialize extension instances
# ==================================================
db = SQLAlchemy()
jwt = JWTManager()

# More extensions here...
# ==================================================

def create_app():
    # Initialize app
    app = Flask(__name__)

    # App config
    app.config.from_object(Config)

    # ==================================================
    # Register extensions to app
    # ==================================================
    db.init_app(app)
    jwt.init_app(app)

    # More here...
    # ==================================================

    # ==================================================
    # Register resource blueprints
    # ==================================================

    # Auth
    from app.resources.auth.route import auth
    app.register_blueprint(auth)

    # Your custom resources here...
    # ==================================================

    return app