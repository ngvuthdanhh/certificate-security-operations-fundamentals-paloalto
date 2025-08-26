#!/usr/bin/env python3
"""
Demo: Enrich alert with geo/IP info
"""

import ipaddress

def enrich_ip(ip):
    # Dummy enrichment
    return {"ip": ip, "country": "US", "malicious_score": 42}

if __name__ == "__main__":
    alerts = ["192.168.1.10", "10.0.0.5"]
    for ip in alerts:
        enriched = enrich_ip(ip)
        print(enriched)
