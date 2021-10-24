# Copyright 2021 Planet Express Labs
# All rights reserved.
# The only reason for taking full copyright is because of a few bad actors.
# As long as you are using my code in good faith, we will probably not have an issue with it.

import codecs
import configparser
import logging
import os

log = logging.getLogger(__name__)

if not os.path.exists(os.getcwd() + "\\config\\config.ini"):
    print("Cannot find config file in /config/config.ini! Trying to load from environment variables... ")

    BOT_TOKEN = os.getenv("FRONTMAN_TOKEN")

else:
    config_file = os.getcwd() + "\\config\\config.ini"
    config = configparser.ConfigParser()
    config.read_file(codecs.open(config_file, "r+", "utf-8"))


    def read_config(file=config_file):
        config.read_file(codecs.open(file, "r+", "utf-8"))

    BOT_TOKEN = config.get("Bot", "bot_token")
    TEST_GUILDS = config.get("Bot", "testing_guilds").split(",")

