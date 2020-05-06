import pyshark
import logging
from logging import handlers
from datetime import datetime


# file hanlder set
fileName = "{:s}.log".format(datetime.now().strftime('%Y_%m_%d_atcs_in_log_'))
myFileHandler = handlers.TimedRotatingFileHandler(filename=fileName, when='midnight', interval=1)
# myFileHandler = logging.FileHandler(fileName)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
myFileHandler.setFormatter(formatter)
myFileHandler.prefix = '%Y%m%d'

# logger set
myLogger = logging.getLogger("atcs_in_file_logger")
myLogger.setLevel(logging.INFO)
myLogger.addHandler(myFileHandler)
myStreamHandler = logging.StreamHandler()
myStreamHandler.setFormatter(formatter)
myLogger.addHandler(myStreamHandler)


def print_conversation_header(pkt):
    try:
        # print("Received")
        # protocol =  pkt.transport_layer
        # src_addr = pkt.ip.src
        # src_port = pkt[pkt.transport_layer].srcport
        # dst_addr = pkt.ip.dst
        # dst_port = pkt[pkt.transport_layer].dstport
        # print("{:%s}  {:%s}:{:%s} --> {:%s}:{:%s}".format(protocol, src_addr, src_port, dst_addr, dst_port))
        # print(pkt.data.data)
        # print(pkt)
        # print(pkt.data.data)
        myLogger.info(pkt.data.data)

    except AttributeError as e:
        #ignore packets that aren't TCP/UDP or IPv4
        pass


# cap = pyshark.LiveCapture(interface='Synergy', bpf_filter='udp port 23232')
cap = pyshark.LiveCapture(interface='Synergy', bpf_filter='udp port 23232')
cap.set_debug()
# cap.sniff()
cap.sniff(packet_count=10)
cap.apply_on_packets(print_conversation_header, timeout=1000000)