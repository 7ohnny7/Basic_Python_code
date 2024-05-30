import ipaddress

def get_ip_addresses_from_subnet(cidr):
    ip_network = ipaddress.IPv4Network(cidr)
    ip_addresses = [str(ip) for ip in ip_network]
    return ip_addresses

# Example usage:
subnet_cidr = "172.16.0.0/27"
all_ips = get_ip_addresses_from_subnet(subnet_cidr)
print(all_ips)
