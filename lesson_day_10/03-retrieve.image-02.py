import ssl
from urllib.request import urlopen

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

img = urlopen('https://httpbin.org/image/png', context=ctx)
fhand = open('sample.png', 'wb')
size = 0
while True:
    info = img.read(100000)
    if len(info) < 1: break
    size = size + len(info)
    fhand.write(info)
    
print(size, 'characters copied.')
fhand.close()