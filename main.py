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

def subtitles(image, len):
    for j in range(len):
        for i in range(10):
            pos = j * 360 / len
            x = int(math.sin(pos * math.pi / 180) * (i + 1) * 40)
            y = int(math.cos(pos * math.pi / 180) * (i + 1) * 40)

            text = str((i+1)/10.0)
            box = (438 + x, 440 + y)   # (450, 450) <-- center of diagram

            font = ImageFont.truetype('arial.ttf', 16)
            line_height = sum(font.getmetrics())
            fontimage = Image.new('L', (font.getsize(text)[0], line_height))
            ImageDraw.Draw(fontimage).text((0,0), text, fill=255, font=font)
            fontimage = fontimage.rotate(pos + 180, resample=Image.BICUBIC, expand=True)
            image.paste((0, 0, 0), box=box, mask=fontimage)
    image.save("final.png")


def categories(image, len):
    boxes = ((400,880),(790,600),(810,220),(360,0),(30,180),(40,620))
    cats = ["Goal per match", "Shots on target per shot", "Ratio", "Succesfull passes per pass", "Assists per match", " Fouls per match"]
    for j in range(len):
        if j == 0:
            pos = 180
        else:
            pos = j * 360 / len

        text = cats[j]
        box = (boxes[j][0], boxes[j][1])

        font = ImageFont.truetype('arial.ttf', 16)
        line_height = sum(font.getmetrics())
        fontimage = Image.new('L', (font.getsize(text)[0], line_height))
        ImageDraw.Draw(fontimage).text((0, 0), text, fill=255, font=font)
        fontimage = fontimage.rotate(pos + 180, resample=Image.BICUBIC, expand=True)
        image.paste((0, 0, 0), box=box, mask=fontimage)


def main():
    processedData = []
    #dane z API
    processedData.extend((stats.player.goals, stats.player.shots, stats.player.rating, stats.player.passCount, stats.player.assist, stats.player.fouls))
    #dane gdyby API nie działało (np. jak teraz :[)
    # processedData.extend((0.4,0.5,0.3,0.36,0.62,0.40))

    firstImg = Image.open("firstIMG.png")
    mask = Image.new("L", firstImg.size, 0)
    draw = ImageDraw.Draw(mask)
    apexes = polygonCreate(processedData)
    draw.polygon(apexes, fill=255)
    firstImg.putalpha(mask)
    finalImg = Image.open("secondIMG.png")
    x = Image.composite(firstImg, finalImg, mask)

    subtitles(x, len(apexes))
    categories(x, len(apexes))

    x.show()
    x.save("final.png")


main()