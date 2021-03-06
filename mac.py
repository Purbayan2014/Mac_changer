import subprocess
import optparse
import re


def usr_data():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i", "--interface", dest="interface", help="Its for changing the interface !!!")
    parse_object.add_option("-m", "--mac_address", dest="mac_address", help="The custom mac-address that you want ")

    return parse_object.parse_args()


def mac_changer_proc(inter, mac_custom):
    subprocess.run(["ifconfig", inter, "down"])
    subprocess.run(["ifconfig", inter, "hw", "ether", mac_custom])
    subprocess.run(["ifconfig", inter, "up"])


def display_proc(inter):
    ifconfig = subprocess.check_output(["ifconfig", inter])
    new_mac = re.search(br"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig)

    if new_mac:
        return new_mac.group(0)
    else:
        return None


print("Mac-changer initiated ................")
(usr_input, args) = usr_data()
mac_changer_proc(usr_input.interface, usr_input.mac_address)
finalize = display_proc(usr_input.interface).decode()

print("\n\n------------------ Results --------------------")
if finalize == usr_input.mac_address:
    print(usr_input.interface + " address updated to " + usr_input.mac_address)
    #print("Success")
else:
    print("Invalid Address Provided")
