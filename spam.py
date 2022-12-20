import requests
import threading
import os
from colorama import Fore
import json

os.system('cls')
print('Enter number of threads')
threadCount = int(input(Fore.LIGHTMAGENTA_EX+"[>] "+Fore.RESET))
os.system('cls')
with open('config.json') as config_file:config = json.load(config_file)

spamurl = config['url']
message = config['message']

successcount = 0
errors = 0

def main():
    global successcount
    global errors
    headers = {
    'authority': 'www.confessout.com',
    'method': 'GET',
    'path': '/',
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.8',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Brave";v="108"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'sec-gpc': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36'
}
    r = requests.get('https://confessout.com/',headers=headers)
    for cookies in r.cookies:
        if cookies.name == "XSRF-TOKEN":
            xsrf = cookies.value
        elif cookies.name == "laravel_session":
            laravel_session = cookies.value


    headers2 = {
        "authority": "www.confessout.com",
        "method": "POST",
        "path": "/sendMessage",
        "scheme": "https",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.8",
        "cache-control": "max-age=0",
        "content-type": "application/x-www-form-urlencoded",
        "cookie": f'XSRF-TOKEN={xsrf}; laravel_session={laravel_session}',
        "origin": 'https://www.confessout.com',
        'referer': spamurl,
        'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Brave";v="108"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'sec-gpc': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36'
}
    print("[+]Cookie : "+Fore.LIGHTMAGENTA_EX+f'XSRF-TOKEN={xsrf}; laravel_session={laravel_session}'+Fore.RESET)

    def get_token():
        r = requests.get(spamurl,headers=headers2)
        for line in r.text.splitlines():
            if "_token" in line:
                nigga = line.replace('<input type="hidden" name="_token" value=','')
                x = nigga.replace('"','')
                final = x.replace('>','')
                ok = final.replace('            ','')
                print(Fore.LIGHTMAGENTA_EX+"Token : "+ok)
                return ok

    token = get_token()
    name = spamurl.replace("https://www.confessout.com/","").capitalize()
    payload = {
    '_token': token,
    'reciever': name,
    'message': message
}

    response = requests.post('https://www.confessout.com/sendMessage',headers=headers2,data=payload)
    if response.status_code == 200:
        print(Fore.BLUE+"Successfully sent message!")
        successcount += 1
        os.system('title Confessout Spammer - Success: '+str(successcount)+ ' Error: '+str(errors))
    else:
        print(Fore.RED+ "Failed to send!")
        errors += 1
        os.system('title Confessout Spammer - Success: '+str(successcount)+ ' Error: '+str(errors))

def nigga():
    while True:
        main()

threads = []
for i in range(threadCount):
     t = threading.Thread(target=nigga)
     t.start()
     threads.append(t)
for i in range(threadCount):
    threads[i].join()
