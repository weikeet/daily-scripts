# -*- coding: utf-8 -*-
import requests

url = "https://api.trello.com/1/cards/5c7cbbafc2341071e2721c54/actions?key=0e21482f7759b336f6745d69b10f87e0&token=d20b993af75be760d598f62e6046a40b8139cd8bc1b168b3950b1c0d9c3cad3a"
# url = "https://api.trello.com/1/cards/5c7cbbafc2341071e2721c54/actions?key={key}&token={token}"

response = requests.request("GET", url)
response.raise_for_status()

print(response.text)
