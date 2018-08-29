from PIL import Image
import numpy as np

mozartImage = Image.open("mozart.gif")
mozartPixels = mozartImage.load()

pink = (255, 0, 255)
white = (251, 251, 251)

width = mozartImage.width
height = mozartImage.height

pinkPixels = []
whitePixels = []

for y in range(0, height):
    for x in range(0, width):
        if mozartPixels[x, y] == 195:

            tempX = x - 1
            print("-------------+---------------")
            while tempX >= 0 or mozartPixels[tempX, y] != 195:
                tempPixel = mozartPixels[tempX, y]
                mozartPixels[tempX, y] = mozartPixels[tempX + 1, y]
                mozartPixels[tempX + 1, y] = tempPixel
                tempX = tempX - 1
                if tempX < 0:
                    break
                print(tempX)
            print("-------------_---------------")




tmp = mozartImage.copy()
tmp.frombytes(bytes(np.array(mozartImage)))

tmp.save("okay.gif")

print(np.array(mozartImage))

mozartImage.save("rendered.gif")
