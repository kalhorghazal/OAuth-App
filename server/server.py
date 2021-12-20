from flask import Flask, request
import requests
from urllib.parse import urlparse
import json

try:
    from urlparse import parse_qs
except ImportError: 
    from cgi import parse_qs
    urlparse.parse_qs = parse_qs

app = Flask(__name__)

@app.route("/oauth/redirect")
def oauth_redirect():
	code = request.args.get('code')
	print(f'Github code is: {code}')

	tokenRequestParams = {'client_id': '4d5eb5180a71cdf82b7d', 
		'client_secret': '6d1ecb318e300ebbea1890c7100b86ed0eec4e36',
		'code': str(code)}
	tokenResponse = requests.post('https://github.com/login/oauth/access_token', params=tokenRequestParams)
	token = parse_qs(tokenResponse.text)['access_token'][0]
	profileResponse = requests.get('https://api.github.com/user', headers={'Authorization': 'token ' + token})
	print(profileResponse.text)

	return f'Github code is: {code}'

if (__name__ == '__main__'):
	app.run(host= '0.0.0.0', port = 8589)
