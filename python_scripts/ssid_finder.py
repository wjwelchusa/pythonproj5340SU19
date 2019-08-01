#!/usr/bin/python

# Joe Welch 18 Jul 2019
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
# SSID Finder works based upon:
#    filter the beacon frames
#    step through the Dot11Elt list to find the SSID's.
# Initial script assumes the SSID as the first tagged parameter.
# Adjustments: Iterate through all the tagged parameters (ELT) to find the SSID.
# The channel hopping required for this sniffing is done by running airodump-ng prior
# to running the below script.

import sys
from scapy.all import *

ssids = set()

def PacketHandler(pkt):
    if pkt.haslayer(Dot11Beacon):   #documentation for extract is scapy >>> ls()

        if (pkt.info not in ssids) and pkt.info:
            ssids.add(pkt.info)
            print(len(ssids), pkt.addr3, pkt.info)

        
        
        
    return

sniff(iface = sys.argv[1], count = int(sys.argv[2]), prn = PacketHandler)
