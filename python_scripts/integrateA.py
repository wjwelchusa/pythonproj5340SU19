#!/usr/bin/python3

# Joe Welch 29 Jul - 1 Aug 2019
# Integrate previously tested programs and behavior from a stand alone programs to a function to be called when the MAC addresses are retrieved with SCAPY.
# Program integrates:
# 1. alldevicesv3.py to retrieve MAC's using the radio card set in monitor mode
# 2. uses the url  "http://macvendors.co/api/" to retrieve mfr for each card
#
# Revision/config info
# Python 3 
#
# Citations/references
# 1. Initial mapping developed developed from http://macvendors.co/api/
# Python 3 Example of how to use https://macvendors.co to lookup vendor from mac address
# 2. Initial scanning developed from Vivek PenTester Academy course
#
# TODOs
# 1. rework this file as a function, to receive the MAC as a parameter and return the mfr information
# 2. determine which values should be returned for use/display



import urllib.request as urllib2	# module to access web information for 
import json							# manages structure of retrieved data
import codecs						# manages format of retrieved data
import sys							# handles command line arguments
from scapy.all import *				# provides access to scapy library



## ________________ functions _________________________

def find_mfr(mac_address):
	for x in range(5):
	    print("MAC addresses are helpful.")

	print ("Content-Type: text/html\n")
	#API base url,you can also use https if you need
	url = "http://macvendors.co/api/" # Create structure used to pair URL, with the MAC to create a search query string to workk through the API
	#Mac address to lookup vendor from
	mac_address = "BC:92:6B:A0:00:01"

	request = urllib2.Request(url+mac_address, headers={'User-Agent' : "API Browser"}) 
	response = urllib2.urlopen( request )
	reader = codecs.getreader("utf-8")  #codec modules used to extract info in str, not utf-8 format
	obj = json.load(reader(response))  # extract using json format, keyed off of OUI in the provided MAC

	#Print company name
	return (obj['result']['company']+"<br/>");

	#print company address
	#print (obj['result']['address']);



## ________________ main  _________________________

def main():


	devices = set()

	def PacketHandler(pkt):
		if pkt.haslayer(Dot11):

		    if pkt.addr2 and (pkt.addr2 not in devices):
		        devices.add(pkt.addr2)
		        print(len(devices), pkt.addr2, pkt.payload.name, find_mfr(str(pkt.addr2)))   # call to mfr here
		    
		    
		    
		return

	sniff(iface = sys.argv[1], count = int(sys.argv[2]), prn = PacketHandler)
	
