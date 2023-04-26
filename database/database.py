from peewee import SqliteDatabase, IntegrityError

from .models import Summoner, Match, Participant, initialize_database


class Database:
    def __init__(self, region):
        initialize_database(f'database/{region}_database.db')
        self.db = SqliteDatabase(f'database/{region}_database.db')
        with self.db:
            self.db.create_tables([Summoner, Match, Participant])

    # Summoner methods
    def insert_summoner(self, summoner):
        try:
            summoner.save(force_insert=True)
            # print(f'Summoner saved: {summoner.puuid} | {summoner.name}') # Debug
        except IntegrityError:
            # print(f'Duplicate summoner: {summoner.puuid}, changing name from "{Summoner.get_by_id(summoner.puuid).name}" to "{summoner.name}"') # Debug
            summoner.save()

    def insert_summoners(self, summoners):
        try:
            with self.db.atomic():
                Summoner.bulk_create(summoners, batch_size=100)
        except IntegrityError:
            print('Notice: Attempted to insert summoners that already exist, now attempting to insert individually')
            for summoner in summoners:
                self.insert_summoner(summoner)
        print(f'League summoners were successfully inserted! (length: {len(summoners)})\n---')

    # Match methods
    def insert_match(self, match):
        try:
            match.save(force_insert=True)
            # print(f'Match saved: {match.id}') # Debug
        except IntegrityError:
            # print(f'Duplicate match: {match.id}') # Debug
            pass

    def insert_matches(self, matches):
        try:
            with self.db.atomic():
                Match.bulk_create(matches, batch_size=100)
        except IntegrityError:
            print('Notice: Attempted to insert matches that already exist, now attempting to insert individually')
            for match in matches:
                self.insert_match(match)
        print(f'Matches were successfully inserted! (length: {len(matches)})\n---')

    # Participant methods
    def insert_participant(self, participant):
        try:
            participant.save(force_insert=True)
            # print(f'Participant saved: {participant.summoner_puuid} | {participant.match_id}') # Debug
        except IntegrityError:
            participant.save()
            # print(f'Duplicate participant: {participant.summoner_puuid} | {participant.match_id}') # Debug

    def insert_participants(self, participants):
        try:
            with self.db.atomic():
                Participant.bulk_create(participants, batch_size=100)
        except IntegrityError:
            print('Notice: Attempted to insert participants that already exist, now attempting to insert individually')
            for participant in participants:
                self.insert_participant(participant)
        print(f'Participants were successfully inserted! (length: {len(participants)})\n---')

    def __del__(self):
        self.db.close()
