from eth.eth_client import EthClient
from better_automation.base import BaseAsyncSession


class OverWorld:

    def __init__(self, data):
        self.data = data
        self.eth_client = EthClient(data['private_key'])
        self.async_session = BaseAsyncSession(proxy=data['proxy'], verify=False)

    async def start_tasks(self):
        print('я тут')
        print(self.data)