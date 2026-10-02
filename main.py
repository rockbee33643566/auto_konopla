from pyrogram import Client
from apscheduler.schedulers.asyncio import AsyncIOScheduler 

from config import get_config, Config
import message

import asyncio

async def create_bot(config: Config) -> Client:
    return Client(
        name=config.login,
        api_id=config.api_id,
        api_hash=config.api_hash,
        phone_number=config.phone
    )

async def init_scheduler(
        scheduler: AsyncIOScheduler, 
        bot: Client,
        config: Config
    ) -> None:
    scheduler.add_job(
        message.send_messages, 
        'interval', 
        args=(bot, config), 
        minutes=31
    )
    scheduler.start()
    
async def main() -> None:
    config = get_config()
    bot = await create_bot(config)
    scheduler = AsyncIOScheduler()
    await init_scheduler(
        scheduler=scheduler,
        bot=bot,
        config=config
    )

    await bot.start()

    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())