from socket import *
from datetime import datetime
import time
import sys
from threading import Thread
import _thread
import select, queue

CLIENT_NUMBERING = 0
CUR_CLIENT = 0

serverPort = 31643
gettime = lambda: time.time()
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.setblocking(0)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)


def incr_id_user():
    global CLIENT_NUMBERING
    CLIENT_NUMBERING += 1

    return 'client ' + str(CLIENT_NUMBERING)


def start_socket():
    print("The server is ready to receive on port", serverPort)
    start = datetime.now()
    global CUR_CLIENT
    inputs = [serverSocket]
    outputs = []
    message_queues = {}

    while inputs:
        readable, writable, exceptional = select.select(inputs, outputs, inputs)

        for s in readable:
            if s is serverSocket:
                connection, client_address = s.accept()
                connection.setblocking(0)
                inputs.append(connection)
                message_queues[connection] = queue.Queue()
            else:
                data = s.recv(2048)
                if data:
                    message_queues[s].put(data)
                    if s not in outputs:
                        outputs.append(s)
                else:
                    if s in outputs:
                        outputs.remove(s)
                    inputs.remove(s)
                    del message_queues[s]
                    (connection, client_address) = s.getpeername()
                    s.close()

        for s in writable:
            if s not in outputs:
                continue
            try:
                next_msg = message_queues[s].get_nowait()
            except queue.Empty:
                outputs.remove(s)
            else:
                connectionSocket = s
                clientAddress = connectionSocket.getpeername()
                server_code_number = next_msg.decode()
                if (server_code_number == "1"):
                    print("Command 1\n\n")
                    message = next_msg.decode().upper()
                    connectionSocket.send(message.encode())
                elif (server_code_number == "2"):
                    print("Command 2\n\n")
                    modifiedMessage = str("IP = " + str(clientAddress[0]) + ", port = " + str(clientAddress[1]))
                    connectionSocket.send(modifiedMessage.encode())
                elif (server_code_number == "3"):
                    print("Command 3\n\n")
                    modifiedMessage = str(datetime.now().time())
                    connectionSocket.send(modifiedMessage.encode())
                elif (server_code_number == "4"):
                    print("Command 4\n\n")
                    end = datetime.now()
                    final_res = end - start
                    modifiedMessage = str(final_res)
                    connectionSocket.send(modifiedMessage.encode())


if __name__ == '__main__':
    try:
        start_socket()
    # IF CTRL + C
    except KeyboardInterrupt:
        print("\nBye bye~")
        sys.exit()
