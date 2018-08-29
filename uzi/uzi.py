# from PIL import Image
#
# uziImage = Image.open("screen15.jpg")
# uziPixels = uziImage.load()
#
# h, w = uziImage.height, uziImage.width
#
# for x in range(w):
#     for y in range(h):
#         print(chr(uziPixels[x, y][0]), end='')

import datetime

yearList = []

for years in range(1000, 2018):
    if years % 100 == 0 :
        continue

    try:
        dec = datetime.date(years - 1, 12, 31)
        jan = datetime.date(years, 1, 26)

        start_of_year = datetime.date(years, 1, 1)
        end_of_year = datetime.date(years+1, 1, 1)

        days = (end_of_year - start_of_year).days

        # print("Year: " + str(years) + " days: " + str(days))

        if days == 366:
            feb = datetime.date(years, 2, 29)
            if jan.strftime("%a") == "Mon" and dec.strftime("%a") == "Wed" and feb.strftime("%a") == "Sun":
                print("Found: " + str(years) + " " + jan.strftime("%a") + ", " + dec.strftime("%a") + ", " + feb.strftime("%a"))


                yearList.append(years)

    except:
        pass