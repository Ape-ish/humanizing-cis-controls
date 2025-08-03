# Account Management

> **CIS Control 5** – “Account Management” – ensures that the right people have the right access to the right systems, and no more.

This outline introduces the principles of account management and access control.  A full version will cover practical steps for creating, maintaining and auditing accounts across your environment.

## Why Account Management Matters

Compromised accounts are a leading cause of data breaches.  Weak passwords, unused accounts and excessive privileges give attackers an easy foothold.  Effective account management reduces this risk by enforcing good password hygiene, limiting access and monitoring activity.

## Outline

1. **Principles of Least Privilege**
   - Grant users only the access they need to do their job.
   - Regularly review and adjust privileges as roles change.
2. **Password Hygiene and Multi‑Factor Authentication**
   - Enforce strong password policies (length, complexity and reuse).
   - Promote password managers for individuals and teams.
   - Enable MFA wherever possible and discuss implementation options (SMS, TOTP, hardware tokens).
3. **Lifecycle Management**
   - Onboarding: create accounts, assign roles, communicate expectations.
   - Offboarding: disable accounts promptly when users leave or change roles.
   - Periodic audits of active accounts and privileges.
4. **Service and System Accounts**
   - Differentiating human and non‑human (service) accounts.
   - Securing API keys and tokens.
   - Rotating credentials for service accounts and documenting dependencies.
5. **Monitoring and Alerting**
   - Detecting abnormal login attempts and access patterns.
   - Integrating logs into a SIEM or centralized logging solution.

More details and hands‑on guides will be added soon, including sample policies and scripts for managing accounts efficiently and securely.