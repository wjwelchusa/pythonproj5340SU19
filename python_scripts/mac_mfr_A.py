#!/usr/bin/python3


# Joe Welch 29 Jul 2019
# Edited program to find mfr for given MAC
# Packet handler is being developed to provide additional info
# regarding the field names and field content for captured packets
#
# Revision/config info
# Python 3 
#
# Initial file developed from http://macvendors.co/api/
# Python 3 Example of how to use https://macvendors.co to lookup vendor from mac address
# Very little change
#
# TODOs
# 1. rework this file as a function, to receive the MAC as a parameter and return the mfr information
# 2. determine which values should be returned for use/display



import urllib.request as urllib2
import json
import codecs



## ________________ Main program _________________
for x in range(5):
    print("MAC addresses are helpful.")

print ("Content-Type: text/html\n")
#API base url,you can also use https if you need
url = "http://macvendors.co/api/" # Very create structure used to pair URL, with the MAC to create a search query string to workk through the API
#Mac address to lookup vendor from
mac_address = "BC:92:6B:A0:00:01"

request = urllib2.Request(url+mac_address, headers={'User-Agent' : "API Browser"}) 
response = urllib2.urlopen( request )
reader = codecs.getreader("utf-8")  #codec modules used to extract info in str, not utf-8 format
obj = json.load(reader(response))  # extract using json format, keyed off of OUI in the provided MAC

#Print company name
print (obj['result']['company']+"<br/>");

#print company address
print (obj['result']['address']);
