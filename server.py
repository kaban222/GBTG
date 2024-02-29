from flask import Flask, render_template, request
from threading import Thread
import json

app = Flask('app')

@app.route('/')
def maun():
  txt = request.args.get('param')
  if txt == "data":
    return open("persons.json", "r").read()
  else:
    return render_template("index.html")

def run():
    app.run(host="0.0.0.0", port=8463)

def keep_alive():
    server = Thread(target=run)
    server.start()

