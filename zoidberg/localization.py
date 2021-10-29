import logging
from json import loads
from typing import Optional
log = logging.getLogger(__name__)

# TODO: Convert to store language in the database.
with open(f"./data/en_us.json", "r") as en_strings:
    en_us = loads(en_strings.read())


def get_string(string_name: str, localization_file: str = "en_us") -> str:
    """
    Returns string found in localization file.
    :param string_name: The name of the string you want.
    :param localization_file: File in which you want to load the string.
    :return: Requested string.
    """
    if localization_file == "en_us":
        res = en_us.get(string_name)
    else:
        with open(f"./data/{localization_file}.json", "r") as strings:
            res = loads(strings.read()).get(string_name)

    if res is None:
        return f'The string "{string_name}" could not be found in {localization_file}'
    return res
