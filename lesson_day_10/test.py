import socket
import ssl

addr = input('Enter a website address: ')

try:
    # Parse the URL to extract domain and path
    url_parts = addr.split('/')
    domain = url_parts[2]
    path = '/' + '/'.join(url_parts[3:])

    # Use default HTTP port (80) or HTTPS port (443) based on the scheme
    port = 80 if url_parts[0].lower() == 'http:' else 443

    # Create a socket and connect
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((domain, port))

    # If using HTTPS, wrap the socket with SSL/TLS
    if port == 443:
        mysock = ssl.wrap_socket(mysock, ssl_version=ssl.PROTOCOL_SSLv23)

    # Send HTTP GET request
    cmd = f'GET {path} HTTP/1.1\r\nHost: {domain}\r\n\r\n'.encode()
    mysock.send(cmd)

    count = 0
    while True:
        data = mysock.recv(512)
        if not data:
            break
        count += len(data)

        # Limit the number of received bytes
        if count > 3000:
            break

    print(f'Total received bytes: {count}')
    mysock.close()

except socket.error as e:
    print(f"Socket error: {e}")
except ssl.SSLError as e:
    print(f"SSL/TLS error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
