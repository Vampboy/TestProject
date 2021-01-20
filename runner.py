import logging


from src.common import logger_config
from src.main import App
from src.views.payment_process.route import payment_api

logger = logging.getLogger(__name__)


app = App.get_instance().app
app.register_blueprint(payment_api,url_prefix="/")
logger.info('App instanced added.')



if __name__ == '__main__':
    App.get_instance().run_server()