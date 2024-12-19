import requests
import json
import time
from colorama import Fore, Style, init
init()
def display_banner():
    print(Fore.CYAN + Style.BRIGHT + '''
:::    ::: :::   ::: :::    :::      ::::::::::: ::::::::::     :::     ::::    ::::       
:+:    :+: :+:   :+: :+:    :+:          :+:     :+:          :+: :+:   +:+:+: :+:+:+      
+:+    +:+  +:+ +:+   +:+  +:+           +:+     +:+         +:+   +:+  +:+ +:+:+ +:+      
+#++:++#++   +#++:     +#++:+            +#+     +#++:++#   +#++:++#++: +#+  +:+  +#+      
+#+    +#+    +#+     +#+  +#+           +#+     +#+        +#+     +#+ +#+       +#+      
#+#    #+#    #+#    #+#    #+#          #+#     #+#        #+#     #+# #+#       #+#      
###    ###    ###    ###    ###          ###     ########## ###     ### ###       ###      
''' + Style.RESET_ALL)
def loading_animation():
    for i in range(3):
        print(Fore.YELLOW + "Loading" + "." * (i + 1), end="\r")
        time.sleep(0.5)
    print(Style.RESET_ALL, end="\r")
display_banner()

while True:
    try:
        player_id = int(input(Fore.GREEN + "Enter UID: " + Style.RESET_ALL))
        loading_animation()

        url = f"https://ff.garena.com/api/antihack/check_banned?lang=en&uid={player_id}"
        headers = {
            'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
            'Accept': "application/json, text/plain, */*",
            'authority': "ff.garena.com",
            'accept-language': "en-GB,en-US;q=0.9,en;q=0.8",
            'referer': "https://ff.garena.com/en/support/",
            'sec-ch-ua': "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\"",
            'sec-ch-ua-mobile': "?1",
            'sec-ch-ua-platform': "\"Android\"",
            'sec-fetch-dest': "empty",
            'sec-fetch-mode': "cors",
            'sec-fetch-site': "same-origin",
            'x-requested-with': "B6FksShzIgjfrYImLpTsadjS86sddhFH",
            'Cookie': "_ga_8RFDT0P8N9=GS1.1.1706295767.2.0.1706295767.0.0.0; apple_state_key=8236785ac31b11ee960a621594e13693; datadome=bbC6XTzUAS0pXgvEs7u",
        }
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            result = response.json()
            is_banned = result.get('data', {}).get('is_banned', 0)
            period = result.get('data', {}).get('period', 0)

            if is_banned == 1:
                print(Fore.RED + f"🚫 Player ID: {player_id} is BANNED!\n⏳ Period: {period} days" + Style.RESET_ALL)
            else:
                print(Fore.GREEN + f"✅ Player ID: {player_id} is NOT BANNED, you are fine!" + Style.RESET_ALL)
        else:
            print(Fore.YELLOW + "Failed to fetch data from the server." + Style.RESET_ALL)        
#############################################
        exit_program = input(Fore.MAGENTA + "Do you want to check another UID? (yes/no): " + Style.RESET_ALL).strip().lower()
        if exit_program == "no":
            print(Fore.CYAN + "Exiting program. Goodbye!" + Style.RESET_ALL)
            break
    except ValueError:
        print(Fore.RED + "Invalid input! Please enter a valid numeric UID." + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"An error occurred: {e}" + Style.RESET_ALL)
    
################©HYX TEAM###################