import requests, re, csv
from bs4 import BeautifulSoup

season_lengths = {1: 6, 2: 22, 3: 23, 4: 14, 5: 26, 6: 24, 7: 24, 8: 24, 9: 23}

with open('office.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Season Number', 'Episode Number', 'Episode Title', 'Character', 'Quote'])
    
    for season_num in season_lengths:
        for episode_num in range(1, season_lengths[season_num] + 1):
            slug = f'no{season_num}-{episode_num:02}.php'
            url = 'http://www.officequotes.net/' + slug

            res = requests.get(url)
            soup = BeautifulSoup(res.text, 'lxml')

            for link in soup.select('a'):
                if link.get('href') == slug:
                    episode_title = link.text

            scenes = soup.select('div.quote')
            for scene in scenes:
                scene = scene.getText()
                quotes = re.findall(r'([A-Za-z ]+): (.+)', scene)
                for quote in quotes: 
                    character = quote[0]
                    phrase = quote[1]
                    csv_writer.writerow([season_num, episode_num, episode_title, character, phrase])
