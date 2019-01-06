import requests

r = requests.get("https://api.chucknorris.io/jokes/categories")
data = r.json()

i = 1
for cat in data:

    url = "https://api.chucknorris.io/jokes/random?category={}".format(cat)
    req = requests.get(url)
    respons = req.json()
    print("\n")
    print( str(i) + " " + respons["value"])
    i = i + 1

    if (i >= 17):
        print("Son todas las quotes disponibles....")
