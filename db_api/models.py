import datetime

from data.models import AutoRepr
from sqlalchemy import (Column, Integer, Text, Boolean, DateTime)
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class Wallet(Base, AutoRepr):
    __tablename__ = 'accounts'

    id = Column(Integer, primary_key=True)

    twitter_username = Column(Text)
    token = Column(Text)
    private_key = Column(Text, unique=True)
    address = Column(Text)
    proxy = Column(Text)
    email_data = Column(Text)

    twitter_account_status = Column(Text)
    user_agent = Column(Text)
    platform = Column(Text)

    galxe_register = Column(Boolean)

    def __init__(
            self,
            token: str,
            private_key: str,
            address: str,
            proxy: str,
            user_agent: str,
            platform: str,
            email: str = None,
    ) -> None:

        self.twitter_username = None
        self.token = token
        self.private_key = private_key
        self.address = address
        self.proxy = proxy
        self.email_data = email

        self.twitter_account_status = "OK"
        self.user_agent = user_agent
        self.platform = platform

        self.galxe_register = False
