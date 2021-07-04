from flask import Flask
from threading import Thread


app = Flask('')


@app.route('/')
def home():
  return('Таки помирать еще мне рано!')


def run():
  app.run(host = '0.0.0.0', port = 8080)


def continuing_run():
  t = Thread(target = run)
  t.start()