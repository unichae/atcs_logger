import socket
import struct
from time import sleep

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        # doesn't even have to be reachable
        s.connect(('118.219.52.84', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()

    return IP

def register(sock):
    print("register thread start")
    # myAddress = get_ip()
    # myPort = 23232
    # sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # sock.bind((myAddress, myPort))

    # print("server start")
    # print("server IP: {:s} | port: {:d}".format(myAddress, myPort))

    # send register packet id: 0x1120
    while True:
        proxyAddress = '118.219.52.84'
        proxyPort = 6900
        data = "\xfe\x00\x00\x02\x00\x11\x20\x12\x34\x56\x78"
        sock.sendto(bytes(data, "utf-8"), (proxyAddress, proxyPort))
        print("register OK")
        sleep(4)