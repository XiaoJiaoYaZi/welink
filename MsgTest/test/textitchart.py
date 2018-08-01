import itchat


#from itchat.content import itcontent



#itchat.send('nihao',)
@itchat.msg_register(itchat.content.TEXT)
def uer_reply(msg):
    # msg[‘ToUserName’] 为通信人名
    print(msg['Text'])
    print(msg['ToUserName'])
    itchat.send(msg['Text'],msg['ToUserName'])

itchat.auto_login(hotReload=True)
print(itchat.get_friends())
print(itchat.search_friends(nickName = 'May'))
itchat.send('nihao','@c24cd210537fcbe7796222d3701ff49dfeca2d05ed98d39cb899fc7b977e51fa')
itchat.run()