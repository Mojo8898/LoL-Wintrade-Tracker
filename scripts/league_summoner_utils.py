import json

from . import api_utils
from database.models import Summoner


def update_leagues(region):
    master, grandmaster, challenger = api_utils.get_leagues(region)
    with open(f'json/leagues/{region}_master.json', 'w') as f1, open(f'json/leagues/{region}_grandmaster.json', 'w') as f2, open(f'json/leagues/{region}_challenger.json', 'w') as f3:
        json.dump(master, f1, indent=4)
        json.dump(grandmaster, f2, indent=4)
        json.dump(challenger, f3, indent=4)
    print('Leagues successfully updated!\n---')

def get_league_summoners(region, summoner_count):
    with open(f'json/leagues/{region}_master.json', 'r') as f1, open(f'json/leagues/{region}_grandmaster.json', 'r') as f2, open(f'json/leagues/{region}_challenger.json', 'r') as f3:
        master = json.load(f1)
        grandmaster = json.load(f2)
        challenger = json.load(f3)

    league_summoner_data = []
    for entry in master['entries']:
        # Skip a summoner if they have less than 10 games played in master and are less than 200 lp (not demoting from grandmaster)
        if entry['freshBlood'] and entry['leaguePoints'] < 200:
            continue
        league_summoner_data.append([entry['summonerId'], entry['leaguePoints']])
    for entry in grandmaster['entries']:
        league_summoner_data.append([entry['summonerId'], entry['leaguePoints']])
    for entry in challenger['entries']:
        league_summoner_data.append([entry['summonerId'], entry['leaguePoints']])
    # Sort summoner data by leaguePoints from highest to lowest so that truncated data starts at the highest elo
    league_summoner_data.sort(key=lambda x: x[1], reverse=True)
    league_summoner_data = league_summoner_data[:summoner_count]

    league_summoners = []
    i=0
    for entry in league_summoner_data:
        summoner_data = api_utils.get_summoner(region, entry[0])
        summoner = Summoner(puuid=summoner_data['puuid'], id=summoner_data['id'], name=summoner_data['name'], level=summoner_data['summonerLevel'])
        league_summoners.append(summoner)
        i+=1
        print(f'Summoner successfully queried: {summoner.puuid} | {summoner.name} ({i}/{len(league_summoner_data)})')
    return league_summoners
