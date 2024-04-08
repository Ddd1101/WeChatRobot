# from models.message import TransactionMsg
import requests
from wcferry import Wcf, WxMsg

user_id = {"wxid_nn3m922bd9j722": {"nickname": "#DFG", "name": "侯国鑫"}}


class Transaction:
    # def __init__(self, msg: TransactionMsg) -> None:
    #     self.msg = msg
    def __init__(self) -> None:
        self.TAG = "finance_Transaction"

    def check_msg(self) -> dict:
        pass

    def post(self) -> None:
        params = {
            "data": {
                "create_time": "",
                "company": "万盈",
                "payer": "侯国鑫",
                "payee": "侯国金",
                "amount": 50000,
                "issue": "返款",
                "remark": "",
            }
        }
        response = requests.post(
            url="http://127.0.0.1:8000/wxbot/addTransaction", json=params
        )

        print(response)

    def processMsg(self, msgContentList, msg: WxMsg):
        print(self.TAG, msgContentList)
        if msgContentList[0] == "返款":
            print(user_id[msg.sender]["name"])
            self.refund(msgContentList, msg)

    def refund(self, msgContentList, msg: WxMsg):
        # 金额
        amount = float(msgContentList[1])
        # 付款方
        payer = user_id[msg.sender]["name"]
        # 收款方
        payee = msgContentList[2]
        if payee == "金" or payee == "国金" or payee == "侯国金":
            payee == "侯国金"
        # 备注
        remark = ""
        if len(msgContentList) >= 4:
            remark = msgContentList[3]
        # 拼接请求参数
        params = {
            "data": {
                "create_time": "",
                "company": "万盈",
                "payer": payer,
                "payee": payee,
                "amount": float(msgContentList[1]),
                "issue": "返款",
                "remark": remark,
            }
        }

        print(params)


if __name__ == "__main__":
    transaction = Transaction()
    transaction.post()
