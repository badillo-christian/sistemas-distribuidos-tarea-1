import socket

#IP Server
UDP_IP = "127.0.0.1"
#Puerto Server
UDP_PORT = 10081
#Se crea socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#Se hace bind a la IP y Puerto
sock.bind((UDP_IP, UDP_PORT))
#Se deja el socket en modo de escucha e imprime los mensajes recibidos
while True:
    data, addr = sock.recvfrom(1024)
    print("Mensaje Recibido: %s" % data)
