import requests

def getResponse(info):
	apiUrl = 'http://www.tuling123.com/openapi/api'
	data = {
		'key' : '34a1e9585ab549ebb7090930d5749d73',
		'info' : info,
		'userid' : 'wechat-robot',
	}

	r = requests.post(apiUrl,data=data).json()
	return r