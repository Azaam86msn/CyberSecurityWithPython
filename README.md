# CyberSecurityWithPython

This repository contains a collection of simple, beginner-friendly cybersecurity projects implemented in Python. Each project demonstrates a fundamental concept or tool used in cybersecurity, including network scanning, client-server communication, and banner grabbing.

## Table of Contents
- [Projects](#projects)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Projects

The following projects are included in this repository:

1. **nmapScript** – Uses the `python3-nmap` module to interact with `nmap` and scan networks.
2. **TCP Client** – Basic implementation of a TCP client.
3. **TCP Server** – Basic implementation of a TCP server to interact with the client.
4. **Port Scanner** – Scans for open ports on a specified target.
5. **Banner Grabber** – Retrieves banner information from specified IP addresses and ports.

## Installation

To run these projects, you need to have **Python 3** installed on your system, as well as the necessary modules.

### 1. Install Python 3
If you haven't installed Python 3, you can download it from [Python's official website](https://www.python.org/downloads/).

### 2. Install Required Modules
Install the following Python modules to run the scripts in this repository:

```bash
pip install python3-nmap socket
```

- **python3-nmap**: This module allows interaction with the `nmap` tool through Python scripts.
- **socket**: This is a built-in Python library, but ensure Python 3 is installed correctly to access it.

## Usage

Each project script is self-contained, and instructions for running each script are provided in the file. Below are examples of running some of these projects:

1. **Run the TCP Client**:
   ```bash
   python tcpClient.py
   ```

2. **Run the TCP Server**:
   ```bash
   python tcpServer.py
   ```

3. **Run the Port Scanner**:
   ```bash
   python portScanner.py
   ```

4. **Run the Banner Grabber**:
   ```bash
   python bannerGrabber.py
   ```

5. **Run the nmap Script**:
   ```bash
   python nmapScript.py
   ```

## License

This repository is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

---

