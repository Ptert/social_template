import traceback

import asyncio

from tasks.overworld import OverWorld
from data.config import logger, completed_tasks, tasks_lock


async def start_task(account_data, option):
    try:
        if option == 1:
            current_task = OverWorld(account_data)
            await current_task.start_tasks()
            await current_task.async_session.close()
    except TypeError:
        pass

    except Exception as error:
        logger.error(f'{account_data.token} | Неизвестная ошибка: {error}')
        print(traceback.print_exc())


async def start_limited_task(semaphore, accounts, account_data, option=1):
    try:
        async with semaphore:
            await start_task(account_data, option)

            async with tasks_lock:
                completed_tasks[0] += 1
                remaining_tasks = len(accounts) - completed_tasks[0]

            logger.info(f'Всего задач: {len(accounts)}. Осталось задач: {remaining_tasks}')
    except asyncio.CancelledError:
        pass
