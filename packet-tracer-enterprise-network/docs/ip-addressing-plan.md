# IP Addressing Plan

All VLANs use a /24 subnet (255.255.255.0). The first usable address is reserved as the router gateway. DHCP excludes addresses .1 through .20 for infrastructure and static assignments.

| VLAN ID | VLAN name | Network | Gateway | Expected DHCP range |
|---:|---|---|---|---|
| 10 | ADMIN | 192.168.10.0/24 | 192.168.10.1 | 192.168.10.21–192.168.10.254 |
| 20 | IT | 192.168.20.0/24 | 192.168.20.1 | 192.168.20.21–192.168.20.254 |
| 30 | EMPLOYEES | 192.168.30.0/24 | 192.168.30.1 | 192.168.30.21–192.168.30.254 |
| 40 | GUESTS | 192.168.40.0/24 | 192.168.40.1 | 192.168.40.21–192.168.40.254 |
| 99 | MANAGEMENT | 192.168.99.0/24 | 192.168.99.1 | 192.168.99.21–192.168.99.254 |

Switch management address: 192.168.99.2/24 on VLAN 99.

## Design rationale
- Department VLANs separate broadcast domains.
- Router subinterfaces provide each VLAN's default gateway.
- DHCP reduces manual endpoint configuration.
- The Guest ACL denies RFC1918 private address ranges and permits other IPv4 destinations. Internet access still requires an upstream network and is not included.
