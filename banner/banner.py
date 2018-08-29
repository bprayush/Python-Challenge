import requests
import pickle

r = requests.get("http://www.pythonchallenge.com/pc/def/banner.p")
org_data = pickle.load(open("banner.p", "rb"))

for grid in org_data:
    for data in grid:
        for i in range(0, data[1]):
            print(data[0], end='')

    print("")


print(org_data)