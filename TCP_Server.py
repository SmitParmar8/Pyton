import socket as S
host="localhost"
port=3600
sock=S.socket(S.AF_INET,S.SOCK_STREAM)
sock.bind((host,port))
sock.listen()
print("Server is Started")
conn,add=sock.accept()
while True:
    data=conn.recv(1024).decode()
    if data=="CLOSE":
        break
    print("Client Data:",data)
    if data.isnumeric():
        msg="Power of Given data "+str(int(data)**3)
    else :
        msg=input("Server Data:")
    conn.send(msg.encode())
conn.close()