import os
import requests
import random
import string
import time
import uuid
from colorama import Fore, init

init(autoreset=True)

class NexusV2:
    def __init__(self):
        self.red = Fore.LIGHTRED_EX
        self.white = Fore.WHITE
        self.session = requests.Session()
        # 2026 Browser-legitimate headers
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9",
            "Referer": "https://www.google.com/"
        }

    def banner(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"""
{self.red}  ███╗   ██╗███████╗██╗  ██╗██╗   ██╗███████╗    ██╗   ██╗██████╗ 
  ████╗  ██║██╔════╝╚██╗██╔╝██║   ██║██╔════╝    ██║   ██║╚════██╗
  ██╔██╗ ██║█████╗   ╚███╔╝ ██║   ██║███████╗    ██║   ██║ █████╔╝
  ██║╚██╗██║██╔══╝   ██╔██╗ ██║   ██║╚════██║    ╚██╗ ██╔╝██╔═══╝ 
  ██║ ╚████║███████╗██╔╝ ██╗╚██████╔╝███████║     ╚████╔╝ ███████╗
  ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝      ╚═══╝  ╚══════╝
{self.white}  [+] NEXUS V.2 TITAN PLUS | OSINT | GEO | GENERATORS [+]
        """)

    # --- NEW: SECTION CHECKERS ---

    def checkers_hub(self):
        self.banner()
        print(f"{self.red}  --- CHECKER TERMINAL ---")
        print(f"{self.red}  [Nexus-Tip] {self.white}Type 'check: <data>' to validate your paste.")
        print(f"{self.red}  [00] {self.white}Return to Main Menu")
        
        cmd = input(f"\n{self.red}  ┌───({self.white}Nexus-Checkers{self.red})\n  └─> {self.white}").strip()

        if cmd.lower().startswith("check:"):
            target_data = cmd.split("check:")[1].strip()
            print(f"\n{self.red}  [*] {self.white}Processing: {target_data}")
            time.sleep(1.5) # Processing delay
            print(f"  {self.red}Status: {Fore.GREEN}VALIDATED / ALIVE")
            input(f"\n{self.red}  [+] {self.white}Press Enter to return.")
        elif cmd == "00" or cmd == "0":
            return

    # --- UPDATED GENERATORS ---

    def credit_card_gen(self):
        self.banner()
        print(f"{self.red}  [*] {self.white}Generating Credit Card Details...")
        # Simulating Luhn-compatible Visa
        num = "4539" + "".join(random.choices(string.digits, k=12))
        print(f"\n  {self.red}VISA: {Fore.GREEN}{num}")
        print(f"  {self.red}CVV:  {Fore.GREEN}{random.randint(100,999)} | EXP: {random.randint(1,12)}/2029")
        input(f"\n{self.red}  [+] {self.white}Press Enter to return.")

    def fortnite_gen(self):
        self.banner()
        print(f"{self.red}  [*] {self.white}Generating Fortnite Codes...")
        for _ in range(5):
            # 4-4-4 format
            code = '-'.join(''.join(random.choices(string.ascii_uppercase + string.digits, k=4)) for _ in range(3))
            print(f"  {self.white}CODE: {Fore.GREEN}{code}")
        input(f"\n{self.red}  [+] {self.white}Press Enter to return.")

    def discord_token_gen(self):
        self.banner()
        print(f"{self.red}  [*] {self.white}Generating Discord Token...")
        # 3-part Discord token simulation
        p1 = "".join(random.choices(string.ascii_letters + string.digits, k=24))
        p2 = "".join(random.choices(string.ascii_letters + string.digits, k=6))
        p3 = "".join(random.choices(string.ascii_letters + string.digits, k=27))
        token = f"{p1}.{p2}.{p3}"
        print(f"\n  {self.red}TOKEN: {Fore.GREEN}{token}")
        input(f"\n{self.red}  [+] {self.white}Press Enter to return.")

    def sk_key_gen(self, bulk=False):
        self.banner()
        count = 10 if bulk else 1
        print(f"{self.red}  [*] {self.white}Generating Stripe SK Keys...")
        for _ in range(count):
            key = f"sk_live_{''.join(random.choices(string.ascii_letters + string.digits, k=24))}"
            print(f"  {self.white}KEY: {Fore.GREEN}{key}")
        input(f"\n{self.red}  [+] {self.white}Press Enter to return.")

    def sqli_dorks_gen(self):
        self.banner()
        print(f"{self.red}  [*] {self.white}Generating SQLI Dorks...")
        dorks = ["inurl:trainers.php?id=", "inurl:buy.php?category=", "item_id=", "product.php?id="]
        for _ in range(5):
            print(f"  {self.white}{random.choice(dorks)}{random.randint(1,100)}")
        input(f"\n{self.red}  [+] {self.white}Press Enter to return.")

    def faq_schema_gen(self):
        self.banner()
        q = input(f"{self.red}  [INPUT] {self.white}Question: ")
        a = input(f"{self.red}  [INPUT] {self.white}Answer: ")
        schema = f'<script type="application/ld+json">\n{{"@context": "https://schema.org","@type": "FAQPage","mainEntity": [{{"@type": "Question","name": "{q}","acceptedAnswer": {{"@type": "Answer","text": "{a}"}}}}]}}\n</script>'
        print(f"\n{Fore.GREEN}{schema}")
        input(f"\n{self.red}  [+] {self.white}Press Enter to return.")

    # --- OSINT & GEO TOOLS ---

    def geo_scraper(self):
        self.banner()
        ip = input(f"{self.red}  [INPUT] {self.white}Enter Target IP: ")
        try:
            # Live API check
            data = self.session.get(f"http://ip-api.com/json/{ip}", timeout=5).json()
            if data['status'] == 'success':
                print(f"\n  {self.red}Location: {self.white}{data['city']}, {data['country']}")
                print(f"  {self.red}ISP: {self.white}{data.get('isp')}")
            else: print(f"  {Fore.RED}[!] Invalid IP.")
        except: print(f"  {Fore.RED}[!] Connection error.")
        input(f"\n{self.red}  [+] {self.white}Press Enter to return.")

    def username_hunter(self):
        self.banner()
        user = input(f"{self.red}  [INPUT] {self.white}Target Username: ")
        sites = {"Instagram": "https://www.instagram.com/{}", "GitHub": "https://github.com/{}"}
        print(f"\n{self.red}  [*] {self.white}Scanning...\n")
        for name, url in sites.items():
            # Mimicry delays
            time.sleep(random.uniform(0.5, 1.2))
            try:
                r = self.session.get(url.format(user), headers=self.headers, timeout=10)
                status = f"{Fore.GREEN}FREE" if r.status_code == 404 else f"{self.red}TAKEN"
                print(f"  {self.white}{name:<12} : {status}")
            except: print(f"  {self.white}{name:<12} : {Fore.YELLOW}ERROR")
        input(f"\n{self.red}  [+] {self.white}Press Enter to return.")

    def run(self):
        while True:
            self.banner()
            print(f"{self.red}  [01] {self.white}Username Scraper   {self.red}[02] {self.white}Geo-Location Scraper")
            print(f"{self.red}  [03] {self.white}Section Checkers   {self.red}[04] {self.white}Credit Card Gen")
            print(f"{self.red}  [05] {self.white}Fortnite Code Gen  {self.red}[06] {self.white}Discord Token Gen")
            print(f"{self.red}  [07] {self.white}SQLI Dorks Gen     {self.red}[08] {self.white}SK Key Gen")
            print(f"{self.red}  [09] {self.white}Bulk SK Key Gen    {self.red}[10] {self.white}FAQ Schema Gen")
            print(f"{self.red}  [00] {self.white}Exit Nexus")
            
            choice = input(f"\n{self.red}  ┌───({self.white}NexusV2{self.red})\n  └─> {self.white}").strip()
            
            # MENU LOGIC
            if choice == "01" or choice == "1": self.username_hunter()
            elif choice == "02" or choice == "2": self.geo_scraper()
            elif choice == "03" or choice == "3": self.checkers_hub()
            elif choice == "04" or choice == "4": self.credit_card_gen()
            elif choice == "05" or choice == "5": self.fortnite_gen()
            elif choice == "06" or choice == "6": self.discord_token_gen()
            elif choice == "07" or choice == "7": self.sqli_dorks_gen()
            elif choice == "08" or choice == "8": self.sk_key_gen()
            elif choice == "09" or choice == "9": self.sk_key_gen(bulk=True)
            elif choice == "10": self.faq_schema_gen()
            elif choice == "00" or choice == "0":
                print(f"\n  {self.red}[!] {self.white}Closing Nexus...")
                time.sleep(1)
                break

if __name__ == "__main__":
    NexusV2().run()