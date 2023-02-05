import logging
import os

import telegram.ext as tg

# enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

LOGGER = logging.getLogger(__name__)


ENV = bool(os.environ.get("ENV", False))

if ENV:
    API_KEY = os.environ.get("API_KEY", None)
    try:
        OWNER_ID = int(os.environ.get("OWNER_ID", 0))
    except ValueError:
        raise Exception("Your OWNER_ID env variable is not a valid integer.")

    try:
        FROM_CHATS = set(int(x) for x in os.environ.get("FROM_CHATS", "").split())
    except ValueError:
        raise Exception("Your FROM_CHATS list does not contain valid integers.")

    try:
        TO_CHATS = set(int(x) for x in os.environ.get("TO_CHATS", "").split())
    except ValueError:
        raise Exception("Your TO_CHATS list does not contain valid integers.")

    try:
        FROM_CHATS_1 = set(int(x) for x in os.environ.get("FROM_CHATS_1", "0").split())
    except ValueError:
        raise Exception("Your FROM_CHATS_1 list does not contain valid integers.")

    try:
        TO_CHATS_1 = set(int(x) for x in os.environ.get("TO_CHATS_1", "0").split())
    except ValueError:
        raise Exception("Your TO_CHATS_1 list does not contain valid integers.")

    try:
        FROM_CHATS_2 = set(int(x) for x in os.environ.get("FROM_CHATS_2", "0").split())
    except ValueError:
        raise Exception("Your FROM_CHATS_2 list does not contain valid integers.")

    try:
        TO_CHATS_2 = set(int(x) for x in os.environ.get("TO_CHATS_2", "0").split())
    except ValueError:
        raise Exception("Your TO_CHATS_2 list does not contain valid integers.")

    try:
        FROM_CHATS_3 = set(int(x) for x in os.environ.get("FROM_CHATS_3", "0").split())
    except ValueError:
        raise Exception("Your FROM_CHATS_3 list does not contain valid integers.")

    try:
        TO_CHATS_3 = set(int(x) for x in os.environ.get("TO_CHATS_3", "0").split())
    except ValueError:
        raise Exception("Your TO_CHATS_3 list does not contain valid integers.")

    try:
        FROM_CHATS_4 = set(int(x) for x in os.environ.get("FROM_CHATS_4", "0").split())
    except ValueError:
        raise Exception("Your FROM_CHATS_4 list does not contain valid integers.")

    try:
        TO_CHATS_4 = set(int(x) for x in os.environ.get("TO_CHATS_4", "0").split())
    except ValueError:
        raise Exception("Your TO_CHATS_4 list does not contain valid integers.")

    try:
        FROM_CHATS_5 = set(int(x) for x in os.environ.get("FROM_CHATS_5", "0").split())
    except ValueError:
        raise Exception("Your FROM_CHATS_5 list does not contain valid integers.")

    try:
        TO_CHATS_5 = set(int(x) for x in os.environ.get("TO_CHATS_5", "0").split())
    except ValueError:
        raise Exception("Your TO_CHATS_5 list does not contain valid integers.")


    REMOVE_TAG = bool(os.environ.get("REMOVE_TAG", False))
    WEBHOOK = bool(os.environ.get("WEBHOOK", False))
    IP_ADDRESS = os.environ.get("IP_ADDRESS", "0.0.0.0")
    URL = os.environ.get("URL", "")  # Does not contain token
    PORT = int(os.environ.get("PORT", 5000))
    CERT_PATH = os.environ.get("CERT_PATH")

    WORKERS = int(os.environ.get("WORKERS", 4))

else:
    from forwarder.config import Development as Config

    API_KEY = Config.API_KEY
    try:
        OWNER_ID = int(Config.OWNER_ID)
    except ValueError:
        raise Exception("Your OWNER_ID variable is not a valid integer.")

    try:
        FROM_CHATS = set(int(x) for x in Config.FROM_CHATS)
    except ValueError:
        raise Exception("Your FROM_CHATS list does not contain valid integers.")

    try:
        TO_CHATS = set(int(x) for x in Config.TO_CHATS or [])
    except ValueError:
        raise Exception("Your TO_CHATS list does not contain valid integers.")

    try:
        FROM_CHATS_1 = set(int(x) for x in Config.FROM_CHATS_1)
    except ValueError:
        raise Exception("Your FROM_CHATS_1 list does not contain valid integers.")

    try:
        TO_CHATS_1 = set(int(x) for x in Config.TO_CHATS_1 or [])
    except ValueError:
        raise Exception("Your TO_CHATS_1 list does not contain valid integers.")

    try:
        FROM_CHATS_2 = set(int(x) for x in Config.FROM_CHATS_2)
    except ValueError:
        raise Exception("Your FROM_CHATS_2 list does not contain valid integers.")

    try:
        TO_CHATS_2 = set(int(x) for x in Config.TO_CHATS_2 or [])
    except ValueError:
        raise Exception("Your TO_CHATS_2 list does not contain valid integers.")

    try:
        FROM_CHATS_3 = set(int(x) for x in Config.FROM_CHATS_3)
    except ValueError:
        raise Exception("Your FROM_CHATS_3 list does not contain valid integers.")

    try:
        TO_CHATS_3 = set(int(x) for x in Config.TO_CHATS_3 or [])
    except ValueError:
        raise Exception("Your TO_CHATS_3 list does not contain valid integers.")

    try:
        FROM_CHATS_4 = set(int(x) for x in Config.FROM_CHATS_4)
    except ValueError:
        raise Exception("Your FROM_CHATS_4 list does not contain valid integers.")

    try:
        TO_CHATS_4 = set(int(x) for x in Config.TO_CHATS_4 or [])
    except ValueError:
        raise Exception("Your TO_CHATS_4 list does not contain valid integers.")

    try:
        FROM_CHATS_5 = set(int(x) for x in Config.FROM_CHATS_5)
    except ValueError:
        raise Exception("Your FROM_CHATS_5 list does not contain valid integers.")

    try:
        TO_CHATS_5 = set(int(x) for x in Config.TO_CHATS_5 or [])
    except ValueError:
        raise Exception("Your TO_CHATS_5 list does not contain valid integers.")


    REMOVE_TAG = Config.REMOVE_TAG
    WEBHOOK = Config.WEBHOOK
    IP_ADDRESS = Config.IP_ADDRESS
    URL = Config.URL
    PORT = Config.PORT
    CERT_PATH = Config.CERT_PATH

    WORKERS = Config.WORKERS


updater = tg.Updater(API_KEY, workers=WORKERS)

dispatcher = updater.dispatcher

FROM_CHATS = list(FROM_CHATS)
TO_CHATS = list(TO_CHATS)
FROM_CHATS_1 = list(FROM_CHATS_1)
TO_CHATS_1 = list(TO_CHATS_1)
FROM_CHATS_2 = list(FROM_CHATS_2)
TO_CHATS_2 = list(TO_CHATS_2)
FROM_CHATS_3 = list(FROM_CHATS_3)
TO_CHATS_3 = list(TO_CHATS_3)
FROM_CHATS_4 = list(FROM_CHATS_4)
TO_CHATS_4 = list(TO_CHATS_4)
FROM_CHATS_5 = list(FROM_CHATS_5)
TO_CHATS_5 = list(TO_CHATS_5)
