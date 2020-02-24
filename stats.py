from datetime import datetime
import requests


class Stats(object):
    def __init__(self):
        self.stats = {}
        self.playerName = "Dybala" #searched player (only Serie A and Primera Division) :(
        self.goals = 0
        self.matches = 0
        self.shots = 0
        self.shotsOnTarget = 0
        self.rating = 0
        self.passCount = 0
        self.passSuccess = 0
        self.assist = 0
        self.fouls = 0
        self.key = "VpZZPQimxVaQAqD8" #key to access API,
        # you can generate it by taking free trial here:
        # https://www.isportsapi.com

    def FindPlayer(self):
        url = "http://api.isportsapi.com/sport/football/player/search?api_key={}&name={}".format(self.key, self.playerName)

        response = requests.get(url)
        x = response.json()['data']

        for item in x:
            playerId = item['playerId']
            self.playerName = item['name']
            teamId = item['teamId']
            break
        return teamId, playerId


    def FindLeague(self, teamId):
        url = "http://api.isportsapi.com/sport/football/team?api_key={}&teamId=".format(self.key) + str(teamId)

        response = requests.get(url)
        x = response.json()['data']

        for item in x:
            leagueId = item['leagueId']
            self.teamName = item['name']
            break
        return leagueId


    def PlayerStats(self, leagueId, playerInfo):
        url = "http://api.isportsapi.com/sport/football/playerstats/league?api_key={}&leagueId=".format(self.key) + str(leagueId)

        response = requests.get(url)
        x = response.json()['data']
        print(x)
        for item in x:
            playerId = item['playerId']
            if playerId == playerInfo:
                print(item)
                self.matches += item["appearanceCount"]
                self.goals += item["goals"]
                self.goals += item["penaltyGoals"]
                self.shots += item["shotCount"]
                self.shotsOnTarget += item["shotTargetCount"]
                self.rating += float(item["rating"])/2
                self.passCount += item["passCount"]
                self.passSuccess += item["passSuccessCount"]
                self.assist += item["assistCount"]
                self.fouls += item["foulsCount"]


def dataProcessing(player):
    player.goals = player.goals / player.matches
    player.shots = player.shotsOnTarget / player.shots
    player.rating = player.rating / 100.0
    player.passCount = player.passSuccess / player.passCount
    player.assist = player.assist / player.matches
    player.fouls = player.fouls / player.matches


player = Stats()
playerInfo = player.FindPlayer()
leagueId = player.FindLeague(playerInfo[0])
player.PlayerStats(leagueId, playerInfo[1])
dataProcessing(player)
