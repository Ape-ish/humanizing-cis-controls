# Secure Configuration

> **CIS Control 4** – “Secure Configuration of Enterprise Assets and Software” – aims to reduce risk by hardening systems and eliminating insecure defaults.

This outline lays out the steps to establish and maintain secure configurations for your operating systems, applications and network devices.

## Outline

1. **Establish Baseline Configurations**
   - Use vendor and industry benchmarks (e.g., CIS Benchmarks) as starting points.
   - Define separate baselines for servers, workstations and mobile devices.
2. **Implement Configuration Management**
   - Automate deployment using configuration management tools (Ansible, Chef, Group Policy).
   - Track deviations from the baseline.
3. **Harden Common Services**
   - Disable unnecessary services and ports.
   - Enforce secure protocols (e.g., SSH over Telnet, TLS 1.2+).
4. **Monitor and Remediate Drift**
   - Regularly scan for misconfigurations and configuration drift.
   - Document exceptions and compensating controls.
5. **Support Secure Build Pipelines**
   - Embed security checks into infrastructure‑as‑code and CI/CD pipelines.

Later versions will include example baseline templates, links to CIS Benchmark resources and step‑by‑step hardening guides.