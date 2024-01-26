import itertools

import asyncio

from utils.create_files import create_files
from utils.user_menu import get_action
from utils.import_info import get_accounts_info
from utils.adjust_policy import set_windows_event_loop_policy
from data.config import TWITTER_TOKENS, PROXYS, PRIVATE_KEYS, logger, EMAIL_DATA
from settings.settings import ASYNC_SEMAPHORE
from db_api.database import initialize_db
from db_api.start_import import ImportToDB
from utils.create_task import (
    get_start
)


def main():
    twitter_tokens: list[str] = get_accounts_info(TWITTER_TOKENS)
    proxies: list[str] = get_accounts_info(PROXYS)
    private_keys: list[str] = get_accounts_info(PRIVATE_KEYS)
    email_data: list[str] = get_accounts_info(EMAIL_DATA)

    cycled_proxies_list = itertools.cycle(proxies) if proxies else None

    logger.info(f'Загружено в twitter_tokens.txt {len(twitter_tokens)} аккаунтов \n'
                f'\t\t\t\t\t\t\tЗагружено в proxys.txt {len(proxies)} прокси \n'
                f'\t\t\t\t\t\t\tЗагружено в private_keys.txt {len(private_keys)} приватных ключей \n'
                f'\t\t\t\t\t\t\tЗагружено в email_data.txt {len(email_data)} почт \n'
                )

    formatted_data: list = [{
            'twitter_token': twitter_tokens.pop(0) if twitter_tokens else None,
            'proxy': next(cycled_proxies_list) if cycled_proxies_list else None,
            'private_key': private_key,
            'email_data': email_data.pop(0) if email_data else None,
        } for private_key in private_keys
    ]

    user_choice = get_action()

    semaphore = asyncio.Semaphore(ASYNC_SEMAPHORE)

    if user_choice == '   1) Импорт в базу данных':

        asyncio.run(ImportToDB.add_account_to_db(accounts_data=formatted_data))

    elif user_choice == '   2) Регистрация на galxe и привязка почты/твиттера':

        asyncio.run(get_start(semaphore))

    else:
        logger.error('ВЫБРАНО НЕВЕРНОЕ ДЕЙСТВИЕ')


if __name__ == "__main__":
    try:
        asyncio.run(initialize_db())
        create_files()
        set_windows_event_loop_policy()
        main()
    except TypeError:
        logger.info('Программа завершена')