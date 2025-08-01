# Simple Security Checklist: Malware Defenses

This checklist corresponds to our guide on "Humanizing CIS Control #10: Malware Defenses." These settings will significantly improve your protection against common threats.

## Task 1: Block "Potentially Unwanted Programs" (PUPs)

PUPs are adware, spyware, and annoying toolbars often bundled with "free" software. This setting is frequently off by default. Enabling it is critical.

### For Windows Security / Microsoft Defender:
- [ ] Open **Windows Security**.
- [ ] Go to **App & browser control**.
- [ ] Click **Reputation-based protection settings**.
- [ ] **Turn On** the setting for **"Potentially unwanted app blocking"**.
- [ ] Ensure both checkboxes for "Block apps" and "Block downloads" are ticked.

### For Other Antivirus (Malwarebytes, Norton, Avast, etc.):
- [ ] Open your antivirus program's main settings panel.
- [ ] Look for a tab named "Protection," "Scan Settings," or similar.
- [ ] Find an option related to "Potentially Unwanted Programs (PUPs)" or "Potentially Unwanted Applications (PUAs)."
- [ ] Set the handling of these threats to **Quarantine** or **Block** (not just "Detect" or "Warn").

## Task 2: Enable Ransomware Protection (Windows)

This feature helps protect your most important files from being encrypted and held for ransom.

- [ ] In **Windows Security**, go to **Virus & threat protection**.
- [ ] Find the **"Ransomware protection"** link and click it.
- [ ] Turn **On** the setting for **"Controlled folder access"**.
- [ ] You may need to approve certain legitimate applications to allow them to save to your protected folders (like Documents, Pictures, etc.).

---
*This checklist is for educational purposes. Always ensure you have a complete backup of your important files.*
