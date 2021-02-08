#SIMPLE MACRO TO PARSE AND CREATE THE NAT MAPPING DATA FOR PHOENIX FL2000 NAT SWITCH
#IMPORTS IP-ADDRESSES FROM CSV FILE WITH HEADER (THATS WHY IF i > 0)
#2021-01-08

import csv
with open('ip.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    i = 0
    START_WAN_IP_END = 126
    RANGE_ID_START = 124
    WAN_IP_START = "192.168.11."

    spares = 20
    SPARE_IP_ADDRESS_START = "192.168.14."
    for row in spamreader:
        if i > 0:
            print("NAT-Range-ID_" + str(int(RANGE_ID_START + i - 1)) + "=" + str(int(RANGE_ID_START + i - 1)))
            print("NAT-Range-Mask_" + str(int(RANGE_ID_START + i - 1)) + "=" + "32")
            print("NAT-Range_Active_" + str(int(RANGE_ID_START + i - 1)) + "=enabled")
            print("NAT-Start-IP-LAN_" + str(int(RANGE_ID_START + i - 1)) + "=" + ', '.join(row))
            print("NAT-Start-IP-WAN_" + str(int(RANGE_ID_START + i - 1)) + "=" + WAN_IP_START + str(i + START_WAN_IP_END - 1))
        i += 1


with open('ip.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')    
    rows = list(reader)
    lastRow = rows[-1]
    parts = str(lastRow).replace("'", '.').split('.')
    
    for x in range(spares):
        print("NAT-Range-ID_" + str(int(RANGE_ID_START + i + x - 1)) + "=" + str(int(RANGE_ID_START + i + x - 1)))
        print("NAT-Range-Mask_" + str(int(RANGE_ID_START + i + x - 1)) + "=" + "32")
        print("NAT-Range_Active_" + str(int(RANGE_ID_START + i + x - 1)) + "=enabled")
        print("NAT-Start-IP-LAN_" + str(int(RANGE_ID_START + i + x - 1)) + "=" + SPARE_IP_ADDRESS_START + str(int(parts[-2]) + x + 1))
        print("NAT-Start-IP-WAN_" + str(int(RANGE_ID_START + i + x - 1)) + "=" + WAN_IP_START + str(i + x + START_WAN_IP_END - 1))