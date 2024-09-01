#!/usr/bin/env python3
import sys
import subprocess
import re
if len(sys.argv)>1:
    print(sys.argv[1])
    try:
        ping_result = subprocess.run(['ping', '-c',sys.argv[2],sys.argv[1]],text=True, capture_output=True, check=True)
    except subprocess.CalledProcessError:
        print("packet loss :(")
        exit(1)
    #print(ping_result.stdout)
    print(ping_result.stderr)
    ping_result_split = ping_result.stdout.split("\n")
    print(ping_result_split[1])
    
    match2 = re.search('(\d+) packets transmitted, (\d+) received', ping_result.stdout)
    if match2:
        packet_transmitted = match2.group(1)
        packet_received = match2.group(2)
    
        match3 = re.search('(\d+) bytes from (\d+\.\d+\.\d+\.\d+): icmp_seq=(\d+) ttl=(\d+) time=(\d+\.?\d*) ([mu]?s)',ping_result.stdout)
        ip_address = match3.group(2)

        match = re.search('([\d]*\.[\d]*)/([\d]*\.[\d]*)/([\d]*\.[\d]*)/([\d]*\.[\d]*)', ping_result.stdout)
        ping_min = match.group(1)
        ping_avg = match.group(2)
        ping_max = match.group(3)
    else:
        print("sorry")

    print("Ping output")
    print('ip_address: ' + ip_address, 'packet transmitted: ' + packet_transmitted, 'packet received: ' + packet_received, 'ping_charasteristics: ' + ping_min, ping_avg, ping_max, )
    


else:
    print("need more arguments")
    