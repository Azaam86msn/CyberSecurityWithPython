import socket

def get_banner(ip, port):
    try:
        # Create a TCP socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)  # Set a timeout of 5 seconds for the connection

        # Attempt to connect to the specified IP and port
        s.connect((ip, port))
        
        # Receive data from the server
        banner = s.recv(1024)
        print("Banner:", banner.decode('utf-8', errors='ignore'))
    
    except socket.timeout:
        print("Connection timed out.")
    except ConnectionRefusedError:
        print("Connection was refused by the target.")
    except socket.gaierror:
        print("Invalid IP address.")
    except ValueError:
        print("Invalid port number.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        s.close()

# Take user input for IP address and port number with basic validation
try:
    ip = input("Enter the IP address: ")
    port = int(input("Enter the port number: "))
    get_banner(ip, port)
except ValueError:
    print("Invalid port number. Please enter a numeric value.")
