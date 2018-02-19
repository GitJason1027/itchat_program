import itchat
from itchat.content import *
from tuling import getResponse

@itchat.msg_register([TEXT,MAP])
def text_reply(msg):
	print('From:'+msg['User']['RemarkName'])
	print(msg['Text'])
	text = '🍉:'+getResponse(msg['Text'])['text']
	print(text)
	return text

@itchat.msg_register([CARD, NOTE, SHARING, PICTURE,
    RECORDING, VOICE, ATTACHMENT, VIDEO, FRIENDS, SYSTEM])
def other_reply(msg):
	text = '🍉:我看不懂文字和表情以外的东西哦'
	return text



itchat.auto_login()
itchat.run()