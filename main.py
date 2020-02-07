from PIL import Image, ImageDraw

def main():
    secondImg = Image.open("secondIMG.jpg")
    
    secondImg.save("final.jpg")


main()