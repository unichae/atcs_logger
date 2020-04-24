import logging
from datetime import datetime

# def getFileLogger():
#     myLogger = logging.getLogger("atcs_file_logger")
#     myLogger.setLevel(logging.INFO)

#     # myStreamHandler = logging.StreamHandler()
#     # myLogger.addHandler(myStreamHandler)

#     # get time to file name
#     # fileName = "{:s}.log".format(datetime.now().strftime('%Y_%m_%d'))
    
#     fileName = "{:s}.log".format(datetime.now().strftime('%Y_%m_%d_%H_%M'))
#     myFileHandler = logging.FileHandler(fileName)
#     myLogger.addHandler(myFileHandler)

#     return myLogger

# def writeLog(myLogger, str):
#     myLogger.info(str)


# def getStreamLogger():
#     myLogger = logging.getLogger("atcs_stream_logger")
#     myLogger.setLevel(logging.INFO)

#     myStreamHandler = logging.StreamHandler()
#     myLogger.addHandler(myStreamHandler)

#     return myLogger


