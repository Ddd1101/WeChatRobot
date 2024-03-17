from enum import Enum
from datetime import datetime


class MsgType(Enum):
    NONE = -1
    RETURN_MONEY = 1


class TransactionMsg:
    def __init__(self) -> None:
        self.msg_type = MsgType.NONE
        self.time = datetime.now()
        self.owner = ""  # 消息发起者
        self.company = ""  # 消息来源公司
        self.group = ""  # 消息来源职务
        self.payer = ""  # 出款人
        self.payee = ""  # 收款人
        self.payer_id = ""
        self.payee_id = ""
        self.issue = ""  # 事项
        self.remark = ""  # 备注
