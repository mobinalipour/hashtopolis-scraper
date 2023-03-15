import time
from bs4 import BeautifulSoup
import requests


def send_to_telegram(message): #a function for sending telegram message 

    apiToken = bot_token
    chatID = id_chat
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'
    response = requests.post(apiURL, json={'chat_id': chatID, 'text': message})
    print(response.text)


server_ip = str(input("Enter hashtopolis server ip (for example 255.255.255.255) :"))
login_url = f"http://{server_ip}/login.php"
loged_url = f"http://{server_ip}/tasks.php"
rows = int(input("How many task rows you wanna scrap? "))
username = str(input("Enter hashtopolis username : "))
password = str(input("Enter hashtopolis password :"))
bot_token = str(input("Enter your telegram bot token :"))
id_chat = str(input("Enter chat id :"))
time_loop = int(input("How many seconds to wait before sending next a log?"))


payload = {
    'username': username,
    'password': password
}

s = requests.session()
s.post(login_url, data=payload)

while True:
    try:
        r = s.get(loged_url)
        soup = BeautifulSoup(r.text, 'html.parser')
        names = soup.select("tr td:nth-child(2)")[:rows]
        cracks = soup.select("tr td:nth-child(5)")[:rows]
        precentage = soup.select("tr td:nth-child(4)")[:rows]

        new_names = []
        new_percentages = []
        new_cracks = []
        finaal_list = []

        for i in names:
            i = i.text.strip()
            new_names.append(i)

        for p in precentage:
            p = p.text.strip().replace("\n", "").replace(" ", "")
            new_percentages.append(p)

        for c in cracks:
            c = c.text.strip()
            if c == "":
                c = 0
            else:
                c = c
            new_cracks.append(c)

        for i in range(len(new_names)):
            message = f"{new_names[i]} is ({new_percentages[i]}) and has {new_cracks[i]} Cracks !"
            finaal_list.append(message)

        x = "\n"
        x = x.join(finaal_list)
        print(x)
        send_to_telegram(x)


    except Exception as e:
        time.sleep(time_loop)
        continue
    time.sleep(time_loop)