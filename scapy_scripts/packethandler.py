#!/usr/bin/python

# Joe Welch 10 Jul 2019
# Developed basic packet handler using scapy

# Revision/config info
# Python 3 
#
# Initial file developed from Vivek PenTester Academy course


import sys
from scapy.all import *

def PacketHandler(pkt):
    if pkt.haslayer(Dot11):
        print(pkt.summary())
    else:
        print("Not an 802.11 packet.")
    return

sniff(iface = sys.argv[1], count = int(sys.argv[2]), prn = PacketHandler)
