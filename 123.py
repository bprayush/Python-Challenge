import urllib.request
import re

html = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345").read().decode()
data = html
print("".join(re.findall("[0-9]", data)))
print(data)
attr = 12345

for i in range(0, 400):

    html = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="+str(attr)).read().decode()
    data = html
    data = "".join(re.findall("[0-9]", data))
    print(str(i)+": ", end='')
    print(data)
    attr = data