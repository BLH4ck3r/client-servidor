import socket

def cliente(host="127.0.0.1", puerto=7777):
    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente_socket.connect((host, puerto))

    print(f"Conectando al servidor en {host}: {puerto}")

    while True:
        mensaje = input("Cliente (tu mensaje): ")
        cliente_socket.sendall(mensaje.encode())
        data = cliente_socket.recv(1024)
        print(f"Servidor: {data.decode()}")
if __name__ == '__main__':
    cliente()
