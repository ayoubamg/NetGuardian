# netguardian.py
from scapy.all import sniff, ARP
import time
from datetime import datetime

LOG_FILE = "alerts/alert_log.txt"

def log_alert(message):
    with open(LOG_FILE, "a") as log:
        log.write(f"[{datetime.now()}] {message}\n")
    print(f"[ALERT] {message}")

def detect_arp_spoof(pkt):
    if pkt.haslayer(ARP) and pkt[ARP].op == 2:
        real_mac = pkt.hwsrc
        claimed_ip = pkt.psrc
        log_alert(f"ARP Spoofing detected! IP {claimed_ip} claims MAC {real_mac}")

def start_detection():
    print("[*] NetGuardian running... Listening for suspicious ARP packets.")
    sniff(filter="arp", prn=detect_arp_spoof, store=0)

if __name__ == "__main__":
    start_detection()
