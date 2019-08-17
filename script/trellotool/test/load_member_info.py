# -*- coding: utf-8 -*-

import simplejson as json
from trello import TrelloApi

trello = TrelloApi('0e21482f7759b336f6745d69b10f87e0', 'd20b993af75be760d598f62e6046a40b8139cd8bc1b168b3950b1c0d9c3cad3a')
memberIds = ["5bfbb2786a76248ffe1602cb", "5b305e4b6cd6490b91b51c86"]

def load_member():
    member_board_json = json.loads(json.dumps(trello.members.get_board('5bfbb2786a76248ffe1602cb')))
    print(member_board_json)
    for board in member_board_json:
        print(board['name'])
        print(board['id'])
    pass


if __name__ == '__main__':
    load_member()
