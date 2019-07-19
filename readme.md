# PROJECT DIARY
## TODO:
1. I need to find useful documentation for referring to the data elements at each layer accessible with scapy.
2. Existing radio card is capturing traffic only in 2.5 Ghz range. This is due to driver or chipset. Investigate and correct if possible. Otherwise, continue for project using this range. Subsequent application to other ranges should be extensible, given scapy library.
3. Purchased new air card with 802.11ac capability. Card is not currently detecting signals. Update and configure driver for the aircard.
4. Separate the MAC addresses into AP MAC and STA MAC. AP MAC may be identified for wireless disassociation and PSK pwd cracking, join the network with common URL/IP address and vendor passwords, to exploit AP.
5. Investigate extraction of SSID's not in beacon mode.
6. STA MAC can be investigated to discern path and vulnerability status.
7. When searching for AP's, clients will search for the SSID's in their listing (what is this called?). It may be possible to determine where a STA has been by pairing their client probes with the Wigle of skyhook database and GeoIP. Print out the location and location by date (if possible).
8. As the ambient WLAN signals are sampled, connect various radio cards and antennae to determine if additional signals are detected. Also, take note of received power as a roungh function of received/antenna selaction


## 6/25/2019 Activities
1. Provided initial project submission.

### Rationale for project:

1. Wireless access is becoming dominant.
2. here are many wireless signals used: 802.11, 802.15, BlueTooth, Cellular, ZigBee, etc.
3. Common characteristics are sought to determine vulnerabilities and hardening techniques.
4. Selected spectrum for this project is 802.11 due to availability of wireless cards with necessary capabilities. Selected card should be used to permit monitor mode andpacket injection.

## 6/27-28/2019 Activities:
1. Ordered and received wireless card with monitor mode and packet injection capability.
Wireless card type: SimpleWiFi Adapter Card Model N124-700, with chipset Ralink RT3070L, 802.11 b/g/n.
2. This card was seleted based upon multiple recommendations and successful demonstrations. This particular card does not address 802.11 ac, which can be explored at a later time.

## 6/30/2019 - 7/1/2019  Activities
Worked with libraries and internet documentation to discern which information about 802.11 signals may be discerned, captured and analyzed with existing utilities. There are many libraries available, of varying use and maturity. My effort will be to implement some of the capabilities via Python mudules, initially  with Scapy module.

## 7/2/2019-7/5-2019 Activities

### Wireless Utility Practice

- Practiced repeatedly with the following commands to:
- Examined how a card is placed in monitor mode.
- Viewed the locally available AP's and STA's.
- Selected an AP for disassociation and reassociation.
- Captured the IV and associated traffic.
- Used a password cracking tool to attempt cracking the PSK for the respective AP.

_______________________________________

### Commands:
- ifconfig -a  			# look for wlan adapter
- lsmod 			# look for drivers for LAN card RT2800XXX drivers
- ifconfig wlan0 up 		# turn on WLAN, check for up in ifconfig -a WLAN adapter
- airmon-ng 			# status check
- airmon-ng check kill 		# disable peer processes which may interfere w/ mon mode
- airmon-ng start wlan0 	# places WLAN in monitor mode. ifconfig -a 					 #
- airodump-ng wlan0mon 		# see Access Points around you
- airodump-ng			# lists all options
- airmon-ng stop wlan0mon	# To return to managed mode (remember the managed service processes may not be running)

Notes:
- Terminal commands in Kali do not exactly match those presented in BT video.
- Once wlan0 is placed into monitor mode, refer to it as wlan0mon card.
- Card can work in one band, one channel at a time. My card is b/g/n .
- Placing card in monitor mode disables internet access.
- Use airodump-ng  before looking for beacon broadcast in Wireshark.

Injecting beacon frames:
- Using mdk3 currently as the utility to inject packets (beacon fales AP, DDOS, etc.)
- After placing card into monitor mode
- mdk3 wlan0mon b -n P0wned
- ** Many features in mdk3 - spend time here
- 802.11 AP beacon flooding supports a misassociation attack


Disassociating and capturing IV for decrypting:
- Solid example: https://www.youtube.com/watch?v=zAWcu3NQLME
- https://www.youtube.com/watch?v=ewBSTJJppmI
- Review these videos: https://www.youtube.com/channel/UC_MuHQPbf3EatJc7M6nDTlQ
- After setup above, and determinationrmination of channels and SSIDs

-  #airodump -c 4 -w /root/dump_info.txt --bssid B0:7F:B9:DC:2E:BB wlan0mon

________________________________________

## 7/12/2019 - 7/13/2019 Activities
- Wrote small Scapy scripts to familiarize myself with the capabilities and synyax.
- Followed several tutorials regarding Scapy.
- Worked the aricrack-ng workflow and defined idealized capabilities for my project scripts.


## Notes for research, practice, exploration and tool development.
### Sources:
1. Ramachandran, V. (15 Jul 2019) "Scripting Wi-Fi Pentesting Tools in Python", retrieved from https://www.pentesteracademy.com/course?id=14
2. Scapy Project Documentation, (10 Jul 2019) "Packet crafting for Python2 and Python3", retrieved from https://scapy.net/
3. Welcome to Scapy’s documentation!, (10 Jul 2019) "Scapy", retrieved from https://scapy.readthedocs.io/en/latest/
4. Wood, M. (8 Jul 2019), "Scapy", retrieved from "https://thepacketgeek.com/"

