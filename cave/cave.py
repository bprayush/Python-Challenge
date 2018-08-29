from PIL import Image


image = Image.open('cave.jpg')
pixels = image.load()

oddImage = Image.new(image.mode, image.size)
evenImage = Image.new(image.mode, image.size)

# odd_pixels = []
# even_pixels = []

#  ODD RANGE

for odd_x in range(1, image.width, 2):
    for odd_y in range(1, image.height, 2):
        # odd_pixels.append(pixels[odd_x, odd_y])
        oddImage.putpixel((odd_x, odd_y), pixels[odd_x, odd_y])

for even_x in range(0, image.width, 2):
    for even_y in range(0, image.height, 2):
        # even_pixels.append(pixels[even_x, even_y])
        evenImage.putpixel((even_x, even_y), pixels[even_x, even_y])


oddImage.save('odd.jpg')
evenImage.save('even.jpg')
