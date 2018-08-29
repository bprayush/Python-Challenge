from PIL import Image

image = Image.open('wire.png')
newSize = (100, 100)
pixels = image.load()

newImage = Image.new('RGB', newSize)

x, y, pixelIndex = -1, 0, 0
dimension = 200
imageDelta = [(1, 0), (0, 1), (-1, 0), (0, -1)]


while dimension/2 > 0:
    for delta in imageDelta:
        steps = dimension // 2
        for step in range(steps):
            x, y = x + delta[0], y + delta[1]
            newImage.putpixel((x, y), pixels[pixelIndex, 0])
            pixelIndex += 1

        dimension -= 1


newImage.save('rendered.png')

