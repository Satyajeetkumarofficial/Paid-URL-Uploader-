from bot import Bot
from threading import Thread
from flask import Flask

app = Flask('')

@app.route('/')
def home():
    return "Bot is alive", 200

def run():
    app.run(host='0.0.0.0', port=8080)

Thread(target=run).start()

if __name__ == '__main__':
    Bot().run()
