import socket
import threading

important_ports = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    139: "NetBIOS",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    993: "IMAPS",
    995: "POP3S",
    3389: "RDP",
    8080: "HTTP-Alt"
}

def scan_port(ip, port, service_name):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((ip, port))
        if result == 0:
            print(f"Port {port} ({service_name}) open")
    except Exception as e:
        print(f"Error scanning port {port}: {e}")
    finally:
        s.close()

def main():
    ip = input("Enter the IP to scan: ")
    threads = []
    print(f"\nStarting port scan on {ip}...\n")
    for port, service_name in important_ports.items():
        thread = threading.Thread(target=scan_port, args=(ip, port, service_name))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    print("\nScan completed.")

if __name__ == "__main__":
    main()
