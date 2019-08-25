import socket


def powmod(p,e,n):
    result=1
    while e!=0:
        result*= p % n
        e-=1
    return result%n


s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()
print("Server will start on host",host)
port=1024
s.bind((host,port))
print("")
print("Server done binding of host and port successfully")
print("")
print("Server is waiting for connection")
print("")
s.listen(1)
conn,addr=s.accept()
print(addr,"is connected to server and is online now...")
print("")
prikey=int(input("Enter Server private key"))
message=str(powmod(17,prikey,23))
print("")
message=message.encode()
conn.send(message)
print("message has been send")
print("")
income_message = conn.recv(1024)
income_message = income_message.decode()
print("client:",income_message)
income_message=int(income_message)
print("Secreat key shared",powmod(income_message,prikey,23))