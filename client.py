import socket
import time

hostName = "localhost"
port = 5160

int_socket = socket.socket()
int_socket.connect((hostName, port))


print("Bağlantı Sağlandı! {}:{}".format(hostName,port))

message = input("---->: ")
print("Server Bekleniyor")

while message != "\cikis":
    int_socket.send(message.encode())
    gelen_veri = int_socket.recv(1024).decode()
    print("SERVER : " + gelen_veri)

    message = input("---->: ")
    print("Server Bekleniyor...")

int_socket.close()