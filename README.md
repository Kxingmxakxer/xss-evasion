# XSS WAF Evasion Toolkit

This project demonstrates how Cross-Site Scripting (XSS) payloads can be obfuscated to bypass Web Application Firewalls (WAFs) using encoding, evasion, and injection techniques. It includes a Python-based payload generator and a vulnerable HTML testbed to simulate real-world testing scenarios.

---

## Table of Contents
- About the Project
- Key Concepts
- Features
- Evasion Techniques Used
- Installation & Usage
- Testing
- Sample Outputs
- Legal Disclaimer
- Credits

---

## About the Project

Web Application Firewalls (WAFs) aim to block malicious inputs like XSS attacks using various filters. However, attackers can use encoding or transformation techniques to bypass WAF restrictions. This project simulates such behavior to show how encoded payloads can go undetected by basic WAFs.

---

## Key Concepts

- **XSS (Cross-Site Scripting)**: A vulnerability that allows attackers to inject malicious scripts into web pages viewed by others.
- **WAF (Web Application Firewall)**: A security solution designed to filter and monitor HTTP traffic to and from a web application.
- **Character-Based Filtering**: WAFs often rely on detecting dangerous characters like `<`, `>`, `"`, `'`, `(`, `)`.

---

## Features

- Generate advanced XSS payload variants
- Test payloads on a sample vulnerable HTML page
- Use encoding methods such as:
  - URL encoding
  - HTML entity encoding
  - JavaScript `String.fromCharCode()` injection
  - Obfuscated script injections

---

## Evasion Techniques Used

| Technique | Description |
|----------|-------------|
| URL Encoding | Encodes dangerous characters like `<`, `>` using `%3C`, `%3E` |
| HTML Entity Encoding | Converts characters to `&#60;`, `&#62;`, etc. |
| Hex Encoding | Uses `\x3C` format to evade detection |
| String.fromCharCode() | Reconstructs payload using JavaScript character codes |
| Null Byte Injection | Bypasses filters by breaking keywords like `scr\0ipt` |
| Keyword Obfuscation | Breaks or alters blacklisted terms like `scr<script>ipt` |

---

## Installation & Usage

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/XSS-WAF-Evasion.git
cd XSS-WAF-Evasion
