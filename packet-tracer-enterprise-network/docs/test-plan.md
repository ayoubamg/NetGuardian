# Validation and Test Plan

Run these checks after building the topology in Cisco Packet Tracer. Record actual results and add screenshots only after performing each test.

## Layer 2 checks
- [ ] show vlan brief lists VLANs 10, 20, 30, 40, and 99.
- [ ] show interfaces trunk confirms the router-facing trunk and allowed VLANs.
- [ ] Each PC switch port is assigned to the expected access VLAN.

## Layer 3 and DHCP checks
- [ ] show ip interface brief shows router subinterfaces up/up.
- [ ] All PCs receive an address in the correct subnet through DHCP.
- [ ] Each PC can ping its own default gateway.
- [ ] Admin-PC can ping IT-PC after inter-VLAN routing is configured.
- [ ] Switch management IP 192.168.99.2 is reachable from an authorized test host in VLAN 99.

## Guest isolation checks
- [ ] Guest-PC can ping 192.168.40.1.
- [ ] Guest-PC cannot reach hosts in internal private networks (for example, a test host in VLAN 10).
- [ ] A non-Guest PC can reach permitted internal VLANs.
- [ ] show access-lists shows matching counters after tests.

## Evidence to capture
1. Full topology view in Packet Tracer.
2. VLAN table from show vlan brief.
3. Trunk status from show interfaces trunk.
4. DHCP address on each PC.
5. Successful authorized inter-VLAN ping.
6. Failed Guest-to-internal ping showing the ACL working.

Do not mark a test as passed until you have run it in Packet Tracer. Save the topology as packet-tracer-enterprise-network.pkt and place genuine screenshots in a screenshots/ folder.
