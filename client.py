import socket


def powmod(p,e,n):
    result=1
    while e!=0:
        result*= p % n
        e-=1
    return result%n


s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=input(str("please enter host name of server:"))
port=1024
s.connect((host,port))
print("Connected to  server")
print("")
prikey=int(input("Enter client private key"))
message=str(powmod(17,prikey,23))
print("")
income_message = s.recv(1024)
income_message = income_message.decode()
print("server:",income_message)
message = message.encode()
s.send(message)
print("message has been send")
print("")
income_message=int(income_message)
print("Secrete key shared",powmod(income_message,prikey,23))