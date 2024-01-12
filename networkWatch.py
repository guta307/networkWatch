import subprocess
import os
import time
import requests
from decouple import config

IP_NETWORK = config('IP_NETWORK')
IP_DEVICE = config('IP_DEVICE').split(',') # split the IP_DEVICE string into a list of IP addresses
connected_ips = [] # Initialize connected IP addresses list
disconnected_times = {} # Initialize a dictionary to store disconnected times for each IP

while True:
    for ip in IP_DEVICE:
        if ip not in connected_ips: # Discover the device only if it has not been discovered yet
            proc = subprocess.Popen(["ping", "-c", "1", ip], stdout=subprocess.PIPE)
            # Use -c 1 option to send only one ping packet
            # Get the output of the ping command
            output = proc.communicate()[0].decode('utf-8')

            # Check if the device is connected
            if "1 received" in output:
                print(f"{ip} discovered in the network")

                # Perform different actions based on which IP is connected
                if ip == '192.168.0.34':
                    url = 'https://www.virtualsmarthome.xyz/url_routine_trigger/'
                    headers = {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
                    }

                    response = requests.get(url, headers=headers)
                    print(response.status_code)
                    print(response.text)
                    time.sleep(10)
                if ip == '192.168.0.75':
                    url = 'https://www.virtualsmarthome.xyz/url_routine_trigger'
                    headers = {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
                    }

                    response = requests.get(url, headers=headers)
                    print(response.status_code)
                    print(response.text)
                    time.sleep(10)
                if ip == '192.168.0.78':
                    url = 'https://www.virtualsmarthome.xyz/url_routine_trigger'
                    headers = {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
                    }

                    response = requests.get(url, headers=headers)
                    print(response.status_code)
                    print(response.text)
                    time.sleep(10)
                if ip == '192.168.0.84':
                    url = 'https://www.virtualsmarthome.xyz/url_routine_trigger'
                    headers = {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
                    }

                    response = requests.get(url, headers=headers)
                    print(response.status_code)
                    print(response.text)
                    time.sleep(10)
                # Add the IP to the connected IP addresses list
                connected_ips.append(ip)
        else: # IP has already been discovered
            proc = subprocess.Popen(["ping", "-c", "1", ip], stdout=subprocess.PIPE)
            # Use -c 1 option to send only one ping packet

            # Get the output of the ping command
            output = proc.communicate()[0].decode('utf-8')
            
            # Check if the device is connected
            if "1 received" in output:
                if ip not in connected_ips: # IP has just connected
                    print(f"{ip} connected to the network")

                    # Perform different actions based on which IP is connected
                    
                    # Add the IP to the connected IP addresses list
                    connected_ips.append(ip)
                disconnected_times[ip] = None
            else:
                if ip in connected_ips: # IP has just disconnected
                    print(f"{ip} disconnected from the network")
                    if disconnected_times[ip] is None: # Only update the disconnected time if it is None
                        disconnected_times[ip] = time.time()
                    # Remove IP addresses that have been disconnected for more than 5 seconds
                    
                    if time.time() - disconnected_times[ip] > 10800 and ip in ['192.168.0.75','192.168.0.84']:
                        print(f"Removing {ip} from connected IP addresses list")
                        connected_ips.remove(ip)
                        del disconnected_times[ip]

                    if time.time() - disconnected_times[ip] > 30 and ip in connected_ips and ip not in ['192.168.0.75','192.168.0.84']:
                        print(f"Removing {ip} from connected IP addresses list")
                        connected_ips.remove(ip)
                        del disconnected_times[ip]