### Options to exploit with available toolsets:
1. Existing utilities and tools (aircrack-ng, pineapple, etc.)
2. Raw Sockets
3. Scapy library approach - built upon Raw Sockets
4. Scapy supports many protocols, we will use utilities associated with 802.11.

### Initial effort to develop workflow for using Scapy in interactive mode:
1. Place attached wireless card in monitor mode
airmon-ng check kill
airmon-ng start wlan0mon (or as req'd for specific card)
airodump wlan0mon (turn on shortly to ensure packet capture is working)

2. Launch scapy for monitor mode
Scapy cannot do channel hopping. It must be done with airmon-ng
```
#scapy
>>>conf   ( lists config settings for scapy)
>>>conf.iface=wlan0mon (set iface for scapy)
>>>wifiPkts = sniff(count=1)
>>>wifiPkts (will list contents)
>>>wifiPkts.summary()   (lists summary of sniff session)
>>>wifiPkts.nsummary() (lists summary with a line number)
>>>wifiPkts.hexdump() (lists summary in hex)
```

### Workflow for using Scapy in scripting mode
Potential uses:
1. packet processor
2. parse, analyze, act
3. callback function

## 15 Jul 2019 Activities

### Workflow for today
1. Scan local STA's for promiscuous mode
2. getmacbyip may be useful

### Understanding layers in Scapy
1. Information regarding the data types and structure of scapy layers is revealed with the ls command. Ex:
```
>>>ls(RadioTap)
>>>ls(Dot11)
>>>ls(Dot11Beacon)
>>>ls(Dot11Ely)
```

2. The content (not structure) of a packet can be extracted with the ls command and then the packet variable, NOT field name.
To work your way up through the layers:
```
>>>pkt.payload  then
>>>.pkt.payload.payload...
```

3. You can reverse the payload, with the .undelayer command
.payload goes up
.underlayer goes down

4. Using a loop, it is possible to iterate up or down the scapy stack.
```
>>>temp = pkt
>>>while temp:
>>>...    print(temp.name)
>>>...    temp = temp.payload
```

5. It is possible to extract the SSID from the beacon layer, using this syntax:
pkt.payload.payload.payload.info   (remember .name is the name of the protocol, .info provides the contents)
6. Can also get the similar info, using the command .getlayer
7. It is also possible to check for layers, using the .haslayer(xx) info

### Individual script development to learn more about Scapy and to build Scapy tools.
1. Created basic PacketHandler script to sniff and print summaries of captured packets (filename: packethandler.py)

## 7/16/2019 Activities
1. Completed first two scripts to monitor ambient wireless trafffic and sniff data from the signals. The first script was for geeneral capture.
The second script was to extract info and labels from the traffic. (.11 traffic and MAC address)
2. The fields and structure available for extraction are considerable.

## 7/17/2019 Activities
### Investigated documentation for scapy Dot11 functions and data extracts
1. Details provided by scapy are significant and detailed.
2. Extracted output of all supported layers to: dot11_layers.txt
3. Extracted all actions available with scapy to all_actions.txt
4. Many of the remainings cripts will depend upon this documentation for data extract, classification and processing.

## 7/18/2019 Activities
### Building scripts to extract data from Dot11 signals and to identify SSID's
1.  Examine in more depth the extraction of additional fields and values from the Dot11 scapy layer.
2. The data is referenced through tagged parameters, in the format : type, length, value. Typically the SSID is the first tagged parameter. Do not always assume this only. Reference otherwise.
3. It will help to determine if the WLAN signal is encrypted. This is extracted from RSN field.

## 7/19/2009 Activities
### Building scripts to extract data from Dot11 signals and to identify SSID's. Also, conducted short survey of effectiveness of more powerful antenna type.
1. The radio card used for the majority of scapy scripting work in this project is the Alpha N124-700, with a simple vertical antenna. (See image in images directory.) The number of APs detected in the area varied between 8-12. For a short period today, a more powerful antenna, the COM-24015PN 15db antenna was connected.  (See image in images directory.) During this period the number of received signals doubled. Also, the new antenna is directional, and if rotated on a schedule would collect even more signals. The utility of the antenna/card pairing is important is extends the application of the implemented scapy scripts.
2. Today's scripts focus on client probes. A client probe is the precursor step to locating a listed SSID in the client OS and beginning an association. The sequencing of the clients through this SSID list will provide information regarding travel and prior location if associated with WLAN databases in Wigle of Skyhook. This is not an explicit part of the project, but would be a growth direction.
3. clientfinder.py was implemented, with no detections. This may be due to all clients in view having already been associated or an error. I will let this run over time to see if a detection is made. There is more detail on this in clientfinder.py script.
4. Initial research effort is complete for the project:
	A. scapy was installed and configured
	B. several radio cards were used and compared
	C. many scapy scripts were developed, tested and debugged, to determine if scapy coould extract useful data fields from the WLAN signals
	D. the next focus will be the actions taken once the wireless signal extracts are in hand
		D1. Locate an API or web scraping script to pair MAC OUI manufacturer with the OUIs detected
		D2. Locate an API or webscraping script to identify MACs with outstanding patches or exploits
		D3. Write the results or scapy scripts to a data file or container and complete D1, D2 


