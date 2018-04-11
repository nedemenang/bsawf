from flask import Flask

def create_app():
    """
    Create a Flask application using the app factory pattern.

    :return: Flask app
    
    """
    app = Flask(__name__, instance_relative_config=true)

    app.config.from_object('config.settings')
    app.config.from_pyfile('settings.py', silent=True)


    @app.route('/')
    def index():
        """
        Render a Hello world response

        :return: Flask response
        """

        return "Hello World!"

    return app
    