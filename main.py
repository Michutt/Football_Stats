from PIL import Image, ImageDraw
import math
import stats


def PolygonCreate(listOfStats):
    apexes = []
    xMid = 400
    yMid = 400
    radius = 400
    for i in range(len(listOfStats)):
        pos = i * 360 / len(listOfStats)
        x = int(math.sin(pos * math.pi / 180) * radius * listOfStats[i] + xMid)
        y = int(math.cos(pos * math.pi / 180) * radius * listOfStats[i] + yMid)
        apexes.append((x, y))

    return apexes


def main():
    rando = []
    rando.append(0.7)
    rando.append(0.46)
    rando.append(0.3)
    rando.append(0.7)
    rando.append(0.32)
    rando.append(0.69)

    firstImg = Image.open("firstIMG.png")
    mask = Image.new("L", firstImg.size, 0)
    draw = ImageDraw.Draw(mask)
    apexes = PolygonCreate(rando)
    draw.polygon(apexes, fill=255)
    firstImg.putalpha(mask)
    finalImg = Image.open("secondIMG.png")
    x = Image.composite(firstImg, finalImg, mask)
    x.show()
    x.save("final.png")


main()
print(stats.player.fouls)