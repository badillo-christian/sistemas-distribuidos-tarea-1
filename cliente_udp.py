import socket

#Se solicita la ip del servidor
user_udp_ip_ = input("introduzca la IP del server\n")
#Se Solicita el puerto
user_udp_port_ = input("introduzca el puerto del server\n")
#Se crea socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#Se deja el socket en modo de envio y todos lo mensajes escritos son enviados.
while True:
    user_udp_message_ = input("introduzca el mensaje a enviar\n")
    sock.sendto(bytes(user_udp_message_, 'utf-8'), (user_udp_ip_, int(user_udp_port_)))
    