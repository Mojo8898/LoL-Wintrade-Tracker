from database.database import Database
from scripts import league_summoner_utils, match_utils, participant_utils


def main():
    region = 'na1'
    db = Database(region)

    league_summoner_utils.update_leagues(region) # 3 API calls (ladder updates at 7am)

    # Truncated length of summoner list, leave as None for no truncation
    summoner_count = None
    league_summoners = league_summoner_utils.get_league_summoners(region, summoner_count) # 1 API call per summoner
    db.insert_summoners(league_summoners)

    matches_per_summoner = 100 # 0-100
    matches = match_utils.get_matches(region, league_summoners, matches_per_summoner) # 1 API calls per summoner
    db.insert_matches(matches)

    participants = participant_utils.get_participants(region, matches) # 1 API call per match
    db.insert_participants(participants)

if __name__ == '__main__':
    main()
