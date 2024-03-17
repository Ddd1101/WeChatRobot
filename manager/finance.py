from models.message import TransactionMsg
import requests


class Transaction:
    def __init__(self, msg: TransactionMsg) -> None:
        self.msg = msg

    def check_msg(self) -> dict:
        pass

    def post(self) -> None:
        params = self.check_msg()
        response = requests.post(url="", json=params)
