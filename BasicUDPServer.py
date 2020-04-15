#
# NAME : OLIVIER METZINGER
# STUDENT ID : 50191643
#

from socket import *
from datetime import datetime
import time
import sys

#GLOBAL VARIABLES
serverPort = 12000
gettime = lambda: time.time()
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))


def start_socket():
    print("The server is ready to receive on port", serverPort, "\n\n")
    start = datetime.now()

    while True:
        client_code_number, clientAddress = serverSocket.recvfrom(2048)
        print('Connection requested from', clientAddress)
        #GET NUMBER OF CLIENT
        server_code_number = client_code_number.decode()
        #SELECT THE PROPER ONE (NUMBER)
        if (server_code_number == "1"):
            print("Command 1\n\n")
            client_sentence_caps, clientAddress = serverSocket.recvfrom(2048)
            modifiedMessage = client_sentence_caps.decode().upper()
            serverSocket.sendto(modifiedMessage.encode(), clientAddress)
        elif (server_code_number == "2"):
            print("Command 2\n\n")
            modifiedMessage = str("IP = " + str(clientAddress[0]) + ", port = " + str(clientAddress[1]))
            serverSocket.sendto(modifiedMessage.encode(), clientAddress)
        elif (server_code_number == "3"):
            print("Command 3\n\n")
            modifiedMessage = str(datetime.now().time())
            serverSocket.sendto(modifiedMessage.encode(), clientAddress)
        elif (server_code_number == "4"):
            print("Command 4\n\n")
            end = datetime.now()
            final_res = end - start
            modifiedMessage = str(final_res)
            serverSocket.sendto(modifiedMessage.encode(), clientAddress)
        else:
            continue


if __name__ == '__main__':
    try:
        start_socket()
    #IF CTRL + C
    except KeyboardInterrupt:
        print("\nBye bye~")
        sys.exit()
