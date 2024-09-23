import socket

def servidor(host="127.0.0.1", puerto=7777):
    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor_socket.bind((host, puerto))
    servidor_socket.listen()

    print(f"Servidor escuchando en {host}: {puerto}")

    conn, addr = servidor_socket.accept()
    with conn:
        print(f"Conexión establecida en {addr}")
        while True:
            datos = conn.recv(1024)
            if not datos:
                break
            print(f"Cliente: {datos.decode()}")
            mensaje = input("Servidor (tu mensaje): ")
            conn.sendall(mensaje.encode())
if __name__ == '__main__':
    servidor()
