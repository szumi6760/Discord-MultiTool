import os, requests, random, json, time, string
from colorama import Fore, Style

def Center(var:str, space:int=None): # From Pycenter
    if not space:
        space = (os.get_terminal_size().columns - len(var.splitlines()[int(len(var.splitlines())/2)])) / 2
  
    return "\n".join((" " * int(space)) + var for var in var.splitlines()) 

def proxy_count():
    proxies_list = 0
    with open("config/proxies.txt", "r") as file:
        proxies = [line.strip() for line in file]
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
                                                                             \n                           ~ Discord Multi Tool ~\n                              Creator by \033[4m\0Szumi\033[0m
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
            config = json.load(f)
        token = config.get("token")
          
    def Generator(self):
        if not os.path.exists("results"):
            os.makedirs("results")
        amount = int(input(Center("Amount: ")))
        boost = str(input(Center(Fore.RESET + "Nitro Boost(Y/N): ")))
        Fore.RESET
        with open("results/codes.txt", "w") as f:
            i = 0
            while i < amount:
                if boost.lower() == "y":
                    code_length = 24
                else:
                    code_length = 16
                code = "".join(random.choice(string.ascii_letters + string.digits) for _ in range(code_length))
                f.write(code + "\n")
                i += 1

    def Checker(self):
        '''
        if not os.path.exists("results/hits.txt"):
            os.path.join("results", "hits.txt")
        '''

if __name__ == "__main__":
    while True:
        Console().Menu()