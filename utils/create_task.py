import asyncio
import random

from data.config import logger
from db_api.models import Wallet
from db_api.database import get_accounts
from tasks.main import start_limited_task


async def get_start(semaphore):
    try:
        accounts: list[Wallet] = await get_accounts(faucet=True)
        if len(accounts) != 0:
            random.shuffle(accounts)
            logger.info(f'Всего задач: {len(accounts)}')
            tasks = []
            for account_data in accounts:
                task = asyncio.create_task(start_limited_task(semaphore, accounts, account_data))
                tasks.append(task)

            await asyncio.wait(tasks)
        else:
            msg = (f'Не удалось начать действие, возможная причина: нет подходящих аккаунтов для действия |'
                   f' не прошло 8 часов с прошлого клейма | вы не добавили аккаунты в базу данных.')
            logger.warning(msg)
    except Exception as e:
        pass
