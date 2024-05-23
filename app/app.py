from flask_cors import CORS
import logging
import os
from flask import Flask
from logging.handlers import RotatingFileHandler

def create_app():
    app = Flask(__name__)
    CORS(app)
    log_dir = 'logs'
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    log_file = os.path.join(log_dir, 'info.log')
    handler = RotatingFileHandler(log_file, maxBytes=10000, backupCount=3)
    handler.setLevel(logging.INFO)
    handler.setFormatter(logging.Formatter(
        "[%(asctime)s] {%(pathname)s:%(funcName)s %(lineno)d} %(levelname)s - %(message)s"
    ))
    
    error_file = os.path.join(log_dir, 'error.log')
    error_handler = RotatingFileHandler(error_file, maxBytes=10000, backupCount=3)
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    ))
    
    app.logger.addHandler(handler)
    app.logger.addHandler(error_handler)

    app.logger.setLevel(logging.INFO)

    @app.errorhandler(Exception)
    def log_exception(e):
        app.logger.error('Unhandled Exception: %s', e, exc_info=True)
        return "Internal Server Error", 500
    

    return app
