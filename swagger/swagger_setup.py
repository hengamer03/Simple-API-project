from flask_swagger_ui import get_swaggerui_blueprint
from flask import send_file, Blueprint
import os

SWAGGER_PATH = os.path.abspath("swagger/swagger.yaml")

def setup_swagger(app):
    @app.route('/swagger.yaml')
    def swagger_file():
        return send_file(SWAGGER_PATH, mimetype='text/yaml')

    # Serve the Swagger documentation
    SWAGGER_URL = '/swagger'  # URL for Swagger UI
    API_URL = '/swagger.yaml'  # Swagger specification URL

    swagger_ui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={'app_name': "Simple API"}
    )
    app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)
