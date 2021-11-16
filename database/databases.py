import datetime
from typing import Optional
from pydantic import BaseModel
from beanie import Document, Indexed, init_beanie
import asyncio, motor


class Server(Document):
    server_id: int
    preferred_name: str
    roles: dict

    # IMAGE FILTERING
    image_filtering: bool
    image_filtering_channels: list
    image_filtering_roles: list
    image_filtering_nsfw: bool

    # TEXT FILTERING
    filter_long_text: bool
    filter_long_text_limit: int = 100

    # Misc
    enable_amptuator: bool
    disabled_modules: list

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class User(Document):
    name: str
    pronouns: str
    birthday: datetime.datetime
