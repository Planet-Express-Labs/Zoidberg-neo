import datetime
from typing import Optional
from pydantic import BaseModel
from beanie import Document, Indexed, init_beanie
import pymongo


class Server(Document):
    """Stores information specific to a discord guild/server. 
    """
    server_id: int
    preferred_name: str
    roles: dict
    premium: int

    ### Moderation

    # Image Filtering
    image_filtering: bool
    image_filtering_channels: list
    image_filtering_channels_blocklist: bool
    image_filtering_roles: list
    image_filtering_roles_blocklist: bool
    image_filtering_nsfw: bool

    # Text Filtering
    filter_long_text: bool
    filter_long_text_limit: int = 100

    # Server sync

    ### Misc
    enable_amptuator: bool
    disabled_modules: list


class User(Document):
    """
    Main document for storing information specific to users. 
    """
    id: str
    name: str
    pronouns: str
    gender: str
    birthday: datetime.datetime
    hidden_users: list
    premium: int


class Ban(Document):
    """
    Document for storing banned users. 
    """
