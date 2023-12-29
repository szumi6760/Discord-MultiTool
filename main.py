import os, requests, random, json, time, string, discord
from colorama import Fore, Style

def Center(var:str, space:int=None): # From Pycenter
    if not space:
        space = (os.get_terminal_size().columns - len(var.splitlines()[int(len(var.splitlines())/2)])) / 2
  
    return "\n".join((" " * int(space)) + var for var in var.splitlines()) 

def proxy_count():
    proxies_list = 0
    with open("config/proxies.txt", "r") as f:
        proxies = [line.strip() for line in f]
    for _ in proxies:
        proxies_list += 1
            
    return int(proxies_list)

class Console():
    def Options(self):
        option = int(input(Center(f"Console: ")))
        if option == 1:
            MultiTool().Sniper()
        elif option == 2:
            MultiTool().Generator()
        elif option == 3:
            MultiTool().Checker()
        else:
            print(Center(f"Invalid option."))
    
    def Menu(self):
        os.system(f"cls && title [DMT] Discord Multi Tool ^| test" if os.name == "nt" else "clear")
        print(Center(f"""\n
███╗   ███╗██╗   ██╗██╗  ████████╗██╗    ████████╗ ██████╗  ██████╗ ██╗     
████╗ ████║██║   ██║██║  ╚══██╔══╝██║    ╚══██╔══╝██╔═══██╗██╔═══██╗██║ 
██╔████╔██║██║   ██║██║     ██║   ██║       ██║   ██║   ██║██║   ██║██║
██║╚██╔╝██║██║   ██║██║     ██║   ██║       ██║   ██║   ██║██║   ██║██║     
██║ ╚═╝ ██║╚██████╔╝███████╗██║   ██║       ██║   ╚██████╔╝╚██████╔╝███████╗
╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝   ╚═╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
                                                                             \n                           ~ Discord Multi Tool ~\n                              Creator - \033[4m\0Szumi\033[0m
              """).replace("█", Fore.RED+"█"+Fore.RESET).replace("╗", Style.DIM + Fore.RED+"╗"+ Style.RESET_ALL + Fore.RESET).replace("╔", Style.DIM + Fore.RED + "╔" + Style.RESET_ALL + Fore.RESET).replace("╚", Style.DIM + Fore.RED + "╚" + Style.RESET_ALL + Fore.RESET).replace("═", Style.DIM + Fore.RED + "═" + Style.RESET_ALL + Fore.RESET).replace("╝", Style.DIM + Fore.RED + "╝" + Style.RESET_ALL + Fore.RESET).replace("║", Style.DIM + Fore.RED + "║" + Style.RESET_ALL + Fore.RESET))
        print(Center(f"""Options:
╭──────────────────────────────────╮
│                                  │
│       [1] Nitro Sniper           │
│       [2] Nitro Generator        │
│       [3] Nitro Checker          │
│          (with proxies)          │
│                                  │
╰──────────────────────────────────╯
""").replace("╭", Style.DIM + Fore.YELLOW + "╭" + Style.RESET_ALL + Fore.RESET).replace("│", Style.DIM + Fore.YELLOW + "│" + Style.RESET_ALL + Fore.RESET).replace("─", Style.DIM + Fore.YELLOW + "─" + Style.RESET_ALL + Fore.RESET).replace("╰", Style.DIM + Fore.YELLOW + "╰" + Style.RESET_ALL + Fore.RESET).replace("╯", Style.DIM + Fore.YELLOW + "╯" + Style.RESET_ALL + Fore.RESET).replace("╮", Style.DIM + Fore.YELLOW + "╮" + Style.RESET_ALL + Fore.RESET))
        Console().Options()

class MultiTool():
    def Sniper(self):
        with open("config/config.json") as f:
            cfg = json.load(f)
        token = cfg.get("token")
          
    def Generator(self):
        if not os.path.exists("results"):
            os.makedirs("results")
        amount = int(input(Center(f"Amount: ") + Fore.YELLOW))
        boost = str(input(Fore.RESET + Center(f"Nitro Boost(Y/N): ") + Fore.YELLOW))
        Fore.RESET
        with open("results/codes.txt", "w") as f:
            count = 0
            while count < amount:
                if boost.lower() == "y":
                    code_length = 24
                else:
                    code_length = 16
                code = "".join(random.choice(string.ascii_letters + string.digits) for _ in range(code_length))
                f.write(code + "\n")
                count += 1
            print("\n" + Fore.RESET + Center(f"Generated {Fore.YELLOW + str(amount) + Fore.RESET} codes and saved them in codes.txt!"))
            input("Press ENTER to continue.")
    def Checker(self):
        with open("results/codes.txt", "r") as f:
            codes = [line.strip() for line in f]
            lines = f.readlines()
            
        def load_proxies():
            with open("config/proxies.txt", "r") as f:
                proxies = [line.strip() for line in f]
            return proxies
        proxies = load_proxies()

        with open("config/config.json", "r") as f:
            cfg = json.load(f)
            nitro_claim = str(cfg.get("nitro_claim_checker"))
            proxy_type = str(cfg.get("proxy_type"))

        count = 0
        while count < len(codes):
            code = random.choice(codes)
            try:
                proxy = random.choice(proxies)
                proxies_dict = {proxy_type: f"{proxy_type.lower()}://" + proxy}
                req = requests.get(f"https://discordapp.com/api/v6/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true", proxies=proxies_dict, timeout=15)

                if req.status_code == 200:
                    if nitro_claim.capitalize == True:
                        pass
                    elif nitro_claim.capitalize == False:
                        print(Fore.GREEN + Center(f"[+] {code}") + Fore.RESET)
                        hits = open("results/hits.txt", "w")
                        hits.write(code + "\n")
                    else:
                        pass
                    codes.remove(code)
                elif req.status_code == 404:
                    print(Fore.RED + Center(f"[-] {code}") + Fore.RESET)
                    codes.remove(code)
                elif req.status_code == 429:
                    print(Style.DIM + Fore.YELLOW + Center(f"[?] Ratelimited") + Style.RESET_ALL + Fore.RESET)
                else:
                    print(Fore.YELLOW + Center(f"[?] Retry") + Fore.RESET)
            except Exception as e:
                print(Fore.RED + f"Error occurred: {str(e)}" + Fore.RESET)
                pass
            count += 1
        input("Press ENTER to continue.")
    
if __name__ == "__main__":
    while True:
        Console().Menu()