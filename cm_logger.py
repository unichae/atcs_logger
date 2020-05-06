import ReceiveFromProxy
import AtcsLogger
import LogWindow
import threading
import RegisterToProxy
import socket
import struct

def openSocket():
    myAddress = RegisterToProxy.get_ip()
    myPort = 23232
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((myAddress, myPort))

    print("server start")
    print("server IP: {:s} | port: {:d}".format(myAddress, myPort))

    return sock


if __name__ == "__main__":
    # window creation 
    print("ATCS logger start")
    sock = openSocket()

    # temp logger
    t_register = threading.Thread(target=RegisterToProxy.register, args=(sock, ))
    t_register.start()
    

    # temp logger
    t_receiver = threading.Thread(target=ReceiveFromProxy.receiveLog, args=(sock, ))
    t_receiver.start()
    
    t_receiver.join()
    t_register.join()