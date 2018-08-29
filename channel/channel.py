import re
# import os
# import requests
import zipfile

file_name = "90052"
file_path = "channel/"

file_stack = []

while(1):
    try:
        file_stack.append(file_name + ".txt")
        file = open(file_path+file_name+".txt", "r")
        file_temp_data = file.read()
        file_data = re.findall(r'[0-9]', file_temp_data)
        new_file_name = "".join(file_data)
        # print(file_name+": "+new_file_name)
        # print(file_temp_data)
        file_name = new_file_name
        file.close()

    except:
        break

# r = requests.get("http://www.pythonchallenge.com/pc/def/channel.html")
#
# comments = re.findall(r'<!--(.*?)-->', r.text)
# print(comments)

print(file_stack)

text = ""

zf = zipfile.ZipFile('channel.zip', 'r')
# for info in zf.infolist():
#     # print(info.comment)
#     text = text + info.comment.decode()
#     print(info.comment, end='')


for file_name in file_stack:
    try:
        print(zf.getinfo(file_name).comment.decode(), end='')
    except:
        pass
