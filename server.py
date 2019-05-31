"""Messenger server"""
# python3 server.py -p 8888

import sys
import json
import logging
import time
import select
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
    clients = []
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
    server_socket.settimeout(0.2)

    while True:
        client, addr = server_socket.accept()
        data = client.recv(1000000)
        json_msg = make_response()
        client.send(json_msg.encode('utf-8'))
        client.close()
        print('Сообщение: ', data.decode('utf-8'), ', было отправлено клиентом: ', addr)


def mainloop():
    address = ('', 10000)
    clients = []
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(address)
    s.listen(5)
    s.settimeout(0.2)
    while True:
        try:
            conn, addr = s.accept()
        except OSError as e:
            pass
        else:
            print("Получен запрос на соединение от %s" % str(addr))
            clients.append(conn)
        finally:
            wait = 10
            r = []
            w = []
            try:
                r, w, e = select.select(clients, clients, [], wait)
            except:
                pass
            requests = read_requests(r, clients)
            if requests:
                write_responses_to_all(requests, w, clients)


def read_requests(r_clients, all_clients):
    responses = {}
    for sock in r_clients:
        try:
            data = sock.recv(1024).decode('utf-8')
            responses[sock] = data
        except:
            print('Клиент {} {} отключился'.format(sock.fileno(), sock.getpeername()))
            all_clients.remove(sock)
    return responses


def write_responses(requests, w_clients, all_clients):
    for sock in w_clients:
        if sock in requests:
            try:
                resp = requests[sock].encode('utf-8')
                sock.send(resp.upper())
            except:
                print('Клиент {} {} отключился'.format(sock.fileno(), sock.getpeername()))
                sock.close()
                all_clients.remove(sock)


def write_responses_to_all(requests, w_clients, all_clients):
    for sock in w_clients:
        if sock in requests:
            try:
                resp = requests[sock].encode('utf-8')
                for s in all_clients:
                    s.send(resp)
            except:
                print('Клиент {} {} отключился'.format(sock.fileno(), sock.getpeername()))
                sock.close()
                all_clients.remove(sock)


if __name__ == '__main__':
    # run_server()
    print('Server running...')
    mainloop()
