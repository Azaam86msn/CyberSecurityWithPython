import socket

def check_port(ip, port):
    try:
        # Create a TCP socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)  # Set a timeout of 5 seconds for the connection attempt

        # Attempt to connect to the specified IP address and port
        result = s.connect_ex((ip, port))
        
        if result == 0:
            print(f"Port {port} is open on {ip}.")
        else:
            print(f"Port {port} is closed on {ip}.")
    
    except socket.gaierror:
        print("Invalid IP address.")
    except ValueError:
        print("Invalid port number. Please enter a number between 1 and 65535.")
    except socket.timeout:
        print("Connection timed out. The server may be down or unresponsive.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        s.close()  # Close the socket to free up resources

# Take user input for IP address and port number with basic validation
try:
    ip = input("Enter the IP address: ")
    port = int(input("Enter the port number (1-65535): "))

    # Ensure the port number is within the valid range for TCP/UDP ports
    if 1 <= port <= 65535:
        check_port(ip, port)
    else:
        print("Invalid port number. Please enter a number between 1 and 65535.")
except ValueError:
    print("Invalid input. Please enter a valid IP address and port number.")
