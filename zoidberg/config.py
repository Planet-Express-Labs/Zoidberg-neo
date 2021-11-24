# Copyright 2021 Planet Express Labs
# All rights reserved.
# The only reason for taking full copyright is because of a few bad actors.
# As long as you are using my code in good faith, we will probably not have an issue with it.

import codecs
import configparser
import logging
import os
import ast
from pathlib import Path
import openai

log = logging.getLogger(__name__)
config_path = p = Path('config/config.ini')

if not os.path.exists(config_path):
    print("Cannot find config file in /config/config.ini! Trying to load from environment variables... ")
    # TODO: make less bad
    LL_NODES = ast.literal_eval(os.getenv("zoidberg_full_nodes"))
    BOT_TOKEN = os.getenv("FRONTMAN_TOKEN")

else:
    config_file = config_path
    config = configparser.ConfigParser()
    config.read_file(codecs.open(config_file, "r+", "utf-8"))

    def read_config(file=config_file):
        config.read_file(codecs.open(file, "r+", "utf-8"))

    BOT_TOKEN = config.get("Bot", "bot_token")
    TEST_GUILDS = config.get("Bot", "testing_guilds").split(",")
    SUBSCRIPTION_KEY = config.get("AI", "azure_cm_sub_key")
    CONTENT_MODERATOR_ENDPOINT = config.get("AI", "azure_cm_endpoint")
    LL_NODES = ast.literal_eval(config.get("Bot", "lavalink_nodes"))

    DB_LOCALHOST = config.get("DB", "use_localhost")
    CONNURL = config.get("DB", "connection_url")
    DISABLED_COGS = config.get("Bot", "disabled_cogs").split(", ")

    HASTE_URL = config.get("API", "hastebin_url")

    openai.api_key = config.get("AI", "openai_api_key")
