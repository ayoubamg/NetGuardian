# Topology Overview

The design uses a router-on-a-stick architecture. One physical router interface carries tagged traffic for each VLAN over an 802.1Q trunk to a Layer 2 switch.

    +---------------------------+
    | R1 - Router               |
    | G0/0 subinterfaces        |
    | VLANs 10/20/30/40/99      |
    +-------------+-------------+
                  |
             802.1Q trunk
                  |
    +-------------+-------------+
    | SW1 - Layer 2 Switch      |
    +--+--------+--------+------+
       |        |        |      |
    VLAN 10  VLAN 20  VLAN 30 VLAN 40
       |        |        |      |
     Admin      IT    Employee Guest
      PC        PC       PC     PC

## Traffic flow
- Each PC receives an address from its VLAN DHCP pool.
- Traffic within a VLAN is switched locally.
- Traffic between VLANs is routed by R1 through the relevant subinterface.
- Traffic originating from VLAN 40 is filtered by the GUEST-IN ACL before routing.
