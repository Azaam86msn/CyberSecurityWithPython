#!/usr/bin/python3
import nmap

# Initialize the scanner
scanner = nmap.PortScanner()

print("Welcome! This is a simple Nmap automation tool.")
print("<--------------------------------------------------->")

# Get IP address from user
ip_addr = input("Enter the IP address to scan: ")
print(f"Entered IP address is: {ip_addr}")

# Display scan options
print("""\nPlease select the type of scan you want to run:
                1) SYN ACK scan
                2) UDP scan
                3) Comprehensive scan\n""")

# Get user's choice and validate input
resp = input("Select an option (1, 2, or 3): ")

# Check and perform the selected scan
if resp == '1':
    print("Running SYN ACK scan...")
    print("Nmap version:", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-sS -v')
    print("Scan info:", scanner.scaninfo())
    print("IP status:", scanner[ip_addr].state())
    print("Protocols:", scanner[ip_addr].all_protocols())
    print("Open TCP ports:", list(scanner[ip_addr]['tcp'].keys()))

elif resp == '2':
    print("Running UDP scan...")
    print("Nmap version:", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-sU -v')
    print("Scan info:", scanner.scaninfo())
    print("IP status:", scanner[ip_addr].state())
    print("Protocols:", scanner[ip_addr].all_protocols())
    print("Open UDP ports:", list(scanner[ip_addr]['udp'].keys()))

elif resp == '3':
    print("Running comprehensive scan...")
    print("Nmap version:", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-sS -v -A -sC -sV -O')
    print("Scan info:", scanner.scaninfo())
    print("IP status:", scanner[ip_addr].state())
    print("Protocols:", scanner[ip_addr].all_protocols())
    print("Open TCP ports:", list(scanner[ip_addr]['tcp'].keys()))

else:
    print("Invalid option. Please select 1, 2, or 3.")
