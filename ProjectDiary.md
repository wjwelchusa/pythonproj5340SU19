# PROJECT DIARY

## 6/25/2019 Activities
1. Provided initial project submission.

Rationale for project:

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

Wireless Utility Practice

- Practiced repeatedly with the following commands to:
- Examined how a card is placed in monitor mode.
- Viewed the locally available AP's and STA's.
- Selected an AP for disassociation and reassociation.
- Captured the IV and associated traffic.
- Used a password cracking tool to attempt cracking the PSK for the respective AP.

_______________________________________

Commands:
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

## 7/11/2019 Activities
- Learned README Use and Format
- Completed Udacity tutorial on README. [https://classroom.udacity.com/courses/ud777]
- Reformatted documentation files using markdown.

