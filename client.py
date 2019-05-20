"""Messenger client"""
# python client.py localhost 8888

import time
import json
import sys
import logging
import logs.client_log_config
from socket import socket, AF_INET, SOCK_STREAM
from utility import log


LOGGER = logging.getLogger('client')


@log('client')
def make_presence_msg():
    """Create presence message"""
    LOGGER.debug('Presence message created')
    timestamp = time.ctime(time.time())
    presence_msg = {
        "action": "presence",
        "time": timestamp,
        "type": "status",
        "user": {
            "account_name": "Zinfir",
            "status": "Yep, I am here!"
        }
    }
    return json.dumps(presence_msg)


def run_client():
    """Start client"""
    LOGGER.debug('Start client')
    if len(sys.argv) > 0:
        host = sys.argv[1]
        port = int(sys.argv[2])
    client_socket = socket(AF_INET, SOCK_STREAM)
    try:
        client_socket.connect((host, port))
        LOGGER.debug('Socket connection success')
    except AttributeError:
        LOGGER.error('Socket connection failed')
    json_msg = make_presence_msg()
    client_socket.send(json_msg.encode('utf-8'))
    data = client_socket.recv(1000000)
    server_data = json.loads(data.decode('utf-8'))
    print('Сообщение от сервера: ', server_data['response'], ', длиной ', len(data), 'байт')
    client_socket.close()


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
