#!/usr/bin/env python3
import os, sys, time, requests, json
from colorama import init, Fore, Style
import pyfiglet

init(autoreset=True)

def banner():
    os.system("clear")
    print(Fore.CYAN + pyfiglet.figlet_format("OSINT-X") + Style.RESET_ALL)
    print(Fore.MAGENTA + "    Advanced OSINT Tool for Termux".center(50))
    print(Fore.YELLOW + "           Created by VIRUS-S85".center(50))
    print(Fore.CYAN + "═" * 55)

def username_tracker():
    user = input(Fore.GREEN + "\n[+] Username → " + Fore.WHITE)
    print(Fore.YELLOW + "Scanning 50+ sites...\n")
    try:
        r = requests.get(f"https://api.sherlock-project.xyz/search/{user}")
        data = r.json()
        found = 0
        for site, info in data.items():
            if info['status'] == 'found':
                print(Fore.GREEN + f"[✔] {site}: {info['url']}")
                found += 1
            else:
                print(Fore.RED + f"[✘] {site}")
        print(Fore.CYAN + f"\nTotal Found: {found} sites\n")
    except:
        print(Fore.RED + "Sherlock API down or no internet!")

def email_breach():
    email = input(Fore.GREEN + "\n[+] Email → " + Fore.WHITE)
    print(Fore.YELLOW + "Checking breaches...\n")
    url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
    headers = {'User-Agent': 'OSINT-X'}
    try:
        r = requests.get(url, headers=headers, timeout=10)
        if r.status_code == 200:
            print(Fore.RED + "[!] BREACHED!\n")
            for breach in r.json():
                print(Fore.RED + f" → {breach['Name']} ({breach['BreachDate']})")
        else:
            print(Fore.GREEN + "[✔] No breach found! Safe.")
    except:
        print(Fore.RED + "Rate limited or error!")

def phone_info():
    phone = input(Fore.GREEN + "\n[+] Phone (with country code) → " + Fore.WHITE)
    try:
        r = requests.get(f"http://apilayer.net/api/validate?access_key=YOUR_KEY&number={phone}")
        print(Fore.RED + "Need NumVerify API key (free at numverify.com)")
    except:
        print(Fore.YELLOW + "Phone info coming soon...")

def ip_tracker():
    ip = input(Fore.GREEN + "\n[+] IP → " + Fore.WHITE)
    try:
        r = requests.get(f"http://ip-api.com/json/{ip}").json()
        print(Fore.CYAN + f"\nCountry : {r['country']} ({r['countryCode']})")
        print(Fore.CYAN + f"Region  : {r['regionName']}")
        print(Fore.CYAN + f"City    : {r['city']}")
        print(Fore.CYAN + f"ISP     : {r['isp']}")
        print(Fore.CYAN + f"Lat,Lon : {r['lat']}, {r['lon']}\n")
    except:
        print(Fore.RED + "Invalid IP or no internet!")

def domain_whois():
    domain = input(Fore.GREEN + "\n[+] Domain → " + Fore.WHITE)
    try:
        r = requests.get(f"https://api.whoisfreak.com/v1/whois?domain={domain}&apikey=free")
        print(Fore.YELLOW + "WHOIS coming soon with free API...")
    except:
        print(Fore.RED + "Service down")

# মেনু লুপ (এটা সবশেষে থাকবে)
    while True:
        banner()
        print(Fore.WHITE + """
[1] Username Tracker         [5] Domain WHOIS
[2] Email Breach Checker     [6] Subdomain Finder
[3] Phone Number Info        [7] Google Dork
[4] IP Tracker               [8] Instagram Analyzer

[99] Exit
""")
        choice = input(Fore.CYAN + "Choose → " + Fore.WHITE).strip()

        if choice == "1":
            username_tracker()
        elif choice == "2":
            email_breach()
        elif choice == "3":
            phone_info()
        elif choice == "4":
            ip_tracker()
        elif choice == "5":
            domain_whois()
        elif choice == "99":
            print(Fore.RED + "\nStay Ethical! ❤️ VIRUS-S85")
            exit()
        else:
            print(Fore.YELLOW + "Coming Soon in v2.0!")

        input(Fore.MAGENTA + "\nPress Enter to continue..." + Fore.RESET)
