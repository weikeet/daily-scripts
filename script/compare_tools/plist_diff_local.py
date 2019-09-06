# -*- coding: utf-8 -*-

import os
import subprocess
import sys
import time


def replace_end_space(s):
    i = len(s) - 1
    if s[i] == ' ':
        new_s = s[0:i]
        return replace_end_space(new_s)
    else:
        return s


def compare_yaml_file(first_file, second_file):
    first_file = replace_end_space(first_file)
    second_file = replace_end_space(second_file)

    strTime = time.strftime('%Y%m%d%H%M%S', time.localtime())
    first_decode_file = first_file + '_' + strTime + '_decode.plist'
    second_decode_file = second_file + '_' + strTime + '_decode.plist'

    curr_py_file_path = os.path.abspath(__file__).replace('plist_diff_local.py', '')
    plist_converter_file = curr_py_file_path + '/jacoder'
    subprocess.run([plist_converter_file, '-d', first_file, first_decode_file], stdout=subprocess.PIPE)
    subprocess.run([plist_converter_file, '-d', second_file, second_decode_file], stdout=subprocess.PIPE)

    compare_tools = curr_py_file_path + "/compare"
    subprocess.run([compare_tools, first_decode_file, second_decode_file], stdout=subprocess.PIPE)


if __name__ == '__main__':
    # file_a_path = input('Please input first file path: ')
    # file_b_path = input('Please input second file path: ')

    file_a_path = sys.argv[1]
    file_b_path = sys.argv[2]

    compare_yaml_file(file_a_path, file_b_path)
