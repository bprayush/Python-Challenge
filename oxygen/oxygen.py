from PIL import Image
import pprint

i = Image.open('oxygen.png')
px = i.load()
h = int(i.height / 2)


dictData = []
dictData.append(px[0, h])

for width in range(5, 629, 7):
    # print(px[width, h])
    data = (px[width, h])
    dictData.append(data)

pprint.pprint(dictData)

text = ""

for a in dictData:
    text = text + chr(a[0])

print(text)

data = [105, 110, 116, 101, 103, 114, 105, 116, 121]

for a in data:
    print(chr(a), end='')