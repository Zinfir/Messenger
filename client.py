"""Messenger client"""
# python client.py localhost 8888

import time, json, sys
from socket import socket, AF_INET, SOCK_STREAM


def make_presence_msg():
    TIMESTAMP = time.ctime(time.time())
    PRESENCE_MSG = {
        "action": "presence",
        "time": TIMESTAMP,
        "type": "status",
        "user": {
            "account_name": "Zinfir",
            "status": "Yep, I am here!"
        }
    }
    return json.dumps(PRESENCE_MSG)
    

def run_client():
    if len(sys.argv) > 0:
        HOST = sys.argv[1]
        PORT = int(sys.argv[2])
    SOCKET = socket(AF_INET, SOCK_STREAM)
    SOCKET.connect((HOST, PORT))
    JSON_MSG = make_presence_msg()
    SOCKET.send(JSON_MSG.encode('utf-8'))
    DATA = SOCKET.recv(1000000)
    dict = json.loads(DATA.decode('utf-8'))
    print('Сообщение от сервера: ', dict['response'], ', длиной ', len(DATA), 'байт')
    SOCKET.close()


if __name__ == '__main__':
    run_client()
    TIMESTAMP = time.ctime(time.time())
    PRESENCE_MSG = {
        "action": "presence",
        "time": TIMESTAMP,
        "type": "status",
        "user": {
            "account_name": "Zinfir",
            "status": "Yep, I am here!"
        }
    }
    print(json.dumps(PRESENCE_MSG))
