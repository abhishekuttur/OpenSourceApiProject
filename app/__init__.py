# import logging
# import os
# from flask import Flask
# import Flask
# # .\venv\Scripts\activate
# app = Flask(__name__)

# from app import routes

# # Ensure the log directory exists
# log_dir = 'logs'
# if not os.path.exists(log_dir):
#     os.makedirs(log_dir)

# # Configure logging
# log_file = os.path.join(log_dir, 'info.log')
# handler = logging.handlers.RotatingFileHandler(log_file, maxBytes=10000, backupCount=3)
# handler.setLevel(logging.INFO)
# handler.setFormatter(logging.Formatter(
#     '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
# ))
# app.logger.addHandler(handler)

# # Set the Flask logger level to INFO
# app.logger.setLevel(logging.INFO)