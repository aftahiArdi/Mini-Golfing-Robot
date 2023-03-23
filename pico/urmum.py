from flask import Flask, make_response, jsonify
import requests
from flask_cors import CORS
import json
import serial
import time



# sends json requests to the server/VM from own computer internet port

app = Flask(__name__)


CORS(app)


def  displayText():
    return "hello world"


@app.route('/')
def hello_world():
    response = make_response(displayText(), 200)
    response.mimetype = "text/plain"
    response = {"test": "hi"}
    print(response)
    global ser
    #misc code here
    sendData("A")
    time.sleep(0.4)
    print(1)

    return jsonify(response)





ser = serial.Serial('/dev/cu.usbmodem101') # open serial port




def sendData(data):
    send = data + " \r\n"
    ser.write(send.encode('utf8'))






if __name__ == '__main__':
    app.run(port=3000)
