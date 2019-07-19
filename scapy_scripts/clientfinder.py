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
# Client Finder works with scapy functions:
#    filter the beacon frames
#    step through the Dot11Elt list to find the SSID's.
# Improved script adjustments: A client steps through the local SSID list in an effort to locate and associate a permitted AP. Identifying SSID's may provide 
# OSINT info on client info. (It can also be used for counter OPSEC work.)
# Consider changing the storage container for this, from a tuple, to a dictionary, with the client MAC as the source and a list of searched SSID's as the value
#
# This script may not pull in many signals unless local clients are seeking association. I need to force associations with local smartphines, ipads.
# Also, the scan needs to occur exactly when the airodump-ng is stapping through that particular channel. Otherwise the scan will miss the signals.
import sys
from scapy.all import *

clientprobes = set()

def PacketHandler(pkt):

    if pkt.haslayer(Dot11ProbeReq):   #documentation for extract is scapy >>> ls() this will detect WLAN probe requests
                                    # Wireshark and lsc() indicates both the source MAC and the probed SSID
        if len(pkt.info) > 0:
            testcase = pkt.addr2 + "---" + pkt.info
            if testcase not in clientprobes:
                clientprobes.add(testcase)
                print("New probe found:  " + pkt.addr2 + pkt.info)
        
        
    return

sniff(iface = sys.argv[1], count = int(sys.argv[2]), prn = PacketHandler)
