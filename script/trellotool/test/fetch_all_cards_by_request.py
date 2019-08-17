import requests
import simplejson as json

# todo get all board id by chrome driver

url = "https://api.trello.com/1/boards/5c6658b10e98ab598a0f315f/cards"

querystring = {"key": "0e21482f7759b336f6745d69b10f87e0",
               "token": "d20b993af75be760d598f62e6046a40b8139cd8bc1b168b3950b1c0d9c3cad3a"}

response = requests.request("GET", url, params=querystring)
response.raise_for_status()

# print(response.text)
board_json = json.loads(response.text)
for card_item in board_json:
    # print(card_item)
    card_json = json.loads(json.dumps(card_item))
    labels = card_json['labels']
    labels_json = json.loads(json.dumps(labels))
    if 'Need QA strtest' in str(labels):
        print('Need card:', card_json['name'], labels)
    if 'QA strtest done' in str(labels):
        print("Done card:", card_json['name'], labels)
