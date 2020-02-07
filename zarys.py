import pygame
import math
from datetime import datetime
import requests

pygame.init()
win = pygame.display.set_mode((800, 800))

run = True


# class Stats(object):
#     def __init__(self):
#         self.modificationTime = 0
#         self.goals = 0
#         self.matches = 0
#         self.shots = 0
#         self.shotsOnTarget = 0
#         self.rating = 0
#         self.passCount = 0
#         self.passSuccess = 0
#         self.assist = 0
#         self.dribbles = 0
#         self.fouls = 0
#
#     def FindPlayer(self):
#         url = "http://api.isportsapi.com/sport/football/player/search?api_key=obhLg1YYVcEZENQm&name=Ronaldo"
#
#         response = requests.get(url)
#         x = response.json()['data']
#         print(x)
#         for item in x:
#             playerId = item['playerId']
#             teamId = item['teamId']
#             break
#         return teamId, playerId
#
#
#     def FindLeague(self, teamId):
#         url = "http://api.isportsapi.com/sport/football/team?api_key=obhLg1YYVcEZENQm&teamId=" + str(teamId)
#
#         response = requests.get(url)
#         x = response.json()['data']
#         print(x)
#         for item in x:
#             leagueId = item['leagueId']
#             break
#         return leagueId
#
#
#     def PlayerStats(self, leagueId, playerInfo):
#         url = "http://api.isportsapi.com/sport/football/playerstats/league?api_key=obhLg1YYVcEZENQm&leagueId=" + str(leagueId)
#
#         response = requests.get(url)
#         x = response.json()['data']
#         for item in x:
#             playerId = item['playerId']
#             if playerId == playerInfo:
#                 print(item)
#                 self.modificationTime = datetime.fromtimestamp(1579479061)
#                 print(self.modificationTime)
#
#
#     def StatCollection(self, item):
#         pass



# ronaldo = Stats()
# playerInfo = ronaldo.FindPlayer()
# print(playerInfo)
# leagueId = ronaldo.FindLeague(playerInfo[0])
# print(leagueId)
# ronaldo.PlayerStats(leagueId, playerInfo[1])


class BackgroundCircles(object):

    def __init__(self, win, color1, color2):
        self.xMid = 400
        self.yMid = 400
        self.radius = 300
        self.x = 0
        self.y = 0
        self.apexes = []
        self.color1 = color1
        self.color2 = color2

        win.fill((255, 255, 255))
        for i in range(10):
            if i % 2 == 0:
                color = color1
            else:
                color = color2
            pygame.draw.circle(win, color, (400, 400), 30 + i * 30, 30)

    def PolygonCreate(self, listOfStats):
        for i in range(len(listOfStats)):
            pos = i*360/len(listOfStats)
            self.x = int(math.sin(pos*math.pi/180) * self.radius * listOfStats[i] + self.xMid)
            self.y = int(math.cos(pos*math.pi/180) * self.radius * listOfStats[i]+ self.yMid)
            self.apexes.append([self.x, self.y])
            pygame.draw.circle(win, (100,200,20), (self.x, self.y), 4)

    def PolygonColor(self):
        pygame.draw.polygon(win, (255,0,0), [item for item in self.apexes])


rando = []
rando.append(0.7)
rando.append(0.46)
rando.append(0.3)
rando.append(0.7)
rando.append(0.32)
rando.append(0.69)
obrazek = BackgroundCircles(win, (250,250,250), (200,200,200))
obrazek.PolygonCreate(rando)


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
