import socket,threading,time,sys

ip = '172.25.160.132'
port = 8888
addr = (ip,port)

#change format

def display(tupletxt):
    txt= str(tupletxt).replace(',',':')
    txt= txt.replace(' ','')
    txt= txt.replace('(','')
    txt= txt.replace(')','')
    txt= txt.replace('\'','')
    return txt

#creating and binding server socket
def bindsock():
    global s
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(addr)
    print('[*]Server socket binded')

def startlistening():
    s.listen(5)
    print(f'[*]Listening for connections at {ip}:{port}')

#accepting connections
def acceptconnection():
    global client
    acceptingconn = True
    while acceptingconn == True:
        client, caddr = s.accept()
        
        #displaying connection info
        tupletxt = caddr
        clientaddr = display(tupletxt)
        print(f'[*]Connection established with {clientaddr}.')
        acceptingconn = False
    
def afterconn():
        while True:
            cmdinput = str(input('tcpshell> '))
            
            #closing connection
            if cmdinput == 'close connection':
                #sends quite conn. msg
                print(f'sending quit msg')
                quitmsg = 'quit_msg-init'
                client.send(bytes(quitmsg,'utf-8'))
                sys.exit('EXITING')

            else:
                print(f'[sending cmd]: {cmdinput}')

                client.send(bytes(cmdinput, 'utf-8'))
                #recieving info
                #dynamic buffer size
                buffersizebytes = client.recv(1028)
                buffersize = int(buffersizebytes.decode('utf-16'))
                print(f'[*]msg is {str(buffersize)} bytes long(utf-16)')
                
                msgbytes = client.recv(buffersize)
                msg = msgbytes.decode('utf-16')
                print(f'[Recieved]: {msg}')

def main():
    start = True
    while start == True:
        bindsock()
        startlistening()
        acceptconnection()
        afterconn()
        start = False

main()