import socket as S
host="192.168.101.166"
port=3700
sock=S.socket(type=S.SOCK_DGRAM)
print("Server is Started")
while True:
    data=input("Client:").encode()
    sock.sendto(data,(host,port))
    if data=="close":
        break
    data,add=sock.recvfrom(1024)
    print("server:",data.decode())
sock.close()