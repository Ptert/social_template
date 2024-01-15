import itertools

import asyncio

from utils.create_files import create_files
from utils.user_menu import get_action
from utils.import_info import get_accounts_info
from utils.adjust_policy import set_windows_event_loop_policy
from data.config import TWITTER_TOKENS, PROXYS, PRIVATE_KEYS, logger
from settings.settings import ASYNC_SEMAPHORE
from tasks.main import start_limited_task


async def main():
    twitter_tokens: list[str] = get_accounts_info(TWITTER_TOKENS)
    proxies: list[str] = get_accounts_info(PROXYS)
    private_keys: list[str] = get_accounts_info(PRIVATE_KEYS)

    cycled_proxies_list = itertools.cycle(proxies) if proxies else None

    logger.info(f'Загружено в twitter_tokens.txt {len(twitter_tokens)} аккаунтов \n'
                f'\t\t\t\t\t\t\tЗагружено в proxys.txt {len(proxies)} прокси \n'
                f'\t\t\t\t\t\t\tЗагружено в private_keys.txt {len(private_keys)} приватных ключей \n')

    formatted_data: list = [{
            'twitter_token': twitter_tokens.pop(0) if twitter_tokens else None,
            'proxy': next(cycled_proxies_list) if cycled_proxies_list else None,
            'private_key': private_key
        } for private_key in private_keys
    ]

    user_choice = get_action()

    semaphore = asyncio.Semaphore(ASYNC_SEMAPHORE)

    if user_choice == '   1) Импорт в базу данных':

        pass
        #await ImportToDB.add_account_to_db(accounts_data=formatted_data)

    elif user_choice == '   2) Войти с помощью приватного ключа':

        tasks = []
        for account_data in formatted_data:
            task = asyncio.create_task(start_limited_task(semaphore, formatted_data, account_data))
            tasks.append(task)

        await asyncio.wait(tasks)


if __name__ == "__main__":
    create_files()
    set_windows_event_loop_policy()
    asyncio.run(main())
