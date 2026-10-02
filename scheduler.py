from apscheduler.schedulers.asyncio import AsyncIOScheduler 

import message

scheduler = AsyncIOScheduler()

scheduler.add_job(message.send_messages, "interval")