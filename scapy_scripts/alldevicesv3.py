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
# Iterative improvement based on more succinct use of scapy syntax and 
# focused on extracting particular values.

import sys
from scapy.all import *

devices = set()

def PacketHandler(pkt):
    if pkt.haslayer(Dot11):

        if pkt.addr2 and (pkt.addr2 not in devices):
            devices.add(pkt.addr2)
            print(len(devices), pkt.addr2, pkt.payload.name)
        
        
        
    return

sniff(iface = sys.argv[1], count = int(sys.argv[2]), prn = PacketHandler)
