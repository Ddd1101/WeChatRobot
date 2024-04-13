# from models.message import TransactionMsg
import requests
from wcferry import Wcf, WxMsg

user_id = {"wxid_nn3m922bd9j722": {"nickname": "#DFG", "name": "侯国鑫"}}


class Transaction:
    def __init__(self) -> None:
        self.TAG = "finance_Transaction"

    def checkMsg(self) -> dict:
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

        print(response.json())

    def processMsg(self, msgContentList, msg: WxMsg):
        print(self.TAG, msgContentList)
        if (
            msgContentList[0] == "提现"
            or msgContentList[0] == "退款"
            or msgContentList[0] == "支出"
        ):
            return self.nomalOrder(msgContentList, msg)
        elif msgContentList[0] == "自由提单":
            self.freeOrder(msgContentList, msg)

    # 常规工单：事项 + （时间） + 金额 + 收款方 + 备注  出款人默认为发消息的人
    def nomalOrder(self, msgContentList, msg: WxMsg):
        # 事项
        issue = msgContentList[0]
        # 金额
        amount = float(msgContentList[1])
        # 付款方
        payer = user_id[msg.sender]["name"]
        # 收款方
        payee = msgContentList[2]
        if payee == "金" or payee == "国金" or payee == "侯国金":
            payee = "侯国金"
        elif payee == "鑫" or payee == "国鑫" or payee == "侯国鑫":
            payee = "侯国鑫"
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
                "amount": amount,
                "issue": issue,
                "remark": remark,
            }
        }

        response = requests.post(
            url="http://127.0.0.1:8000/wxbot/addTransaction", json=params
        )

        res = response.json()

        return res

    # 自由工单：“自由工单” + 事项 +（时间）+ 金额 + 出款方 + 收款方 + 备注  出款人需要填写
    def freeOrder(self, msgContentList, msg: WxMsg):
        # 事项
        issue = msgContentList[1]
        # 金额
        amount = float(msgContentList[2])
        # 付款方
        payer = msgContentList[3]
        # 收款方
        payee = msgContentList[4]
        if payee == "金" or payee == "国金" or payee == "侯国金":
            payee == "侯国金"
        elif payee == "鑫" or payee == "国鑫" or payee == "侯国鑫":
            payee == "侯国鑫"
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
                "amount": amount,
                "issue": issue,
                "remark": remark,
            }
        }

        print(params)
        response = requests.post(
            url="http://127.0.0.1:8000/wxbot/addTransaction", json=params
        )


if __name__ == "__main__":
    transaction = Transaction()
    transaction.post()
