import requests
import json
import socketio
import base64
from scraping import scrapFnacLatestReleases
from parsing import parseMessage

sio = socketio.Client()
payload = { "mail": "dalil.mahdi@gmail.com", "password": "24041993abc" }
data = requests.post("http://localhost:8000/user/login", json=payload)
token = data.text
user = json.loads(base64.b64decode(token.split(".")[1] + "=="))

@sio.event
def connect():
	print("Bot connected")
@sio.event
def disconnect():
	print("Bot disconnected")
	sio.emit("disconnect")
@sio.event
def newMessage(data):
	message = data["content"]
	if parseMessage(message) == "fnac":
		releases = scrapFnacLatestReleases(10)
		payload = {"content": releases, "username": user["username"], "avatarId": user["avatarId"]}
		headers = {"Authorization": f'Bearer {token}'}
		send = requests.post("http://localhost:8000/message/create", json=payload, headers=headers)
		print("Message sent")

sio.connect(f'http://localhost:8080?token={token}')

sio.wait()