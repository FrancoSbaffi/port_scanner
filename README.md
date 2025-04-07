# Advanced Port Scanner

---

## Overview

The Advanced Port Scanner is a Python-based network scanning tool designed to check the status of commonly used ports on a given IP address. It uses multi-threading to speed up the scanning process and only checks important ports, making it ideal for quick security assessments and network diagnostics.

## Features

- **Multi-threaded Scanning:** Uses threads to scan multiple ports concurrently for faster results.
- **Targeted Port List:** Scans a predefined list of important ports commonly associated with network services such as FTP, SSH, HTTP, HTTPS, and more.
- **Customizable:** Easy to modify if you wish to change the port range or adjust the timeout settings.
- **User-friendly:** Simple command-line interface that prompts the user to input an IP address and displays results directly in the terminal.

## Requirements

- **Python 3:** Make sure Python 3 is installed on your system. You can download it from [python.org/downloads](https://www.python.org/downloads/).

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/FrancoSbaffi/port_scanner.git
   ```

2. **Navigate to the project directory:**
    ```bash
   cd port_scanner
   ```
    
3. Ensure Python is installed and added to your PATH.

---

### Usage

1. **Run the Script:**
   Open a terminal or PowerShell, navigate to the project directory, and run the following command:
   ```bash
   python port_scanner.py
   ```
   If your system requires Python 3 explicitly, use:
   ```bash
   python3 port_scanner.py
   ```

2. **Input the IP Address:**
   When prompted, enter the IP address you want to scan. For example:
   ```bash
   Enter the IP to scan: Write ur IP
   ```

3. **View Results:**
   The script will display a list of open ports along with their corresponding service names
   ```bash
   Starting port scan on UR IP...

   Port 22 (SSH) open
   Port 80 (HTTP) open
   Port 443 (HTTPS) open

   Scan completed.

   ```

---

### Disclaimer
This tool is intended for educational purposes and basic network diagnostics. Ensure you have proper authorization before scanning any network or IP address. I´m not responsible for any misuse of this tool.
