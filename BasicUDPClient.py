#
# NAME : OLIVIER METZINGER
# STUDENT ID : 50191643
#


from socket import *
import time
import sys

#SERVER IP CONFIG
serverName = '127.0.0.1'
serverPort = 12000
# clientSocket.bind(('', 5432))

#GLOBAL VARIABLES
clientSocket = socket(AF_INET, SOCK_DGRAM)
gettime = lambda: time.time() * 1000


#MENU TEXT
def init_text():
    print("<Menu>")
    print("1) convert text to UPPER-case")
    print("2) get my IP address and port number")
    print("3) get server time")
    print("4) get server running time")
    print("5) exit")

#FONCTION FOR GET THE SERVER MESSAGE + TIME IT TAKES FOR SERVER/TASK
def same_sending():
    start = gettime()
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    end = gettime()
    final_res = end - start
    final_res = round(final_res, 1)
    print('\nReply from server:', modifiedMessage.decode())
    print('Response time: ', final_res, ' ms\n')
    start_socket()


def start_socket():
    init_text()
    choice_number = input('Input option: ')
    #GET THE USER NUMBER
    clientSocket.sendto(choice_number.encode(), (serverName, serverPort))
    while True:
        if choice_number == "1":
            sentence_caps = input('Input sentence: ')
            start = gettime()
            clientSocket.sendto(sentence_caps.encode(), (serverName, serverPort))
            modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
            end = gettime()
            final_res = end - start
            final_res = round(final_res, 1)
            print('\nReply from server:', modifiedMessage.decode())
            print('Response time: ', final_res, ' ms\n')
            start_socket()
        #NUMBER 2, 3, 4 ONLY GET SERVER ANSWER NO NEED TO SEND
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
