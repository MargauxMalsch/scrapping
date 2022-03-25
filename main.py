import requests
from bs4 import BeautifulSoup
import pandas as pd
import requests_cache
import xlrd

requests_cache.install_cache('demo_cache')

def get_page(url):
    page = requests.get(url).text
    return BeautifulSoup(page, 'html.parser')


def get_stats(page_data):
    data_stats = []
    array = []

    titre = page_data.find('h2').text
    data_stats.append(titre)

# avec une boucle for on récupere dans le grand tableau les tableaux avec la donnée
    table = page_data.find('tbody')
    for row in table.find_all('tr'):
        player = {
            'joueur': {
                'nom': row.find('th', {"data-stat": "player"}).text,
                'nation': row.find('td', {"data-stat": "nationality"}).text,
                'pos': row.find('td', {"data-stat": "position"}).text,
                'age': row.find('td', {"data-stat": "age"}).text,
            },
            'tempsDeJeu': {
                'mj': row.find('td', {"data-stat": "games"}).text,
                'titulaire': row.find('td', {"data-stat": "games_starts"}).text,
                'min': row.find('td', {"data-stat": "minutes"}).text,
                '90': row.find('td', {"data-stat": "minutes_90s"}).text,
            },
            'performance': {
                'buts': row.find('td', {"data-stat": "goals"}).text,
                'pd': row.find('td', {"data-stat": "assists"}).text,
                'b-penm': row.find('td', {"data-stat": "goals_pens"}).text,
                'penm': row.find('td', {"data-stat": "pens_made"}).text,
                'pent': row.find('td', {"data-stat": "pens_att"}).text,
                'cj': row.find('td', {"data-stat": "cards_yellow"}).text,
                'cr': row.find('td', {"data-stat": "cards_red"}).text,
            },
            'par90Minutes-1': {
                'buts': row.find('td', {"data-stat": "goals_per90"}).text,
                'pd': row.find('td', {"data-stat": "assists_per90"}).text,
                'b+pd': row.find('td', {"data-stat": "goals_assists_per90"}).text,
                'b-penm': row.find('td', {"data-stat": "goals_pens_per90"}).text,
                'b+pd-penm': row.find('td', {"data-stat": "goals_assists_pens_per90"}).text,
            },
            'attendu': {
                'xg': row.find('td', {"data-stat": "xg"}).text,
                'npxg': row.find('td', {"data-stat": "npxg"}).text,
                'xa': row.find('td', {"data-stat": "xa"}).text,
                'npgxg+xa': row.find('td', {"data-stat": "npxg_xa"}).text,
            },
            'par90Minutes-2': {
                'xg': row.find('td', {"data-stat": "xg_per90"}).text,
                'xa': row.find('td', {"data-stat": "xa_per90"}).text,
                'xg+xa': row.find('td', {"data-stat": "xg_xa_per90"}).text,
                'npxg': row.find('td', {"data-stat": "npxg_per90"}).text,
                'npxg+xa': row.find('td', {"data-stat": "npxg_xa_per90"}).text,
            },
        }
        array.append(player)
    data_stats.append(array)
    return data_stats




if __name__ == "__main__":
    path = r'https://fbref.com/fr/equipes/53a2f082/Statistiques-Real-Madrid'
    page_data = get_page(path)

    data_stats = get_stats(page_data)

    data_to_export = []
    data_to_export.append(data_stats)


    #print(pd.DataFrame(data_export).to_string())

    print(data_to_export)

## j'ai cru que ça allait me faire un excel des résultats mais je dois pas comprendre la doc
    #data_export = xlrd.open_workbook("resultats.xlsx")
    #data_export.save()
