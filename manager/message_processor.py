from wcferry import Wcf, WxMsg
from configuration import Config
from manager.finance import Transaction as finance_Transaction


class MessageProcessor:
    # def __init__(self, msg: TransactionMsg) -> None:
    #     self.msg = msg
    def __init__(self, config: Config) -> None:
        self.TAG = "MessageProcessor"
        self.config = config
        self.finance_transaction = finance_Transaction()

    def processMsg(self, msg: WxMsg) -> str:
        print(self.TAG, msg.sender)
        content = msg.content.split("\u2005")
        if len(content) < 2:
            return "内容错误"

        contentItems = content[1].split()

        if contentItems[0] in self.config.FINANCE_TRIGGERS:
            res = self.finance_transaction.processMsg(contentItems, msg)
            rsp = "个人账目统计"
            rsp += "\n"
            rsp += "工单编号：" + ""
            rsp += "\n"
            rsp += "账户姓名：" + res["name"]
            rsp += "\n"
            rsp += "账户余额：" + str(round(res["company_account"], 2))
            return rsp
        return ""
