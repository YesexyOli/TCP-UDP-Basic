#
# NAME : OLIVIER METZINGER
# STUDENT ID : 50191643
#


from socket import *
from datetime import datetime
import time
import sys

serverPort = 7722
gettime = lambda: time.time()
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)


def start_socket():
    print("The server is ready to receive on port", serverPort)
    start = datetime.now()

    while True:
        (connectionSocket, clientAddress) = serverSocket.accept()
        print('Connection requested from', clientAddress)
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

if __name__ == '__main__':
    try:
        start_socket()
    # IF CTRL + C
    except KeyboardInterrupt:
        print("\nBye bye~")
        sys.exit()
