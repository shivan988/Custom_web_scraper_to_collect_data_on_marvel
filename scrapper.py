import json
import time
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

# ---------------------------------- basic of scrapping --------------------------------------
# page = urlopen("https://weimergeeks.com/examples/scraping/example1.html")
# soup = BeautifulSoup(page, 'html.parser')
# ps = soup.find_all('td', class_='city')
# print(ps)
# for p in ps:
#     print(p.text)


# ------------------------------------ function used for scrapping ironman suits details------------------------
def ironman_suits():
    armour = {}
    suits = urlopen("https://marvelcinematicuniverse.fandom.com/wiki/Category:Iron_Man_Armors")
    soup1 = BeautifulSoup(suits, 'html.parser')
    suit_data = soup1.find_all('li', class_="category-page__member")
    new_suit_data = suit_data[2:-1]
    # print(new_suit_data)
    for d in new_suit_data:
        s = d.text.strip().split(":")[1]
        # time.sleep(2)
        # print("\n", s)

        suit_name = s.split(" ")
        print(suit_name)
        capabilities = urlopen(f"https://marvelcinematicuniverse.fandom.com/wiki/Iron_Man_Armor:_{suit_name[1]}_{suit_name[2]}")
        soup2 = BeautifulSoup(capabilities, 'html.parser')
        cap_data = soup2.find('div', class_='quote-left')
        try:
            cap_data2 = cap_data.find_next_sibling('p')
        except AttributeError:
            print("no data found")
        else:
            try:
                cap_data3 = cap_data2.find_next_sibling('ul')
            except AttributeError:
                print('yet to add data')
            else:
                try:
                    cap_data4 = cap_data3.find_all("li")
                except AttributeError:
                    print("yet to be shown")
        # print(len(cap_data))
                else:
                    for data in cap_data4:
                        # print(data.text.strip())
                        # d = data.text.strip()
                        armour[s] = [dd.text.strip() for dd in cap_data4]
                        with open("database/ironman_suits_data.json", "w") as f:
                            json.dump(armour, f, indent=4)


# ------------------------------------ function used for scrapping marvel movies by phases ------------------------
def marvel_movies_by_phase():
    marvel_movies = {}
    marvel_phase_page = requests.get("https://marvelcinematicuniverse.fandom.com/wiki/Category:Movies")
    soup = BeautifulSoup(marvel_phase_page.content, 'html.parser')
    marvel_phase_list = soup.find_all('li', class_='category-page__member')
    for phase in marvel_phase_list[:-4]:
        find_phase = phase.text.strip().split(":")[1].split(" ")
        print()
        print(phase.text.strip().split(":")[1])
        phase_name = phase.text.strip().split(":")[1]
        current_phase = requests.get(f'https://marvelcinematicuniverse.fandom.com/wiki/Category:{find_phase[0]}_{find_phase[1]}_{find_phase[2]}')
        soup1 = BeautifulSoup(current_phase.content, 'html.parser')
        phase_data = soup1.find_all('figcaption', class_= 'category-page__trending-page-title')
        for data in phase_data:
            print(data.text)
            movies = data.text
            marvel_movies[phase_name] = [data.text for data in phase_data]
            with open('database/marvel_movies.json', 'w') as f:
                json.dump(marvel_movies, f, indent=4)


# ------------------------------------ function used for scrapping marvel series ------------------------
def marvel_series():
    marvel_tv_series = {}
    marvel_tv_series_page = requests.get('https://marvelcinematicuniverse.fandom.com/wiki/Category:TV_Series')
    soup = BeautifulSoup(marvel_tv_series_page.content, 'html.parser')
    marvel_tv_series_list = soup.find_all('li', class_='category-page__member')
    letters = requests.get('https://marvelcinematicuniverse.fandom.com/wiki/Category:TV_Series')
    soup2 = BeautifulSoup(letters.content, 'html.parser')
    letters_list = soup2.find_all('div', class_='category-page__first-char')
    for series in marvel_tv_series_list:
        for letter in letters_list:
            # print(letter.text)
            marvel_tv_series[letter.text.strip()] = [series.text.strip() for series in marvel_tv_series_list if series.text.strip()[0].upper() == letter.text.strip()]
            with open('database/marvel_tv_series.json', 'w') as f:
                json.dump(marvel_tv_series, f, indent=4)


# ------------------------------------ function used for scrapping marvel universe characters ------------------------
def marvel_characters():
    characters = {}
    marvel_character_page = requests.get('https://en.wikipedia.org/wiki/List_of_Ultimate_Marvel_characters')
    soup = BeautifulSoup(marvel_character_page.content, 'html.parser')

    marvel_character_list = soup.find_all('div', class_='mw-heading mw-heading2')
    for header in marvel_character_list:
        alphabet = header.text.split('[')[0]
        ul = header.find_next_sibling(['ul'])
        lis = ul.find_all('li')
        for i in lis:
            # print()
            print(i.text)
            characters[alphabet] = [c.text for c in lis]
            with open('database/characters.json', 'w') as f:
                json.dump(characters, f, indent=4)


marvel_movies_by_phase()
ironman_suits()
marvel_series()
marvel_characters()
