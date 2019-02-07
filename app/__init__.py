from flask import Flask, Blueprint


from .api.v1.views import version_one as v1




def start_app():
    app = Flask(__name__)

    app.register_blueprint(v1)

    return app