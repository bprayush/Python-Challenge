from PIL import Image

evil1 = open('evil2.gfx', 'rb')
raw = evil1.read()
print(len(raw))


for i in range(0, 5):
    print(raw[i::5])
    file = open(str(i)+'.jpg', 'wb')
    file.write(raw[i::5])
    file.close()
