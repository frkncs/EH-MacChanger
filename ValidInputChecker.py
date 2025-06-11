def is_interface_valid(interface: str, valid_interfaces: list) -> bool:
    return interface in valid_interfaces

def is_mac_valid(new_mac: str) -> bool:
    return len(new_mac.split(":")) == 6