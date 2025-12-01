# ArpSpoofy
ARP spoofing tool that poisons the ARP cache of a victim and a router to create a man-in-the-middle position and restores ARP tables on exit.

arpSpoofy is a small ARP spoofing tool written in Python with scapy.
It sends forged ARP replies to both a victim and the default gateway in order
to put the attacker machine in the middle of their communication (MITM).
When you stop the script (e.g. with CTRL+C), it attempts to restore the
original ARP entries.

⚠️ Offensive tool – use strictly for authorized lab practice and penetration
testing with written permission.

Features

Performs ARP poisoning between:

A victim host

The router / default gateway

Automatically discovers victim and router MAC addresses with ARP

Periodically sends spoofed ARP replies in a loop

Best-effort ARP table restoration when the script is interrupted

Requirements

Python 3

scapy

Root/administrator privileges

Correct network interface configured inside the script, for example:

conf.iface = "eth0"


Install:

pip install scapy


Usage
sudo python3 arpSpoofy.py <victim_ip> <router_ip>

Example:

sudo python3 arpSpoofy.py 192.168.1.50 192.168.1.1


Disclaimer

This script is for ethical hacking training and understanding ARP spoofing.
Never use it on production or third-party networks without explicit, legal
authorization.
