# -*- coding: utf-8 -*-

import os
import difflib
import webbrowser
from Crypto.Cipher import AES

cipher = AES.new(b'1vs^&Ecwq)@Mtpw!', AES.MODE_ECB)


def replaceEndSpace(s):
    i = len(s) - 1
    if s[i] == ' ':
        new_s = s[0:i]
        return replaceEndSpace(new_s)
    else:
        return s


def compare_yaml_file(file_a, file_b):
    a_lines = []
    b_lines = []
    
    file_a = replaceEndSpace(file_a)
    with open(file_a, 'rb') as f_a:
        data_a = f_a.read()
        print(len(data_a))
        decrypt_data_a = cipher.decrypt(data_a)
        decrypt_result_a = decrypt_data_a.decode('utf-8')
        print(decrypt_result_a)
        a_lines = decrypt_result_a.splitlines()

    file_b1 = replaceEndSpace(file_b)
    with open(file_b1, 'rb') as f_b:
        data_b = f_b.read()
        decrypt_data_b = cipher.decrypt(data_b)
        decrypt_result_b = decrypt_data_b.decode('utf-8')
        # print(decrypt_result_b)
        b_lines = decrypt_result_b.splitlines()

    html_str = compareInner(a_lines, b_lines, file_a, file_b)
    # print(html_str)
    html_file_path = os.getcwd() + '/compare_result.html'
    html_file = open(html_file_path, 'w', encoding='utf-8')
    html_file.write(str(html_str['html']))
    webbrowser.open('file://' + html_file_path)


def compareInner(text1_lines, text2_lines, file_a, file_b):
    d = difflib.HtmlDiff()

    html_string = d.make_file(text1_lines, text2_lines)\
        .replace("table.diff {font-family:Courier; border:medium;}", ".warpabc{width: 100%; white-space: normal; word-wrap: break-word; word-break: break-all}\n        table.diff {font-family:Courier; border:medium; font-size: 80%}")\
        .replace('<tbody>', '<tbody>\n            <tr><td class="diff_next"></td><td class="diff_header" id="from698_3"></td><td style="width:48%;font-weight:bold;"><span style="background-color:#ffaaaa">' + file_a + '</span></td><td class="diff_next"></td><td class="diff_header" id="to698_3"></td><td style="width:48%;font-weight:bold;"><span style="background-color:#aaffaa">' + file_b + '</span></td></tr>')\
        .replace('<td nowrap="nowrap">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;SignatureKey', '<td class="warpabc">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;SignatureKey')

    different_lines = html_string.count('diff_add') - 2 + html_string.count('diff_chg') - 2 + html_string.count('diff_sub') - 2
    if (different_lines < 0):
        different_lines = 0
    
    total_lines = len(text1_lines) + len(text2_lines)
    if (total_lines == 0):
        total_lines = 1
    
    similarity = round(1 - different_lines / total_lines, 4)
    # print('Similarity', similarity)
    return {'html' : html_string, 'similarity' : format(similarity, '.2%')}


if __name__ == '__main__':
    # print(os.getcwd())
    # webbrowser.open('file:///Users/zhengwei.zhang/Documents/compare.html')
    file_a_path = input('Please input first file path: ')
    file_b_path = input('Please input second file path: ')

    compare_yaml_file(file_a_path, file_b_path)
