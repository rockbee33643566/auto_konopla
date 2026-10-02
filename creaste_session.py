from pyrogram import Client

import asyncio

from config import get_config, Config


async def create_bot(config: Config) -> Client:
    return Client(
        name=config.login,
        api_id=config.api_id,
        api_hash=config.api_hash,
        phone_number=config.phone
    )

async def load_dialogues(bot: Client):
    async for dialog in bot.get_dialogs():
        print(dialog.chat.id)  


async def main() -> None:
    config = get_config()
    bot = await create_bot(config)
    await bot.start()

    await load_dialogues(bot)
    
    await bot.stop()

if __name__ == "__main__":
    asyncio.run(main())