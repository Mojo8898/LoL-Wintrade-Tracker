from . import api_utils
from database.models import Match


def get_matches(region, league_summoners, match_count=100):
    start_time = get_latest_match_time()
    match_set = set()
    i=0
    for summoner in league_summoners:
        matchlist = api_utils.get_summoner_matchlist(region, summoner.puuid, match_count, start_time)
        if len(matchlist) == 0:
            print(f'No matches found for summoner: {summoner.puuid} | {summoner.name}')
            continue
        match_set.update(matchlist)
        i+=1
        print(f'Matchlist successfully queried for summoner: {summoner.puuid} | {summoner.name} ({i}/{len(league_summoners)})')
        print(f'Match count: {len(match_set)} unique / {i*match_count} total | Average overlap per summoner: {(i*match_count - len(match_set))/i}')
    matches = []
    for match_id in match_set:
        matches.append(Match(id=match_id))
    return matches

def get_latest_match_time():
    try:
        for match in Match.select().order_by(Match.id):
            latest_match_time = match.end_timestamp
        return latest_match_time
    except UnboundLocalError:
        return 1673449200
