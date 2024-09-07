import requests
from datetime import datetime, timedelta
import json
import time
import random
import sys
import os
from colorama import Fore, Style, init

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def art():
    print("\033[1;91m" + r""" ______  _               _    
 | ___ \| |             | |   
 | |_/ /| |  __ _   ___ | | __
 | ___ \| | / _` | / __|| |/ /
 | |_/ /| || (_| || (__ |   < 
 \____/ |_| \__,_| \___||_|\_\
""" + "\033[0m" + "\033[1;92m" + r""" ______                                   
 |  _  \                                  
 | | | | _ __   __ _   __ _   ___   _ __  
 | | | || '__| / _` | / _` | / _ \ | '_ \ 
 | |/ / | |   | (_| || (_| || (_) || | | |
 |___/  |_|    \__,_| \__, | \___/ |_| |_|
                       __/ |              
                      |___/               
""" + "\033[0m" + "\033[1;93m" + r"""  _   _               _                
 | | | |             | |               
 | |_| |  __ _   ___ | | __  ___  _ __ 
 |  _  | / _` | / __|| |/ / / _ \| '__|
 | | | || (_| || (__ |   < |  __/| |   
 \_| |_/ \__,_| \___||_|\_\ \___||_| 
""" + "\033[0m\n\033[1;96m---------------------------------------\033[0m\n\033[1;93mScript created by: Black Dragon Hacker\033[0m\n\033[1;92mJoin Telegram: \nhttps://t.me/BlackDragonHacker007\033[0m\n\033[1;91mVisit my GitHub: \nhttps://github.com/BlackDragonHacker\033[0m\n\033[1;96m---------------------------------------\033[0m\n\033[1;38;2;139;69;19;48;2;173;216;230m--------------[Blum Bot]--------------\033[0m\n\033[1;96m---------------------------------------\033[0m")

def get_query_ids_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            query_ids = [line.strip() for line in file.readlines()]
            return query_ids
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return []
    except Exception as e:
        print(f"Error: {e}")
        return []

def save_token(token, file_path):
    try:
        with open(file_path, 'w') as file:
            file.write(token)
    except Exception as e:
        print(f"Error saving token: {e}")

def get_token_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            token = file.readline().strip()
            return token
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def get_new_token(query_id):
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9",
        "content-type": "application/json",
        "origin": "https://telegram.blum.codes",
        "priority": "u=1, i",
        "referer": "https://telegram.blum.codes/"
    }

    data = json.dumps({"query": query_id})
    url = "https://user-domain.blum.codes/api/v1/auth/provider/PROVIDER_TELEGRAM_MINI_APP"

    animation = ["|", "/", "-", "\\"]

    while True:  # Loop indefinitely
        try:
            response = requests.post(url, headers=headers, data=data)
            if response.status_code == 200:
                try:
                    response_json = response.json()
                    token = response_json.get('token', {}).get('refresh', None)
                    if token:
                        return token
                    else:
                        print("Token key not found in response.")
                except json.JSONDecodeError as e:
                    print(f"JSON Decode Error: {e}")
                    print(f"Response content: {response.text}")
            elif response.status_code == 520:
                for i in range(len(animation)):  # Loop through animation frames
                    sys.stdout.write(f"\rWait Token Fetched {animation[i]}")
                    sys.stdout.flush()
                    time.sleep(0.5)
                sys.stdout.write("\r" + " " * 20 + "\r")  # Clear line
            else:
                print(f"Unexpected status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")

        time.sleep(5)

def get_balance(token, account_no):
    url = "https://game-domain.blum.codes/api/v1/user/balance"
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9",
        "authorization": f"Bearer {token}",
        "sec-ch-ua": "\"Chromium\";v=\"111\", \"Not(A:Brand\";v=\"8\"",
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": "\"Android\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data_balance = response.json()

        available_balance = data_balance.get("availableBalance", "N/A")
        play_passes = data_balance.get("playPasses", "N/A")        
        is_fast_farming_enabled = data_balance.get("isFastFarmingEnabled", False)
        
        print(f"{Fore.CYAN + Style.BRIGHT}------Account No.{account_no}------")
        print(f"{Fore.GREEN + Style.BRIGHT}Balance: {available_balance}")
        print(f"{Fore.YELLOW + Style.BRIGHT}Total Play Pass: {play_passes}")

        if not is_fast_farming_enabled:
            print(f"{Fore.RED + Style.BRIGHT}Farming not started")

        return data_balance

    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED+ Style.BRIGHT}Request failed: {e}")
        return None

