import socket
import threading
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("192.168.1.105",2000))
def send():
    while True:
        message=input()
        msg=message.encode()
        s.sendto(msg,("192.168.1.103",2000))
def recieve():
    while True:
        x=s.recvfrom(1024)
        y=x[0].decode()
        print("\n"+x[1][0]+" : "+y+"\n")
r=threading.Thread(target=recieve)
st=threading.Thread(target=send)
r.start()
st.start()
