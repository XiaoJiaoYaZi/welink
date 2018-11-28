
from SQLManager import SQLManager

db = SQLManager('10.1.120.87:1433', 'sa', 'admin123!@#', 'MsgPlatform')

ProductId = 20181123
ResourceIdList = 201811231706
ForbiddenAreaSet = 0
BlacklistRank = 0
KeywordRank = 0
AppType =0
ExtendState = 0
TelecomSet = 0
BusinessType = 0
MsgPriority = 0
SingleCharCount = 0
MaxCharCount = 0
IsNumberExtend = 0
IsUpload = 0
StartSendTime = 0
EndSendTime = 0
TestSingleMsgCount = 0
TestDailyMsgCount = 0
IsSign = 0
IsPackageStatistic = 0
AuditStrategy = 0
LongSMSType = 0
MinuteIncrement = 0
BakProductExtendId = 0
LastTime = 0
BitsFlag = 0
Remark = 'remark'
MinPkgCount = 0
MaxPkgCount = 0
AuditAttribute = 'AuditAttribute'
IsAccountBind = 0
ReplaceProductExtendId = 0
SignalRegExp = 'SignalRegExp'
ForceCheckMaxNo = 0
SignNoReportBackupPrdEX = 0
WhiteMobilesBackupPrdEX = 0
TestProductExtendId = 0
DayMobileLimit = 0
TimePeriodMobileLimit = 0
RedListBackupPrdId = 0
DayContentLimit = 0
TimePeriodContentLimit = 0
PrivateBListLv = 0
RepTimeOut = 0
ResendTimes = 0
PreventComplaintsPrdEX = 0
PrivateKeywordRank = 0
ProductExtendNumber = 0

i = 100
while i<1000:
    sql = "UPDATE [MsgPlatform].[dbo].[Mas_ProductExtend] SET [ResourceIdList] = '{}' WHERE [ProductExtendId] = 101288871".format(i)
    i = i+1
    db.ExecNoQuery(sql.encode('utf-8'))

"INSERT INTO [MsgPlatform].[dbo].[Mas_ProductExtend] ([ProductExtendId], [ProductId], [ResourceIdList], [ForbiddenAreaSet], [BlacklistRank], [KeywordRank], [AppType], [ExtendState], [TelecomSet], [BusinessType], [MsgPriority], [SingleCharCount], [MaxCharCount], [IsNumberExtend], [IsUpload], [StartSendTime], [EndSendTime], [TestSingleMsgCount], [TestDailyMsgCount], [IsSign], [IsPackageStatistic], [AuditStrategy], [LongSMSType], [MinuteIncrement], [BakProductExtendId], [LastTime], [BitsFlag], [Remark], [MinPkgCount], [MaxPkgCount], [AuditAttribute], [IsAccountBind], [ReplaceProductExtendId], [SignalRegExp], [ForceCheckMaxNo], [SignNoReportBackupPrdEX], [WhiteMobilesBackupPrdEX], [TestProductExtendId], [DayMobileLimit], [TimePeriodMobileLimit], [RedListBackupPrdId], [DayContentLimit], [TimePeriodContentLimit], [PrivateBListLv], [RepTimeOut], [ResendTimes], [PreventComplaintsPrdEX], [PrivateKeywordRank], [ProductExtendNumber]) VALUES (2018112300, 20181123, '999', 0, 2, 3, 1, 1, 1, 1, 5, 70, 350, 1, 1, '2000-01-01 00:00:00.000', '2000-01-01 23:59:59.000', 0, 0, 0, 0, 2, 2, 1440, 1012888351, '2017-06-01 14:17:09.343', 451602, '【掌上车店】独享', 1, 1, '免审子产品—注意审核内容！！', 0, 0, '[【][^】]{1,24}[】]$', 0, 0, 0, 0, 200, 0, 0, 5000, 5000, 2, 0, 1, 0, 0, 12)"