def claim_farming(token):
    url = "https://game-domain.blum.codes/api/v1/farming/claim"
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9",
        "authorization": f"Bearer {token}",
        "sec-ch-ua": "\"Chromium\";v=\"111\", \"Not(A:Brand\";v=\"8\"",
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": "\"Android\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site"
    }
    
    try:
        sys.stdout.write("Claiming farming balance...")
        sys.stdout.flush()
        response = requests.post(url, headers=headers)
        sys.stdout.write('\r' + ' ' * len("Claiming farming balance..."))
        sys.stdout.write('\r')
        data = response.json()
       
        if response.status_code == 425 and data.get("message") == "It's too early to claim":
            print(f"{Fore.RED+ Style.BRIGHT}Farming Already Claimed")
        elif response.status_code == 200:
            print(f"{Fore.GREEN+ Style.BRIGHT}Farming Claimed Successfully")
        else:
            print(f"{Fore.RED+ Style.BRIGHT}Unexpected status code: {response.status_code}")
            print(f"{Fore.RED+ Style.BRIGHT}Response text: {response.text}")
            
    except requests.exceptions.RequestException as req_err:
        print(f"{Fore.RED+ Style.BRIGHT}Request error occurred: {req_err}")

def start_farming(token):
    url_farming = "https://game-domain.blum.codes/api/v1/farming/start"
    url_balance = "https://game-domain.blum.codes/api/v1/user/balance"
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9",
        "authorization": f"Bearer {token}",
        "sec-ch-ua": "\"Chromium\";v=\"111\", \"Not(A:Brand\";v=\"8\"",
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": "\"Android\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site"
    }
    
    try:
        sys.stdout.write("Starting farming...")
        sys.stdout.flush()
        sys.stdout.write('\r' + ' ' * len("Starting farming..."))
        sys.stdout.write('\r')
        
        response1 = requests.post(url_farming, headers=headers)
        response1.raise_for_status()  # Check for errors in the response
        
        data1 = response1.json()
        farming_balance = data1.get("balance", "N/A")
        end_time = data1.get("endTime", None)
        
        if end_time:
            end_time_dt = datetime.fromtimestamp(end_time / 1000.0)
            now = datetime.now()
            remaining_time = end_time_dt - now
            hours, remainder = divmod(remaining_time.total_seconds(), 3600)
            minutes, seconds = divmod(remainder, 60)
            time_str = f"{int(hours)} hours, {int(minutes)} minutes, {int(seconds)} seconds"
            
            if farming_balance == "0":
                print("Farming Started Successfully")
                response2 = requests.get(url_balance, headers=headers)
                response2.raise_for_status()
                data2 = response2.json()
                new_balance = data2.get("availableBalance", "N/A")
                print(f"{Fore.GREEN+ Style.BRIGHT}New Balance: {new_balance}")
            else:
                print(f"{Fore.MAGENTA+ Style.BRIGHT}Farming Balance: {farming_balance}")
            
            print(f"{Fore.CYAN+ Style.BRIGHT}Time Until End: {time_str}")
            return end_time_dt
        else:
            print(f"{Fore.RED+ Style.BRIGHT}No end time returned.")
            return None
        
    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED+ Style.BRIGHT}Request failed: {e}")
        return None

def get_daily_reward(token):
    url = "https://game-domain.blum.codes/api/v1/daily-reward"
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9",
        "authorization": f"Bearer {token}",
        "sec-ch-ua": "\"Chromium\";v=\"111\", \"Not(A:Brand\";v=\"8\"",
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": "\"Android\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site"
    }

    try:
        response = requests.post(url, headers=headers)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
      if response.status_code == 200:
        print(f"{Fore.GREEN+ Style.BRIGHT}Daily Reward Claimed Successfully")
      elif response.status_code == 400:
        print(f"{Fore.RED+ Style.BRIGHT}Daily Reward Already Claimed")
      else:
        print(f"{Fore.RED+ Style.BRIGHT}Response Status Code: {response.status_code}")

