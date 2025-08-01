# The "Smarter Than Malware" Protection Checklist

Your **anti‑malware** (often called “antivirus”) is your first line of defense, but it's not your only one.  Malicious software is designed to be sneaky and often relies on tricking you, the user.

Use this checklist to build a multi‑layered defense that makes you a much harder target. This is based on the principles of **CIS Control 10**.

## ✅ Level 1: Supercharge Your Antivirus

- [ ] **Deploy Trusted Anti‑Malware:** Is a trusted anti‑malware program (like Windows Defender or a reputable third‑party tool) installed and active on your computer?
- [ ] **Enable Automatic Updates:** Is your anti‑malware set to update its definitions automatically?  New malware appears daily, so staying up‑to‑date is critical.
- [ ] **Enable Behavior‑Based Detection:** If your software has a “behavior‑based,” “heuristic,” or “real‑time” protection setting, ensure it's enabled.  This helps catch brand‑new threats that don't have a known signature yet.

*Why these matter:*  A trusted anti‑malware engine with up‑to‑date definitions and behavioral detection gives you a fighting chance against both known and unknown threats.  Many modern attacks use “zero‑day” exploits that signature‑based scanners alone cannot catch.

## ✅ Level 2: Lock the Side Doors

- [ ] **Disable USB Autorun:** Have you disabled “Autorun” and “Autoplay” for removable media?  This simple change prevents malware from launching automatically when you plug in an infected USB drive.
- [ ] **Review Browser Extensions:** Have you uninstalled old or unnecessary browser extensions?  These can be a hidden gateway for malware.

*Why these matter:*  USB drives and browser add‑ons are two of the most common ways malware sneaks onto a system.  Disabling autorun stops malicious code from executing without your consent, and pruning browser extensions limits the attack surface of your web browser.

## ✅ Level 3: Fortify Your Internet Connection

- [ ] **Use DNS Filtering:** Have you switched to a DNS filtering service?  It acts like a bouncer for the internet, blocking known malicious websites before they can even load on your computer.  (Free options include Quad9 and Cloudflare for Families.)

*Why this matters:*  DNS filtering stops you from even reaching sites known to host malware or phishing pages.  Combined with a secure browser and healthy skepticism, it dramatically reduces your risk of accidentally downloading something dangerous.