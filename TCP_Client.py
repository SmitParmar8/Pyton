import socket as S
host="localhost"
port=3600
sock=S.socket()
sock.connect((host,port))
print("Client Connected")
while True:
    msg=input("client Data:")
    sock.send(msg.encode())
    if msg=="CLOSE":
        break
    data=sock.recv(1024).decode()
    print("server data:",data)
conn.close() 