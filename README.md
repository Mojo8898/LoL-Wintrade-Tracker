# LoL-Wintrade-Tracker
The LoL-Wintrade-Tracker is a tool that queries Masters+ leagues and uses statistical analysis to find wintraders in the game League of Legends.

## Get Started
To use the tool, you need to place your API key in an empty Python file named keys.py inside the config/ folder in the following format:

    API_KEY = 'your_api_key'

## Rate Limits
The Riot Games API has rate limits that restrict the number of requests you can make within a certain time period. The following are the rate limits a personal Riot API key:

- 20 requests every 1 second(s)
- 100 requests every 2 minute(s)

## Runtime Estimates
The following are estimated runtime requirements:
- League summoners query time: ~2 hours
- Matches query time: ~2 hours
- Participants query time: ~3 days
- Disk space: ~250MB