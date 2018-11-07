from SMessage import BMSEMsgType
from PlatformPublicDefine import EMsgType


class EType(dict):
    def __init__(self):
        super().__init__()
        self[BMSEMsgType.MSG_SUBMIT.value[0]] = 0
        self[BMSEMsgType.MSG_HIS_MT.value[0]] = 1
        self[BMSEMsgType.MSG_HIS_REP.value[0]] = 2
        self[BMSEMsgType.MSG_REP_NTF.value[0]] = 3
        self[BMSEMsgType.MSG_HIS_MO.value[0]]   = 4
        self[BMSEMsgType.MSG_NEED_ACCBLIST.value[0]]    = 5
        self[BMSEMsgType.SUBMIT_MONITOR.value[0]]       = 6
        self[BMSEMsgType.FEECENTER_MONITOR.value[0]]    = 6
        self[BMSEMsgType.DISPATCH_MONITOR.value[0]]     = 6
        self[BMSEMsgType.RESOURCE_MONITOR.value[0]]     = 6
        self[BMSEMsgType.TIMESCAN_MONITOR.value[0]]     = 6
        self[BMSEMsgType.HISPREDEAL_MONITOR.value[0]]   = 6
        self[BMSEMsgType.HISCENTER_MONITOR.value[0]]    = 6
        self[BMSEMsgType.RESSTANOTIFY_MONITOR.value[0]] = 6
        self[BMSEMsgType.RESCOMSTATIS_MONITOR.value[0]] = 6

        self[EMsgType.MSG_CLOUD.value] = 7
        self[EMsgType.MSG_HIS_MT.value] = 8
        self[EMsgType.MSG_HIS_REP.value] = 9


if __name__ == '__main__':
    print(EMsgType.MSG_CLOUD.value)
    E = EType()
    e = E[EMsgType.MSG_CLOUD.value]
    print(e)