from PIL import Image, ImageDraw, ImageFont
import math
import stats


def polygonCreate(listOfStats):
    apexes = []
    xMid = 450
    yMid = 450
    radius = 400
    for i in range(len(listOfStats)):
        pos = i * 360 / len(listOfStats)
        x = int(math.sin(pos * math.pi / 180) * radius * listOfStats[i] + xMid)
        y = int(math.cos(pos * math.pi / 180) * radius * listOfStats[i] + yMid)
        apexes.append((x, y))

    return apexes

def subtitles(image):
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", 16)
    draw.text((10, 15), "1.0", font=font, fill=(0,0,0))


def main():
    processedData = []
    processedData.extend((stats.player.goals, stats.player.shots, stats.player.rating, stats.player.passCount, stats.player.assist, stats.player.fouls))
    print(processedData)


    firstImg = Image.open("firstIMG.png")
    mask = Image.new("L", firstImg.size, 0)
    draw = ImageDraw.Draw(mask)
    apexes = polygonCreate(processedData)
    draw.polygon(apexes, fill=255)
    firstImg.putalpha(mask)
    finalImg = Image.open("secondIMG.png")
    x = Image.composite(firstImg, finalImg, mask)
    subtitles(x)
    x.show()
    x.save("final.png")


main()