import socket as S
host="192.168.101.166"
port=3700
sock=S.socket(type=S.SOCK_DGRAM)
sock.bind((host,port))
print("Server is Started")
while True:
    data,add=sock.recvfrom(1024)
    data=data.decode()
    if data=="CLOSE":
        break
    print("Client Data:",data)
    msg=input("Server Data:").encode()
    sock.sendto(msg,add)
sock.close()