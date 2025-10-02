# simplesub

**Simple Python Subdomain Enumerator — lightweight, fast, and easy to use**

---

## Overview
`simplesub` is a **minimal yet powerful** subdomain enumeration tool written in Python.  
Unlike bulky frameworks, it is designed to be **fast, understandable, and flexible** while still performing essential subdomain discovery tasks:

- **Passive discovery** using [crt.sh](https://crt.sh) — find subdomains without touching the target directly.  
- **Active DNS brute-force** using your own wordlists — customizable to your scope.  
- Optional **live host verification** — avoid cluttering results with unreachable hosts.  

`simplesub` outputs results in **plain text** or **JSON**, making them easy to parse, share, or integrate into other tools.

---

## Why `simplesub`?

Most subdomain enumeration tools are either **overly complex**, require heavy dependencies, or generate **too much noise**. `simplesub` is different:

1. **Lightweight** — a single Python script with minimal dependencies.  
2. **Flexible** — use your own wordlists, or even integrate it into larger workflows.  
3. **Reliable** — combines passive and active enumeration with optional host verification.  
4. **Readable output** — clean, simple, and easy to understand at a glance.  

It’s ideal for **students, bug bounty hunters, and pentesters** who want **speed, clarity, and control**.

---

## Installation

```bash
git clone https://github.com/s7a7am/simplesub.git
cd simplesub
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

