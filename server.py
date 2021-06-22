import socket
import time

hostName = "localhost"
port = 5160

int_socket = socket.socket()
int_socket.bind((hostName, port))

int_socket.listen(1)

conn, adress = int_socket.accept()

print(str(adress)+ "Bağlantı Sağlandı")

while True:
    while True:
        try:
            gelen_veri = str(conn.recv(1024).decode())
            print("Client şunu yolladı: "+ gelen_veri)
            break
        except ConnectionResetError:
            time.sleep(2)
            conn, adress = int_socket.accept()
            print(str(adress)+ "Bağlantı Sağlandı")
    if gelen_veri == "\cikis":
        time.sleep(2)
        break
    else:
        message = input("---->: ")
        print("Client Bekleniyor...")
        conn.send(message.encode())

conn.close()