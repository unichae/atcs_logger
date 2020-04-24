import socket
import struct
from datetime import datetime
import AtcsLogger
import logging


def saveLogData(str):
    # print(str)
    # time.localtime(time.time())
    # logStr = "[{:s}]: ".format(datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
    # print("[{:s}]: ".format(datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')), end='')
    logStr = ''
    for i in range(len(str)):
        # print("{:d}th byte: {:x}".format(i, str[i]))
        logStr += "{:02x} ".format(str[i]) 
        # print("{:02x}".format(str[i]) + " ", end='')
        
    # print("")

    # AtcsLogger.writeLog(logger, logStr)

    return logStr


def printLogData(str):  
    logStr = str
    print(logStr)
    # AtcsLogger.writeLog(logger, logStr)


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


# log server 
# def receiveLog(fileLogger, streamLogger):
def receiveLog():
    myAddress = get_ip()
    myPort = 23232
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((myAddress, myPort))

    print("server start")
    print("server IP: {:s} | port: {:d}".format(myAddress, myPort))


    # temp file logger 
    myLogger = logging.getLogger("atcs_file_logger")
    myLogger.setLevel(logging.INFO)
    fileName = "{:s}.log".format(datetime.now().strftime('%Y_%m_%d'))
    myFileHandler = logging.FileHandler(fileName)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    myFileHandler.setFormatter(formatter)
    myLogger.addHandler(myFileHandler)
    myStreamHandler = logging.StreamHandler()
    myStreamHandler.setFormatter(formatter)
    myLogger.addHandler(myStreamHandler)


    # send register packet id: 0x9900
    # data = [0xFE, 0x00, 0x00, 0x02, 0x00, 0x00, 0x99, 0x12, 0x34, 0x56, 0x78]
    proxyAddress = '118.219.52.84'
    proxyPort = 6900
    data = "\xfe\x00\x00\x02\x00\x00\x99\x12\x34\x56\x78"
    sock.sendto(bytes(data, "utf-8"), (proxyAddress, proxyPort))

    while True:

        data, info = sock.recvfrom(512)
        str = saveLogData(data)
        myLogger.info(str)
        
        # printLogData(str)

