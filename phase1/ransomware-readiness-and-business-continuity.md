# Checklist: The Ransomware Readiness & Recovery Plan

For a small business, a ransomware attack isn't just a tech problem—it can be a financial catastrophe.  This checklist, based on **CIS Control 10**, is designed to ensure your business can **survive and recover** from a worst‑case scenario without paying a ransom.

## Phase 1: Proactive Hardening (Making Your Business a Tough Target)

- [ ] **Automate OS & Application Patching:** Are all computers set to automatically update their operating system (Windows/macOS) and web browsers?  Attackers exploit old software; keeping everything up‑to‑date closes the door.
- [ ] **Restrict Administrative Privileges:** Are you and your employees operating as *standard* users for daily work, not *administrators*?  Limiting privileges contains an attack and prevents malware from taking over the whole system.
- [ ] **Secure Your Email Gateway:** Is your email system configured to scan for and block malicious attachments and links *before* they reach your inbox?  This is your #1 defense against phishing, the primary entry point for ransomware.

*Why this matters:* Ransomware often enters through unpatched software, phishing emails and over‑privileged accounts.  Automating updates closes known vulnerabilities before attackers can exploit them.  Running as a standard user limits what malware can modify even if it runs.  A secure email gateway acts as a filter, stopping malicious messages from landing in inboxes in the first place.

## Phase 2: The Ultimate Safety Net (The “Survive Anything” Backup Strategy)

This is the most critical phase.  A working backup is the difference between a bad day and a dead business.

- [ ] **Implement the 3‑2‑1 Backup Rule:** Do you have **3** copies of your essential data on **2** different types of media, with **1** of those copies stored **offsite** (e.g., in the cloud or at a different physical location)?
- [ ] **Ensure Backup Immutability/Offline Status:** Is your offsite backup “immutable” or “offline”?  This means a hacker who has compromised your network cannot also delete or encrypt your backups.  Many cloud backup services offer this.
- [ ] **Schedule and Verify Backup Tests:** Have you successfully restored a test file from your backup within the last 90 days?  An untested backup is not a real backup.

```
                    Data Backup Strategy (3‑2‑1)

      +------------+         +------------+          +--------------+
      |  Original  |  -->  | On‑site copy |  -->  |  Off‑site copy |
      +------------+         +------------+          +--------------+
        (3 copies)               (2 media)                (1 off‑site)
```

*Why this matters:* Ransomware’s power lies in its ability to encrypt or destroy data.  With properly structured backups—multiple copies, diverse media and an offsite, immutable copy—an attacker cannot hold your business hostage.  Regularly testing restores ensures your backups work when you need them.

## Phase 3: “In Case of Emergency” Plan (Don't Panic – Execute)

- [ ] **Create an Incident Contact List:** Do you have a printed or offline list with the contact information for your IT support, a cybersecurity incident response firm and your cyber‑insurance provider?
- [ ] **Know the First Move:** Has everyone been instructed that the first step when ransomware is suspected is to immediately **disconnect the computer from the network** (unplug the ethernet cable or turn off Wi‑Fi)?  This prevents it from spreading to other computers and your backups.

*Why this matters:* Panic and confusion during an attack waste precious time.  Having an offline list of contacts prevents you from relying on potentially compromised systems.  Quickly isolating the infected system limits the blast radius and protects your backups and other machines.

---

## Example Scenario: The Coffee Shop Comptroller

Imagine a small coffee shop with three computers—one for point‑of‑sale, one for accounting and one personal laptop used by the owner.  The owner receives an email that appears to be from a supplier with an invoice attached.  Curious, they open the attachment.  Within minutes, the screen locks and a ransom note appears.

Because the business followed the checklist above:

* Their email system flagged the suspicious message, but the owner overrode the warning.  Training would have reminded them to verify attachments.
* Automatic updates were enabled, so the malware exploited no known vulnerabilities.  However, the owner ran as a local administrator, allowing the ransomware to encrypt files.
* Nightly backups were configured following the 3‑2‑1 rule.  The accounting data lived on a NAS device, with an immutable cloud copy.  The ransomware encrypted the local POS computer but could not reach the offsite backup.
* The owner consulted the incident contact list and called their IT support.  They immediately disconnected the infected machine, wiped it and restored from the previous night’s backup.  No ransom was paid and operations resumed within hours.

This scenario illustrates the difference between inconvenience and catastrophe.  A layered defense combined with tested backups and a simple response plan makes ransomware a recoverable event rather than a business‑ending disaster.