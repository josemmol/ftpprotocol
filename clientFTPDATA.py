import socket

def main():
    # Configura el host y el puerto
    host = '127.0.0.1'  # Puedes cambiarlo por la dirección IP de tu máquina
    port = 40000

    # Crea un objeto socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Vincula el socket al host y puerto especificados
        server_socket.bind((host, port))

        # Escucha las conexiones entrantes (máximo 1 conexión en la cola)
        server_socket.listen(1)
        print(f"Servidor escuchando en {host}:{port}")

        # Acepta la conexión entrante
        client_socket, client_address = server_socket.accept()
        print(f"Conexión aceptada desde {client_address}")

        # Maneja la conexión
        handle_connection(client_socket)

    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Cierra el socket del servidor
        server_socket.close()

def handle_connection(client_socket):
    try:
        # Recibe datos del cliente
        data = client_socket.recv(1024)
        print(f"Datos recibidos: {data.decode('utf-8')}")

        # Envía una respuesta al cliente
        response = "Hola, cliente. ¡Conexión exitosa!"
        client_socket.send(response.encode('utf-8'))

    except Exception as e:
        print(f"Error en la conexión: {e}")
    finally:
        # Cierra el socket del cliente
        client_socket.close()

if __name__ == "__main__":
    main()