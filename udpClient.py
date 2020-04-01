import socket


def Main():
    host = '127.0.0.1'
    port = 8081

    server = (host, 8080)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))

    message = input("-> ")
    while message != 'q':
        s.sendto(message.encode('utf-8'), server)
        data, addr = s.recvfrom(1024)
        data = data.decode('utf-8')
        print("Recieved from server: "+data)
        message = input("-> ")
    s.close()


if __name__ == "__main__":
    Main()
