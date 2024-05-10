import socket
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def send_syslog(message, host='192.168.10.114', port=12667):
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        # Send the message to the syslog server
        sock.sendto(message.encode(), (host, port))
        logging.info("Message sent to syslog server successfully: %s", message)
    except Exception as e:
        logging.error("Error sending message to syslog server: %s", e)
    finally:
        # Close the socket
        sock.close()

# Example usage
message = "<14>1 python-script: This is a test message from Python syslog sender"
send_syslog(message)
print("Message sent to syslog server:", message)

