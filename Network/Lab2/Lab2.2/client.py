import sys
from pathlib import Path
import get_info 
import json
import socket

# Add the parent directory to the Python module search path
sys.path.append(str(Path(__file__).parent.parent))

def main():
    # TODO
    # Define the server host and port to connect to
    server_host = " 4.tcp.ngrok.io"
    server_port = 10151
    CP_SERVER_ADDRESS = '161.200.92.6'
    CP_SERVER_PORT = 27006
    # Define your student-id
    message = get_info.extract()
    message["ID"] = "6633235421"
    message["Host"] = server_host
    message["Port"] = server_port
    json_message = json.dumps(message).encode('utf-8')
    
    message = get_info.extract()
    
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((CP_SERVER_ADDRESS, CP_SERVER_PORT))
            client_socket.send(json_message)
            final_response = client_socket.recv(1024).decode('utf-8')
            print(f"[INFO] Received response from CP Server: {final_response}")
    
    except ConnectionRefusedError:
        print("[ERROR] Could not connect to the server. Make sure it is running.")
    except Exception as e:
        print(f"[ERROR] An unexpected error occurred: {e}")
    finally:
        # Close the client socket
        client_socket.close()
        print("[INFO] Connection closed.")
        
if __name__ == '__main__':
    main()
