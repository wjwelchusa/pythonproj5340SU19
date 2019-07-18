#!/usr/bin/python

# Joe Welch 10 Jul 2019
# Developed basic packet handler using scapy
# Packet handler is being developed to provide additional info
# regarding the field names and field content for captured packets
#
# Storage data structure initially used was a set (tuple)
# Based upon use this may be better changed to a list. TBD.

# Revision/config info
# Python 3 
#
# Initial file developed from Vivek PenTester Academy course


import sys
from scapy.all import *

devices = set()

def PacketHandler(pkt):
    if pkt.haslayer(Dot11):

        dot11_layer = pkt.getlayer(Dot11)

        if dot11_layer.addr2 and (dot11_layer.addr2 not in devices):
            devices.add(dot11_layer.addr2)
            print(len(devices), dot11_layer.addr2, dot11_layer.payload.name)
        
        
        
    return

sniff(iface = sys.argv[1], count = int(sys.argv[2]), prn = PacketHandler)
