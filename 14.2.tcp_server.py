import socket
import time
s = socket.socket()
s.bind(('', 8888))
s.listen()
while True:
    client, addr = s.accept()#return conn,addr
    print(client)
    timestr = time.ctime(time.time())+'\r\n'
    client.send(timestr.encode())
    #send参数encode('utf8')
    client.close()