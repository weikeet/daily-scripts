# -*- coding: utf-8 -*-

import csv
import time
import simplejson as json
from trello import TrelloApi

trello = TrelloApi('0e21482f7759b336f6745d69b10f87e0', 'd20b993af75be760d598f62e6046a40b8139cd8bc1b168b3950b1c0d9c3cad3a')
member_id = '5bfbb2786a76248ffe1602cb'
board_id_list = {'IA-AppLock-DEV':'5c53e12591179c8957495b30', 'IA-CN-DEV':'5c6658b10e98ab598a0f315f', 'IA-Security-DEV':'5c53e10c50fbe74830a0587d'}
# board_id_list = {}

data = {}
file_name = time.strftime("%Y%m%d_%H.%M.%S", time.localtime())


def write_data():
    with open(file_name + '.csv', 'w') as myFile:
        myWriter = csv.writer(myFile)
        myWriter.writerow(['board', 'Need_QA_test', 'QA_test_done'])
        for key, value in data.items():
            myWriter.writerow([key, value[0], value[1]])


def load_board():
    member_board_json = json.loads(json.dumps(trello.members.get_board('5bfbb2786a76248ffe1602cb')))
    print(member_board_json)
    for board in member_board_json:
        if 'IA-' in board['name']:
            board_id_list[board['name']] = board['id']

    for board_name,board_id in board_id_list.items():
        # board_json = json.loads(json.dumps(trello.boards.get(board_id)))
        # board_name = board_json['name']

        all_cards_json = json.loads(json.dumps(trello.boards.get_card(board_id)))
        print(len(all_cards_json))
        print(all_cards_json)

        need_test = []
        test_done = []
        need_test_result = ''
        test_done_result = ''
        for card_item in all_cards_json:
            # print(card_item)
            card_json = json.loads(json.dumps(card_item))
            labels = card_json['labels']
            labels_json = json.loads(json.dumps(labels))
            if 'Need QA strtest' in str(labels):
                need_test.append(card_json['name'])
                need_test_result = need_test_result + card_json['name'] + '\n'
                print('Need card:', card_json['name'], labels)
            if 'QA strtest done' in str(labels):
                test_done.append(card_json['name'])
                test_done_result = test_done_result + card_json['name'] + '\n'
                print("Done card:", card_json['name'], labels)

        data[board_name] = [need_test_result, test_done_result]

    write_data()


if __name__ == '__main__':
    load_board()