def claim_ref(token):
    url = "https://user-domain.blum.codes/api/v1/friends/claim"
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9",
        "authorization": f"Bearer {token}",
        "sec-ch-ua": "\"Chromium\";v=\"111\", \"Not(A:Brand\";v=\"8\"",
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": "\"Android\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site"
    }

    try:
        response = requests.post(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        ref_balance = data.get("claimBalance")
    except requests.exceptions.RequestException as e:
      if response.status_code == 200:
        print(f"{Fore.GREEN+ Style.BRIGHT}Referral Bonus Claimed Successfully")
        print(f"{Fore.GREEN+ Style.BRIGHT}Referral Bonus: {ref_balance}")
      elif response.status_code == 400:
        print(f"{Fore.RED+ Style.BRIGHT}Referral Bonus Already Claimed")
      else:
        print(f"{Fore.RED+ Style.BRIGHT}Response Status Code: {response.status_code}")

def new_balance(token):
    url = "https://game-domain.blum.codes/api/v1/user/balance"
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9",
        "authorization": f"Bearer {token}",
        "sec-ch-ua": "\"Chromium\";v=\"111\", \"Not(A:Brand\";v=\"8\"",
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": "\"Android\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Check for HTTP errors
        data_balance = response.json()

        new_balance = data_balance.get("availableBalance", "N/A")
        play_passes = data_balance.get("playPasses", 0)  # Default to 0 if not found

        return new_balance, play_passes       
    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED + Style.BRIGHT}Request failed: {e}")
        return None, None

def play_game(token):
    url = "https://game-domain.blum.codes/api/v1/game/play"
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9",
        "authorization": f"Bearer {token}",
        "sec-ch-ua": "\"Chromium\";v=\"111\", \"Not(A:Brand\";v=\"8\"",
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": "\"Android\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site"
    }

    try:
        response = requests.post(url, headers=headers)
        response.raise_for_status()  # Raises error for bad status codes
        data = response.json()
        gameid = data.get("gameId")

        if gameid:
            print(f"{Fore.YELLOW + Style.BRIGHT}Game Started....")
            time.sleep(32)
            return gameid
        else:
            print("Game ID not found in the response.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def claim_game(token, gameId):
    url = "https://game-domain.blum.codes/api/v1/game/claim"
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9",
        "authorization": f"Bearer {token}",
        "sec-ch-ua": "\"Chromium\";v=\"111\", \"Not(A:Brand\";v=\"8\"",
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": "\"Android\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site"
    }
    points = random.randint(256, 278)
    
    body = {"gameId": gameId, "points": points}

    try:
        response = requests.post(url, headers=headers, json=body)
        response.raise_for_status()
        if response.status_code == 200:
        	print(f"{Fore.GREEN + Style.BRIGHT}Game Reward Claimed")      	
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def format_timedelta(td):
    total_seconds = int(td.total_seconds())
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours}:{minutes}:{seconds}"

def countdown_timer(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        hours, mins = divmod(mins, 60)
        print(f"{Fore.CYAN + Style.BRIGHT}Wait {hours:02}:{mins:02}:{secs:02}", end='\r')
        time.sleep(1)
        seconds -= 1
    print("Wait 00:00:00          ", end='\r')  # Clear the countdown message

import time

def main():
    while True:
        query_ids = get_query_ids_from_file('data.txt')
        clear_terminal()
        art()

        for index, query_id in enumerate(query_ids):
            if query_id:
                token = get_new_token(query_id)
                if token:
                    token_file = 'token.txt'
                    save_token(token, token_file)
                    get_balance(token, index + 1)
                    claim_farming(token)
                    start_farming(token)
                    claim_ref(token)
                    while True:
                        current_balance, play_passes = new_balance(token)
                        if current_balance is None or play_passes is None:
                            print(f"{Fore.RED + Style.BRIGHT}Failed to retrieve balance or play passes.")
                            break
                        if play_passes > 0:
                            print(f"{Fore.CYAN + Style.BRIGHT}Play Passes Available: {play_passes}")
                            game_id = play_game(token)
                            if game_id:
                                claim_game(token, game_id)
                        else:
                            print(f"{Fore.RED + Style.BRIGHT}Play Pass is 0")
                            break
                    get_daily_reward(token)
                else:
                    print(f"{Fore.RED + Style.BRIGHT}Account No.{index + 1}: Token generation failed.")
            else:
                print(f"{Fore.RED + Style.BRIGHT}Account No.{index + 1}: Query ID not found.")
        
        countdown_timer(1*60*60)
        clear_terminal()
        art()
        
if __name__ == "__main__":
    main()
