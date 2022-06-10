import logging
try:
    from user_config import *
except ModuleNotFoundError:
    pass

def set_value(user_var_name, default_value):
    if user_var_name in globals():
        user_value = globals()[user_var_name]
        if user_value is not None and (not isinstance(user_value, str) or user_value != ""):
            return user_value
    return default_value

BOT_TG_TOKEN = set_value("BOT_TG_TOKEN", "")
USERS_DB_PATH = set_value("USERS_DB_PATH", "./users.db")
DEBUG = set_value("DEBUG", False)

logger = logging.getLogger(__name__)
log_handler = logging.StreamHandler()
logger.setLevel(logging.INFO)
log_format = logging.Formatter('[%(asctime)s] %(levelname)s: %(message)s')
log_handler.setFormatter(log_format)
logger.addHandler(log_handler)

if DEBUG:
    logger.setLevel(logging.DEBUG)
