#
# NAME : OLIVIER METZINGER
# STUDENT ID : 50191643
#


from socket import *
import time
import sys

serverName = 'nsl2.cau.ac.kr'
serverPort = 0
gettime = lambda: time.time() * 1000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))


#MENU TEXT
def init_text():
    print("<Menu>")
    print("1) convert text to UPPER-case")
    print("2) get my IP address and port number")
    print("3) get server time")
    print("4) get server running time")
    print("5) exit")

def same_sending():
    start = gettime()
    modifiedMessage = clientSocket.recv(2048)
    end = gettime()
    final_res = end - start
    final_res = round(final_res, 1)
    print('\nReply from server:', modifiedMessage.decode())
    print('Response time: ', final_res, ' ms\n')
    start_socket()

#FONCTION FOR GET THE SERVER MESSAGE + TIME IT TAKES FOR SERVER/TASK

def start_socket():
    init_text()
    choice_number = input('Input option: ')
    #GET THE USER NUMBER
    clientSocket.send(choice_number.encode())
    while True:
        if choice_number == "1":
            sentence_caps = input('Input sentence: ')
            start = gettime()
            clientSocket.send(sentence_caps.encode())
            modifiedMessage = clientSocket.recv(2048)
            end = gettime()
            final_res = end - start
            final_res = round(final_res, 1)
            print('\nReply from server:', modifiedMessage.decode())
            print('Response time: ', final_res, ' ms\n')
            start_socket()
        elif choice_number == "2" or choice_number == "3" or choice_number == "4":
            same_sending()
        elif choice_number == "5":
            print("\nBye bye~")
            sys.exit()
        else:
            start_socket()
        clientSocket.close()

if __name__ == '__main__':
    try:
        print("The client is running on port", clientSocket.getsockname()[1])
        start_socket()
    #IF CTRL + C
    except KeyboardInterrupt:
        print("\nBye bye~")
        sys.exit()