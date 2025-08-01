# Email & Web Browser Protections

> **CIS Control 9** – “Email and Web Browser Protections” – focuses on the technologies and habits that prevent malicious content from ever reaching you or executing in your browser.

This outline lays the groundwork for a future deep dive into secure email and browsing practices.  The goal is to highlight key concepts and provide a clear path for expanding this post into a full article.

## Why Email and Browsers Matter

Email and web browsers are the front doors to the internet—and to most cyber attacks.  Phishing emails and drive‑by downloads deliver malware, steal credentials and trick users into revealing sensitive information.  By hardening these entry points, you can block an enormous percentage of threats before they do damage.

## Outline

1. **Understand the Threat Landscape**
   - Common attack vectors: phishing, malicious attachments, embedded scripts and watering‑hole websites.
   - Real‑world examples of email and browser‑based attacks.
2. **Secure Your Email Gateway**
   - Spam and malware filtering at the mail server level.
   - User awareness: recognizing phishing cues and suspicious links.
   - Multi‑factor authentication for email accounts.
3. **Harden Your Browser**
   - Keep browsers and plugins up‑to‑date.
   - Limit or disable insecure plugins (e.g., Flash, Java).
   - Use privacy/security‑focused extensions (e.g., uBlock Origin, HTTPS Everywhere) judiciously.
   - Consider using a separate browser profile or container for high‑risk activities.
4. **Sandbox and Isolation Techniques**
   - Running untrusted email attachments in a virtual machine or cloud sandbox.
   - Using application isolation (e.g., Windows Defender Application Guard) to open untrusted sites.
5. **DNS and Web Filtering**
   - Leveraging DNS filtering (Quad9, Cloudflare for Families) to block malicious domains.
   - Centralized filtering at the network or router level for families or SMBs.
6. **User Training and Habit Building**
   - Encouraging skepticism of unsolicited attachments or links.
   - Recognizing spoofed domains and look‑alike URLs.
   - Reporting suspicious emails to IT/security.

*Stay tuned! In a future update we will expand each section with step‑by‑step guides, recommended tools and checklists.*