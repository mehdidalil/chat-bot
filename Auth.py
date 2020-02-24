import json
import base64
import requests

class Auth():
	def __init__(self, url, credentials):
		self.credentials = credentials
		self.url = url
		self.auth()
	
	def auth(self):
		self.response = requests.post(self.url, json=self.credentials)
		self.token = self.response.text
		self.user = json.loads(base64.b64decode(self.token.split(".")[1] + "=="))