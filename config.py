from dotenv import load_dotenv

import os
from dataclasses import dataclass

@dataclass
class Config:
    api_id: str
    api_hash: str
    phone: str
    login: str
    chat_id: int

def get_config() -> Config:
    load_dotenv()

    api_id = os.getenv("API_ID")
    api_hash = os.getenv("API_HASH")
    phone = os.getenv("PHONE")
    login = os.getenv("LOGIN")
    chat_id = os.getenv("CHAT_ID")


    if api_id is None:
            raise ValueError("API_ID не задана.")
    if api_hash is None:
        raise ValueError("API_HASH не задана.")
    if phone is None:
        raise ValueError("PHONE не задан.")
    if login is None:
        raise ValueError("LOGIN не задан.")
    if chat_id is None:
         raise ValueError("CHAT_ID не задан.")

    return Config(
         api_id=api_id,
         api_hash=api_hash,
         phone=phone,
         login=login,
         chat_id=chat_id
    )