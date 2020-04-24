import ReceiveFromProxy
import AtcsLogger
import LogWindow
import threading
from datetime import datetime
from time import sleep


if __name__ == "__main__":
    # window creation 
    print("ATCS logger start")
    t_receiver = threading.Thread(target=ReceiveFromProxy.receiveLog)
    t_receiver.start()
    

    # file creation time


    # logger seems not good
    # refTimeStr = ''

    # while True:
    #     # file logger for everyday
    #     NowTimeStr = "{:s}".format(datetime.now().strftime('%Y-%m-%d %H:%M'))

    #     if(refTimeStr == ''):
    #         refTimeStr = "{:s}".format(datetime.now().strftime('%Y-%m-%d %H:%M'))

    #         atcsFileLogger = AtcsLogger.getFileLogger()
    #         atcsStreamLogger = AtcsLogger.getStreamLogger()
    #         # log receiver 
    #         t_receiver = threading.Thread(target=ReceiveFromProxy.receiveLog, args=(atcsFileLogger, atcsStreamLogger, ))
    #         t_receiver.start()
    #         # print("receive thread start..")
            
    #     elif(refTimeStr == NowTimeStr):
    #         # do nothing
    #         continue

    #     else:
    #         continue
    #         # file logger change?
    #         # t_receiver.join()

    #         # refTimeStr = NowTimeStr
    #         # atcsFileLogger = AtcsLogger.getFileLogger()
    #         # atcsStreamLogger = AtcsLogger.getStreamLogger()
    #         # # log receiver 
    #         # t_receiver = threading.Thread(target=ReceiveFromProxy.receiveLog, args=(atcsFileLogger, atcsStreamLogger, ))
    #         # t_receiver.start()

    #     # sleep an hour
    #     sleep(60)
    
    
