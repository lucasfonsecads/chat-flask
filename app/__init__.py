from flask import Flask
from flask_socketio import SocketIO
from flask_bootstrap import Bootstrap

socketio = SocketIO()


def create_app(debug=False):
    #Aplication Create
    app = Flask(__name__)
    boostrap = Bootstrap(app)
    app.debug = debug
    app.config['SECRET_KEY'] = '!@#938201-Ddashduaena_!984#'

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    socketio.init_app(app)
    return app
