# -*- encoding: utf-8 -*-

import json
import time

if __name__ == '__main__':
    with open('brew_backup_2021070323.json') as backup_file:
        brew_backup_json = json.load(backup_file)
        brew_tap_list = brew_backup_json['brew_tap_list']
        brew_formula_list = brew_backup_json['brew_formula_list']
        brew_formula_unknown_list = brew_backup_json['brew_formula_unknown_list']
        brew_cask_list = brew_backup_json['brew_cask_list']

        brew_formula_new_list = []
        for formula in brew_formula_list:
            if formula['tag'] == 'unknown':
                brew_formula_unknown_list.append(formula['name'])
            else:
                brew_formula_new_list.append(formula)

        new_brew_backup_dict = {"brew_tap_list": brew_tap_list, "brew_formula_list": brew_formula_new_list, "brew_formula_unknown_list": brew_formula_unknown_list, "brew_cask_list": brew_cask_list}
        new_brew_backup_json = json.dumps(new_brew_backup_dict, ensure_ascii=False)
        new_brew_backup_json_file = open('brew_backup_' + time.strftime('%Y%m%d%H', time.localtime()) + '.json', 'w')
        new_brew_backup_json_file.write(new_brew_backup_json)
