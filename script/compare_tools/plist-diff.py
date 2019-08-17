# -*- coding: utf-8 -*-

import os
import time
import difflib
import webbrowser
import subprocess


def replaceEndSpace(s):
    i = len(s) - 1
    if s[i] == ' ':
        new_s = s[0:i]
        return replaceEndSpace(new_s)
    else:
        return s


def convert_any_plist_to(source_file='', target_file=''):
    plist_converter_file = os.getcwd() + '/jacoder'
    target_file = target_file + '_decode.plist'
    subprocess.run([plist_converter_file, '-d', source_file, target_file], stdout=subprocess.PIPE)
    with open(target_file, 'r') as tf:
        result = tf.read()
    return result


def compare_yaml_file1(first_file, second_file):
    first_file = replaceEndSpace(first_file)
    second_file = replaceEndSpace(second_file)

    first_decode_file = first_file + '_decode_' + str(time.time()) + '.plist'
    second_decode_file = second_file + '_decode_' + str(time.time()) + '.plist'

    plist_converter_file = os.getcwd() + '/jacoder'
    subprocess.run([plist_converter_file, '-d', first_file, first_decode_file], stdout=subprocess.PIPE)
    subprocess.run([plist_converter_file, '-d', second_file, second_decode_file], stdout=subprocess.PIPE)

    compare_tools = os.getcwd() + "/compare"
    subprocess.run([compare_tools, first_decode_file, second_decode_file], stdout=subprocess.PIPE)


def compare_yaml_file(first_file, second_file):
    first_file = replaceEndSpace(first_file)
    second_file = replaceEndSpace(second_file)

    first_target_file = os.getcwd() + '/first_target_file.oa'
    second_target_file = os.getcwd() + '/second_target_file.oa'

    first_decode_result = convert_any_plist_to(source_file=first_file, target_file=first_target_file)
    second_decode_result = convert_any_plist_to(source_file=second_file, target_file=second_target_file)

    html_str = compareInner(first_decode_result.splitlines(), second_decode_result.splitlines(), first_file,
                            second_file)
    html_file_path = os.getcwd() + '/compare_result.html'
    html_file = open(html_file_path, 'w', encoding='utf-8')
    html_file.write(str(html_str['html']))
    webbrowser.open('file://' + html_file_path)


def compareInner(text1_lines, text2_lines, file_a, file_b):
    d = difflib.HtmlDiff()

    html_string = d.make_file(text1_lines, text2_lines) \
        .replace("table.diff {font-family:Courier; border:medium;}",
                 ".warpabc{width: 100%; white-space: normal; word-wrap: break-word; word-break: break-all}\n        table.diff {font-family:Courier; border:medium; font-size: 80%}") \
        .replace('<tbody>',
                 '<tbody>\n            <tr><td class="diff_next"></td><td class="diff_header" id="from698_3"></td><td style="width:48%;font-weight:bold;"><span style="background-color:#ffaaaa">'
                 + file_a + '</span></td><td class="diff_next"></td><td class="diff_header" id="to698_3"></td><td style="width:48%;font-weight:bold;"><span style="background-color:#aaffaa">'
                 + file_b + '</span></td></tr>') \
        .replace('<td nowrap="nowrap">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"Message"',
                 '<td class="warpabc">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"Message"')

    different_lines = html_string.count('diff_add') - 2 + html_string.count('diff_chg') - 2 + html_string.count(
        'diff_sub') - 2
    if different_lines < 0:
        different_lines = 0

    total_lines = len(text1_lines) + len(text2_lines)
    if total_lines == 0:
        total_lines = 1

    similarity = round(1 - different_lines / total_lines, 4)
    return {'html': html_string, 'similarity': format(similarity, '.2%')}


if __name__ == '__main__':
    file_a_path = input('Please input first file path: ')
    file_b_path = input('Please input second file path: ')

    compare_yaml_file1(file_a_path, file_b_path)
