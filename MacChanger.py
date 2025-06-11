import subprocess
import optparse
import os
import time
import ValidInputChecker as Vic

def change_mac(interface: str, new_mac: str):

    print(f"MAC Address changer started...")
    print("")

    valid_interfaces = os.listdir('/sys/class/net/')

    if not Vic.is_interface_valid(interface, valid_interfaces):
        print(f"Enter a valid Interface! Valid Interfaces: {valid_interfaces}")
        return
    if not Vic.is_mac_valid(new_mac):
        print(f"Enter a valid MAC Address! MAC Address should be something like this: 00:11:11:11:11:11")
        return

    # Added timer to make it look like it's a hard process
    time.sleep(1)


    print(f"MAC Address changing to {new_mac}...")
    print("")

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

    # Added timer to make it look like it's a hard process
    time.sleep(0.5)

    if not check_if_mac_changed(interface, new_mac):
        print(f"MAC Address cannot be changed!")
        return

    print(f"Changed MAC Address to {new_mac}")

def get_parse_objects() -> tuple[any, any]:
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i", "--interface", dest="interface", help="Interface to change")
    parse_object.add_option("-m", "--mac", dest="mac_to_change", help="New MAC address")

    return parse_object.parse_args()

def check_if_mac_changed(interface: str, new_mac: str) -> bool:
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    split_data = ifconfig_result.split()

    return split_data[split_data.index(b'ether') + 1].decode() == new_mac

(user_input, arguments) = get_parse_objects()
change_mac(user_input.interface, user_input.mac_to_change)