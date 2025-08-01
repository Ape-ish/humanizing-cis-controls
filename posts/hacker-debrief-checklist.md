# Hacker Attack Debrief: The Checklist That Stops Attacks Cold

This checklist summarizes the defensive layers that successfully thwarted a simulated hacking attempt on a standard PC, as detailed in our experiment. This is your guide to activating the same protections.

## Mission Critical Finding:
The attack was not stopped by a single tool, but by a **System of Coordinated Defenses**. The most effective attacks assume at least one layer will fail. Your goal is to ensure multiple layers are active.

### Layer 1: Web Threat Protection (The Moat)
This layer blocked the initial phishing attempt by identifying the malicious website.

- **Action:** Ensure browser protection is active.
- [ ] In **Windows Security**, go to **App & browser control** -> **Reputation-based protection settings**.
- [ ] **Turn On** "SmartScreen for Microsoft Edge."
- [ ] **Turn On** "Phishing protection."
- [ ] *For Chrome/Firefox:* Install and enable the official browser extension from your antivirus provider (e.g., Malwarebytes Browser Guard, Norton Safe Web).

### Layer 2: Real-Time Scanning & PUP Blocking (The Gatekeeper)
This layer identified and blocked the trojan horse application (bundled with a "Potentially Unwanted Program") before it could execute.

- **Action:** Verify that real-time scanning and PUP blocking are enabled.
- [ ] In your antivirus settings (e.g., **Windows Security -> Virus & threat protection**), ensure **"Real-time protection"** is **On**.
- [ ] In **App & browser control -> Reputation-based protection settings**, ensure **"Potentially unwanted app blocking"** is **On**. This is the most critical and often-overlooked setting.

### Layer 3: Ransomware Protection (The Vault)
This layer protects your most important files even if a threat gets past the other defenses.

- **Action:** Activate controlled folder access.
- [ ] In **Windows Security -> Virus & threat protection**, find and click **"Ransomware protection."**
- [ ] **Turn On** the setting for **"Controlled folder access."** This will prevent unauthorized apps from changing files in your key folders (Documents, Pictures, etc.).

---
*This debrief is for educational purposes. A multi-layered defense and regular backups are the foundation of personal security.*
