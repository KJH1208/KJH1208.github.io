---
title: Network Security Practice Project
summary: A collection of reports from network security exercises using Wireshark, Nmap, firewalls, and more.
type: project
tags:
  - SEC
date: 2024-12-31
draft: false
featured: true
share: false

image:
  filename: security-cover.jpg
  preview_only: false

links:
  - icon: file-archive
    icon_pack: fas
    name: Download Full ZIP
    url: /files/projects/security_reports.zip
---

## Project Overview
This page compiles reports from **network security coursework and individual practice**.  
Topics include packet analysis with Wireshark, Nmap scanning, banner grabbing, SNMP testing, and firewall/DoS experiments.

---

### 📘 Main Practice Topics
- Packet Sniffing & Analysis (Wireshark)
- Various Port Scanning and Evasion Techniques (Nmap SYN/FIN/Fragmentation, etc.)
- Banner Grabbing (FTP/SMTP/SSH/HTTP)
- SNMP Information Gathering Attempts
- Firewall and Network Topology Configuration
- Basic Packet Tracer Setup and Route Verification

---

### 📄 Detailed Exercise Summaries

- **Packet Analysis**  
  Captured and analyzed packets (e.g., with Wireshark) to interpret headers and payloads, understand protocol behavior, communication flow, and identify abnormal traffic.  
  *Learning Points:* Packet structure (TCP/UDP/IPv4/IPv6), packet filtering, and traffic reconstruction.

- **Whois & DNS Investigation**  
  Queried registration data and DNS records (A/AAAA/MX/TXT, etc.) to identify domain ownership and network information.  
  *Learning Points:* DNS operation principles, record types, and reverse lookup techniques.

- **IP Address Tracing (IP Geolocation / Traceroute)**  
  Combined traceroute results with public databases (WHOIS, BGP) to analyze routing paths and estimate source/destination locations.  
  *Learning Points:* Routing and AS concepts, TTL-based tracing, privacy and accuracy limitations.

- **Asset / Service Enumeration**  
  Identified hosts and open services (ports) in a network to understand the attack surface and asset prioritization.  
  *Learning Points:* Nmap scanning options, service banner checking, and asset classification.

- **Sniffing & Spoofing**  
  Practiced traffic capture (sniffing) and sender information forgery (spoofing) to explore authentication bypass or session hijacking potential.  
  *Learning Points:* ARP spoofing, MAC/IP forgery, and the defense role of HTTPS/TLS.

- **Tunneling & TCP Session Hijacking**  
  Experimented with legitimate and unauthorized tunnels (e.g., SSH tunneling) and demonstrated how TCP sessions can be hijacked.  
  *Learning Points:* TCP 3-way handshake, session identifiers, and risks of sequence number manipulation.

- **SSL Sniffing / Man-in-the-Middle (MITM) Attack**  
  Simulated interception of encrypted communication via MITM attacks, and compared mitigation mechanisms such as certificate validation, HSTS, and public key pinning.  
  *Learning Points:* TLS handshake, certificate trust chain, and common mitigation methods.

- **Denial of Service (DoS/DDoS) Simulation**  
  Conducted controlled DoS experiments and simulations to test defensive strategies such as rate limiting and firewall rules.  
  *Learning Points:* Types of attack vectors, traffic control strategies, and importance of monitoring.

- **Firewall Configuration Practice**  
  Designed and applied packet-filtering and stateful firewall rules to block unwanted access, handle exceptions, and log activities.  
  *Learning Points:* Writing ACLs, state tracking, NAT, and port forwarding considerations.
---