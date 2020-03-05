from access_points import get_scanner
wifi_scanner = get_scanner()
NetList = wifi_scanner.get_access_points()
print ("Network: PFA-BYOD")
for each in NetList:
    if each.ssid == "PFA-BYOD":
        print ("MAC: ",each.bssid, " signal strength: ", each.quality)
