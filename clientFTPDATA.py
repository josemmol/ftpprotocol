import socket
import psutil

def get_address_ip():
    try:
        # Obté el nom del host
        host_name = socket.gethostname()
        interfaces_net = psutil.net_if_addrs()

        # Obté l'adreça IP asociada al nom del host
        address_ip = socket.gethostbyname(host_name)
        # Busca la primera interfície conectada a la xarxa local i obté la seva adreça IP
        address_ip = None
        for interface, list_address in interfaces_net.items():
            for i_address in list_address:
                if i_address.family == socket.AF_INET and not i_address.address.startswith("127."):
                    address_ip = i_address.address
                    break
            if address_ip:
                break

        if address_ip:
            print(f"L'adreça IP de la interfíce de xarxa conectada a la xarxa local es: {address_ip}")
        else:
            print("No s'ha trobat una interfície de xarxa conectada a la xarxa local.")

        return address_ip 

    except Exception as e:
        print(f"Error al obtenir l'addreça IP: {e}")

def main():
    address_ip = get_address_ip()
    # Configura el host y el port
    host = address_ip  # Pots cambiar-ho amb l'adreça IP del teu ordinador
    port = 32768 

    # Crea un objete socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Vincula el socket al host i port especificats
        server_socket.bind((host, port))

        # Esccolta les conexions entrants (máxim 1 conexión a la cua)
        server_socket.listen(1)
        print(f"Servidor escoltant a {host}:{port}")

        # Acepta la conexió entrant
        client_socket, client_address = server_socket.accept()
        print(f"Conexió aceptada des de {client_address}")

        # Maneja la conexió
        handle_connection(client_socket)

    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Tanca el socket del servidor
        server_socket.close()

def handle_connection(client_socket):
    try:
        # Reb les dades del client
        data = client_socket.recv(1024)
        print(f"Dades rebudes: {data.decode('utf-8')}")

        # Envía una resposta al cliente
        #response = "Hola, client. ¡La Conexió és un exit!"
        #client_socket.send(response.encode('utf-8'))

    except Exception as e:
        print(f"Error en la conexió: {e}")
    finally:
        # Tanca el socket del client
        client_socket.close()

if __name__ == "__main__":
    main()