import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'}

player_info = {
    'ranking': [],
    'name': [],
    'profile': [],
    'position': [],
    'age': [],
    'nationality': [],
    'flag': [],
    'club': [],
    'club_logo': [],
    'market_value': [],
}

def get_data():
    for page in range(4):
        url = f'https://www.transfermarkt.com/spieler-statistik/wertvollstespieler/marktwertetop?ajax=yw1&page={page + 1}'

        r = requests.get(url, headers=headers)
        print(r.status_code)

        soup = BeautifulSoup(r.text, 'html.parser')  # r.text -> r.content

        player_list = soup.find_all('tr', {'class': ['odd', 'even']})

        for player in player_list:
            columns = player.find_all('td')

            player_info['ranking'].append(columns[0].text)
            player_info['name'].append(columns[3].text)
            player_info['profile'].append(columns[1].img['src'])
            player_info['position'].append(columns[4].text)
            player_info['age'].append(columns[5].text)
            player_info['nationality'].append(columns[6].img['title'])
            player_info['flag'].append(columns[6].img['src'])
            player_info['club'].append(columns[7].img['alt'])
            player_info['club_logo'].append(columns[7].img['src'])
            player_info['market_value'].append(columns[8].b.text)

            time.sleep(1)

    return player_info

    # df = pd.DataFrame(player_info)

    # export csv file
    # df.to_csv('data/transfermarket100.csv', index=False)