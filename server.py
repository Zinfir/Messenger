"""Messenger server"""
# python server.py -p 8888

import time, sys, json
from socket import socket, AF_INET, SOCK_STREAM


def make_response():
    MSG = {
            "response": 200,
            "alert": "OK"
        }
    return json.dumps(MSG)
    

def run_server():
    if len(sys.argv) > 0:
        for index, param in enumerate(sys.argv):
            if param == '-p':
                PORT = int(sys.argv[index + 1])
            elif param == '-a':
                ARGV_ADDR = sys.argv[index + 1]
    SOCKET = socket(AF_INET, SOCK_STREAM)
    SOCKET.bind(('', PORT))
    SOCKET.listen(5)

    while True:
        CLIENT, ADDR = SOCKET.accept()
        DATA = CLIENT.recv(1000000)
        
        JSON_MSG = make_response()
        CLIENT.send(JSON_MSG.encode('utf-8'))
        CLIENT.close()
        print('Сообщение: ', DATA.decode('utf-8'), ', было отправлено клиентом: ', ADDR)

if __name__ == '__main__':
    run_server()
