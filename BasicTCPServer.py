#
# NAME : OLIVIER METZINGER
# STUDENT ID : 50191643
#


from socket import *

serverPort = 4242
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('nsl5.cau.ac.kr', serverPort))
serverSocket.listen(1)

print("The server is ready to receive on port", serverPort)

while True:
    (connectionSocket, clientAddress) = serverSocket.accept()
    print('Connection requested from', clientAddress)
    message = connectionSocket.recv(2048)
    modifiedMessage = message.decode().upper()
    connectionSocket.send(modifiedMessage.encode())
    connectionSocket.close()

