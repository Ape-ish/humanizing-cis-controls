# Network Infrastructure Management

> **CIS Control 12** – “Network Infrastructure Management” – requires you to design, implement and manage secure networks that resist and contain attacks.

This outline sketches the high‑level steps to build and maintain secure networks.  The final article will provide diagrams, configuration examples and troubleshooting tips.

## Outline

1. **Segment Your Network**
   - Separate sensitive systems from less critical ones (e.g., guest Wi‑Fi vs. internal network).
   - Use VLANs and firewall rules to control traffic flow.
2. **Secure Network Devices**
   - Change default credentials and disable unused services on routers, switches and firewalls.
   - Keep firmware up‑to‑date.
3. **Enforce Traffic Filtering and Monitoring**
   - Implement firewall rules that permit only necessary traffic.
   - Deploy intrusion detection/prevention systems (IDS/IPS).
   - Leverage network flow monitoring to detect anomalies.
4. **Ensure Resilience and Availability**
   - Design redundant network paths and failover configurations.
   - Test recovery procedures for network outages.
5. **Document and Review**
   - Maintain network diagrams and configuration backups.
   - Regularly review rulesets and update them as business needs change.

Upcoming sections will include example firewall policies, segmentation architectures and open‑source network monitoring tools.