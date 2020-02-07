from PIL import Image, ImageDraw
import math


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
    # firstImg.show()
    finalImg = Image.open("secondIMG.png")
    finalImg.paste(firstImg)
    finalImg.show()
    # firstImg.show()
    finalImg.save("final.png")


main()