import socket
import ssl
addr = input('Enter a website address: ')
domain = addr.split('/')[2]
print(domain)
port = 80


try:
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((domain, port))
    cmd = f'GET {addr} HTTP/1.0\r\n\r\n'.encode()
    mysock.send(cmd)
    count = 0
    while True:
        data = mysock.recv(512)
        for c in data:
            count += 1
        if len(data) < 1 or count > 3000:
            break
    print(count)
    mysock.close()
except:
    print("Wrong URL")
    exit()