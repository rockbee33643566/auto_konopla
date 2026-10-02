from pyrogram import Client

import asyncio

from config import Config

TEXTS = [
    "/collect@konoplyankabot",
    "/smoke@konoplyankabot",
    "/sell@konoplyankabot all"
]

async def send_messages(bot: Client, config: Config) -> None: 
    for mes in TEXTS:
        await bot.send_message(chat_id=config.chat_id, text=mes)
        await asyncio.sleep(1)