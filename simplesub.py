#!/usr/bin/env python3
"""
SimpleSub - Simple Subdomain Enumerator - crt.sh + DNS brute force (small wordlist)
Usage: python3 simplesub.py example.com
"""
import sys
import requests
import dns.resolver

def crtsh_subdomains(domain):
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    try:
        r = requests.get(url, timeout=12)
        r.raise_for_status()
        data = r.json()
        names = set()
        for item in data:
            name = item.get("name_value")
            if name:
                for n in name.splitlines():
                    names.add(n.strip().lower())
        return names
    except Exception as e:
        print(f"[!] crt.sh error: {e}")
        return set()

def dns_check(subdomain):
    try:
        answers = dns.resolver.resolve(subdomain, "A")
        return True
    except Exception:
        return False

def dns_bruteforce(domain, wordlist_path="wordlists/small-subdomains.txt"):
    discovered = set()
    try:
        with open(wordlist_path, 'r') as f:
            for line in f:
                prefix = line.strip()
                if not prefix:
                    continue
                sub = f"{prefix}.{domain}"
                if dns_check(sub):
                    discovered.add(sub)
    except FileNotFoundError:
        print("[!] Wordlist not found.")
    return discovered

def main(domain):
    results = set()
    print(f"[+] Querying crt.sh for {domain} ...")
    results |= crtsh_subdomains(domain)
    print(f"[+] Running DNS brute-force from wordlist ...")
    results |= dns_bruteforce(domain)
    if not results:
        print("[+] No subdomains found.")
    else:
        for s in sorted(results):
            print(s)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 simplesub.py <domain>")
        sys.exit(1)
    main(sys.argv[1])
