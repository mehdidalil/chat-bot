import requests
import json
import socketio
import base64
from scraping import scrapFnacLatestReleases
from parsing import parseMessage
from Auth import Auth

auth = Auth("http://localhost:8000/user/login", {
	"mail": "dalil.mahdi@gmail.com",
	"password": "24041993abc" })
sio = socketio.Client()

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
		payload = {"content": releases}
		headers = {"Authorization": f'Bearer {auth.token}'}
		send = requests.post("http://localhost:8000/message/create", json=payload, headers=headers)
		print("Message sent")

sio.connect(f'http://localhost:8080?token={auth.token}')

sio.wait()