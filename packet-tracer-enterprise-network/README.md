# Enterprise Network Design and Security — Cisco Packet Tracer

A portfolio lab for practicing enterprise networking fundamentals. It separates departments with VLANs, routes traffic between VLANs, provides DHCP addressing, and restricts guest access with an extended ACL.

**Deliverables note:** This repository contains the design, sample configurations, IP plan, and test checklist. The actual Cisco Packet Tracer .pkt file and genuine screenshots must be added after building and testing the topology in Packet Tracer. The configurations are a starting point and may need interface-name adjustments for your device models.

## Project goals
- Segment a small office network with VLANs.
- Configure 802.1Q trunking and inter-VLAN routing (router-on-a-stick).
- Provide DHCP scopes for client VLANs.
- Restrict the Guest VLAN from reaching internal private networks.
- Document a repeatable validation plan.

## Proposed topology
- R1 — router providing inter-VLAN routing and DHCP
- SW1 — Layer 2 access switch
- Admin-PC — VLAN 10
- IT-PC — VLAN 20
- Employee-PC — VLAN 30
- Guest-PC — VLAN 40

R1 connects to SW1 over an 802.1Q trunk. End devices connect to access ports in their assigned VLANs.

## VLAN and IP plan
| VLAN | Name | Subnet | Default gateway |
|---:|---|---|---|
| 10 | ADMIN | 192.168.10.0/24 | 192.168.10.1 |
| 20 | IT | 192.168.20.0/24 | 192.168.20.1 |
| 30 | EMPLOYEES | 192.168.30.0/24 | 192.168.30.1 |
| 40 | GUESTS | 192.168.40.0/24 | 192.168.40.1 |
| 99 | MANAGEMENT | 192.168.99.0/24 | 192.168.99.1 |

## Build steps
1. Add one router, one 2960-style Layer 2 switch, and four PCs in Packet Tracer.
2. Connect R1 G0/0 to SW1 G0/1 (or equivalent ports).
3. Connect PCs to SW1 access ports as described in docs/switch-port-map.md.
4. Apply configs/router-r1.txt and configs/switch-sw1.txt.
5. Set all PCs to DHCP.
6. Run the checks in docs/test-plan.md.
7. Save the finished topology as packet-tracer-enterprise-network.pkt and add real screenshots to a screenshots/ folder.

## Repository layout
- configs/router-r1.txt — router-on-a-stick and DHCP example
- configs/switch-sw1.txt — VLANs, access ports, trunk, and management SVI
- docs/ip-addressing-plan.md — addressing details
- docs/switch-port-map.md — suggested physical port assignments
- docs/test-plan.md — validation checklist
- docs/topology.md — topology overview

## Security notes
The Guest ACL blocks access to the listed internal private networks while allowing other IPv4 traffic. Internet access requires an upstream connection, routing, and possibly NAT; those are outside this basic lab. Test ACLs carefully; this is not a production-ready design.

## Skills demonstrated
Cisco IOS basics, VLAN segmentation, 802.1Q trunking, inter-VLAN routing, DHCP, IPv4 subnetting, ACL fundamentals, troubleshooting, and technical documentation.
