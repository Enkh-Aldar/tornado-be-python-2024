import socket
import ssl
addr = input('Enter a website address: ')
domain = addr.split('/')[2]
print(domain)
port = 80

try:
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((domain, port))
    test =    f'GET {addr} HTTP/1.0\r\n\r\n'
    print(test)
    cmd = f'GET {addr} HTTP/1.0\r\n\r\n'.encode()
    mysock.send(cmd)
    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        print(data.decode(),end='')
    mysock.close()
except:
    print("Wrong URL")
    exit()


