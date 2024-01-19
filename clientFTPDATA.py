import socket
import psutil

def get_address_ip():
    try:
        # Obté el nom del host
        host_name = socket.gethostname()
        interfaces_de_red = psutil.net_if_addrs()

        # Obté l'adreça IP asociada al nom del host
        address_ip = socket.gethostbyname(host_name)
        # Busca la primera interfaz que esté conectada a la red local y obtiene su dirección IP
        address_ip = None
        for interface, direcciones in interfaces_de_red.items():
            for direccion in direcciones:
                if direccion.family == socket.AF_INET and not direccion.address.startswith("127."):
                    address_ip = direccion.address
                    break
            if address_ip:
                break

        if address_ip:
            print(f"La dirección IP de la interfaz de red conectada a la red local es: {address_ip}")
        else:
            print("No se encontró una interfaz de red conectada a la red local.")

        return address_ip 

    except Exception as e:
        print(f"Error al obtenir l'addreça IP: {e}")

def main():
    address_ip = get_address_ip()
    # Configura el host y el puerto
    host = address_ip  # Puedes cambiarlo por la dirección IP de tu máquina
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
        #response = "Hola, cliente. ¡Conexión exitosa!"
        #client_socket.send(response.encode('utf-8'))

    except Exception as e:
        print(f"Error en la conexión: {e}")
    finally:
        # Cierra el socket del cliente
        client_socket.close()

if __name__ == "__main__":
    main()