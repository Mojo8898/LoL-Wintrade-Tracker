from time import sleep

from riotwatcher import LolWatcher

from config.keys import API_KEY


watcher = LolWatcher(API_KEY)

def get_leagues(region):
    master = watcher.league.masters_by_queue(region, 'RANKED_SOLO_5x5')
    grandmaster = watcher.league.grandmaster_by_queue(region, 'RANKED_SOLO_5x5')
    challenger = watcher.league.challenger_by_queue(region, 'RANKED_SOLO_5x5')
    sleep(2.49)
    return master, grandmaster, challenger

def get_summoner(region, summoner_id):
    summoner = watcher.summoner.by_id(region, summoner_id)
    sleep(.83)
    return summoner

def get_summoner_matchlist(region, summoner_puuid, match_count, start_time):
    summoner_matchlist = watcher.match.matchlist_by_puuid(region, summoner_puuid, 0, match_count, 420, start_time=start_time)
    sleep(.83)
    return summoner_matchlist

def get_match(region, match_id):
    match = watcher.match.by_id(region, match_id)
    sleep(.83)
    return match

def get_timeline(region, match_id):
    timeline = watcher.match.timeline_by_match(region, match_id)
    sleep(.83)
    return timeline
