from socket import *
from datetime import datetime
import time
import sys
from threading import Thread
import _thread

CLIENT_NUMBERING = 0
CUR_CLIENT = 0

serverPort = 31643
gettime = lambda: time.time()
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

def incr_id_user():
    global CLIENT_NUMBERING
    CLIENT_NUMBERING += 1

    return 'client ' + str(CLIENT_NUMBERING)



def start_socket(connectionSocket):
    print("The server is ready to receive on port", serverPort)
    start = datetime.now()
    global CUR_CLIENT


    while True:
        (connectionSocket, clientAddress) = serverSocket.accept()
        print('Connection requested from', clientAddress)
        _thread.start_new_thread(start_socket, (connectionSocket,))
        client_name = incr_id_user()
        CUR_CLIENT += 1
        print(client_name + ' connected. Number of connected clients = ' + str(CUR_CLIENT))

        while True:
            client_code_number = connectionSocket.recv(2048)
            server_code_number = client_code_number.decode()
            if (server_code_number == "1"):
                print("Command 1\n\n")
                message = connectionSocket.recv(2048)
                modifiedMessage = message.decode().upper()
                connectionSocket.send(modifiedMessage.encode())
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
        connectionSocket.close()
        CUR_CLIENT -= 1
        print(client_name + ' disconnected. Number of connected clients = ' + str(CUR_CLIENT))

if __name__ == '__main__':
    try:
        start_socket("")
    # IF CTRL + C
    except KeyboardInterrupt:
        print("\nBye bye~")
        sys.exit()