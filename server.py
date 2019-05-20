"""Messenger server"""
# python server.py -p 8888

import sys
import json
import logging
import logs.server_log_config
from socket import socket, AF_INET, SOCK_STREAM
from utility import log


LOGGER = logging.getLogger('server')


@log('server')
def make_response():
    """Create response message"""
    LOGGER.debug('Response created')
    msg = {
        "response": 200,
        "alert": "OK"
    }
    return json.dumps(msg)


def run_server():
    """Start server"""
    LOGGER.debug('Start server')

    if len(sys.argv) > 0:
        for index, param in enumerate(sys.argv):
            if param == '-p':
                port = int(sys.argv[index + 1])
            elif param == '-a':
                argv_addr = sys.argv[index + 1]
    server_socket = socket(AF_INET, SOCK_STREAM)
    try:
        server_socket.bind(('', port))
        LOGGER.debug('Socket binding success')
    except AttributeError:
        LOGGER.error('Socket binding failed')
    server_socket.listen(5)

    while True:
        client, addr = server_socket.accept()
        data = client.recv(1000000)
        json_msg = make_response()
        client.send(json_msg.encode('utf-8'))
        client.close()
        print('Сообщение: ', data.decode('utf-8'), ', было отправлено клиентом: ', addr)

if __name__ == '__main__':
    run_server()
