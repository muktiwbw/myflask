import os
from dotenv import load_dotenv

# Search and load .env file
load_dotenv()

class Config:
    # ====================================================================
    # LIST OF ENVIRONMENT VARIABLES
    #   To add custom extensions, add their configs here:
    # ====================================================================

    # App secret key
    SECRET_KEY = os.getenv('SECRET_KEY')

    # SQL Alchemy
    SQLALCHEMY_DATABASE_URI = f"mysql://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_DATABASE')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # JWT
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')

    # Your custom extensions here...
    # ====================================================================

    # CONFIG_KEY = os.getenv('DOTENV_VARIABLE_NAME')