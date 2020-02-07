from datetime import datetime
import requests


class Stats(object):
    def __init__(self):
        self.modificationTime = 0
        self.goals = 0
        self.matches = 0
        self.shots = 0
        self.shotsOnTarget = 0
        self.rating = 0
        self.passCount = 0
        self.passSuccess = 0
        self.assist = 0
        self.dribbles = 0
        self.fouls = 0

    def FindPlayer(self):
        url = "http://api.isportsapi.com/sport/football/player/search?api_key=obhLg1YYVcEZENQm&name=Ronaldo"

        response = requests.get(url)
        x = response.json()['data']
        print(x)
        for item in x:
            playerId = item['playerId']
            teamId = item['teamId']
            break
        return teamId, playerId


    def FindLeague(self, teamId):
        url = "http://api.isportsapi.com/sport/football/team?api_key=obhLg1YYVcEZENQm&teamId=" + str(teamId)

        response = requests.get(url)
        x = response.json()['data']
        print(x)
        for item in x:
            leagueId = item['leagueId']
            break
        return leagueId


    def PlayerStats(self, leagueId, playerInfo):
        url = "http://api.isportsapi.com/sport/football/playerstats/league?api_key=obhLg1YYVcEZENQm&leagueId=" + str(leagueId)

        response = requests.get(url)
        x = response.json()['data']
        for item in x:
            playerId = item['playerId']
            if playerId == playerInfo:
                print(item)
                # self.modificationTime = datetime.fromtimestamp(1579479061)
                # print(self.modificationTime)


    def StatCollection(self, item):
        pass



player = Stats()
playerInfo = player.FindPlayer()
leagueId = player.FindLeague(playerInfo[0])
player.PlayerStats(leagueId, playerInfo[1])

