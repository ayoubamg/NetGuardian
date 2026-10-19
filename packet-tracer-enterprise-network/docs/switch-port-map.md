# Switch Port Map

Use this map when building the lab. Port names may differ by switch model.

| Switch interface | Connected device | Mode | VLAN |
|---|---|---|---:|
| Gi0/1 | R1 Gi0/0 | 802.1Q trunk | 10, 20, 30, 40, 99 |
| Fa0/1 | Admin-PC | Access | 10 |
| Fa0/2 | IT-PC | Access | 20 |
| Fa0/3 | Employee-PC | Access | 30 |
| Fa0/4 | Guest-PC | Access | 40 |

If interface names differ, adjust the configuration. The router-facing port must support trunking.
