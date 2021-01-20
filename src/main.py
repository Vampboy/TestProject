

#pylint:disable=broad-except
import logging
from flask import Flask, request

logger = logging.getLogger(__name__)


class App:
    """class app """

    __instance = None

    def __init__(self):
        self._app = Flask(__name__)

    def app_name(self):
        """ app name """
        return self._app.name

    @property
    def app(self):
        """ self return """
        return self._app

    def run_server(self):
        """ runs the server """
        debug = True
        port = 5005
        self._app.run(host="0.0.0.0", debug=debug, port=port)

    @classmethod
    def get_instance(cls):
        """gets the instance """
        if App.__instance is None:
            App.__instance = cls()
        return App.__instance


app = App.get_instance().app
@app.route("/", methods=["GET"])
def check_running():
    """ GET '/' """
    logger.info('api alive')
    return 'I am running!'