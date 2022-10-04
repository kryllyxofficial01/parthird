from flask import Flask
from threading import Thread

client = Flask('')

@client.route('/')
def home():
	return "online"

def run():
  client.run(host='0.0.0.0', port=8080)

def runServer():  
    t = Thread(target=run)
    t.start()