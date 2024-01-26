import os
from dotenv import load_dotenv

load_dotenv()


# КОЛ-ВО ПОПЫТОК
NUMBER_OF_ATTEMPTS = int(os.getenv('NUMBER_OF_ATTEMPTS'))

# Одновременное кол-во асинк семафоров
ASYNC_SEMAPHORE = int(os.getenv('ASYNC_SEMAPHORE'))

# DAILY w token
W = os.getenv('W')

# ADD_TWITTER
ADD_TWITTER = bool(os.getenv('ADD_TWITTER'))

# КЛЮЧ от капчи
API_KEY_CAPMONSTER = os.getenv('API_KEY_CAPMONSTER')

# СВАП amount
SWAP_AMOUNT_FROM = float(os.getenv('SWAP_AMOUNT_FROM'))
SWAP_AMOUNT_TO = float(os.getenv('SWAP_AMOUNT_TO'))
