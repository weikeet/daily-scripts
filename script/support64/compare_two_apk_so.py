# -*- encoding: utf-8 -*-
import subprocess
import sys

total_so_list = []


def get_so_list(apk_path):
    # apk_zip_info_bytes = subprocess.check_output(['zipinfo', '-1', apk_path, '| grep \.so$'])
    apk_zip_info_bytes = subprocess.check_output(['zipinfo', '-1', apk_path])
    apk_zip_info_texts = apk_zip_info_bytes.decode('utf-8')
    apk_zip_info_list = apk_zip_info_texts.split('\n')
    apk_zip_info_list.remove('')

    so_list = []
    for em in apk_zip_info_list:
        if 'lib/arm' in em and '.so' in em:
            so_list.append(em)
    so_list.sort()

    print('')
    print(apk_path, 'so list:')

    so_name_list = []
    for so in so_list:
        so_name = so.split('/')[2]
        if so_name in total_so_list:
            pass
        else:
            total_so_list.append(so_name)

        so_name_list.append(so_name)
        print(so)

    print('')
    print('------------------------------------------------------')

    return so_name_list


if __name__ == '__main__':
    file_a_path = sys.argv[1]
    file_b_path = sys.argv[2]

    a_so_name_list = get_so_list(file_a_path)
    b_so_name_list = get_so_list(file_b_path)

    total_so_list.sort()

    print('')
    print(file_a_path, '缺少的 so 文件：')
    for so_name in total_so_list:
        if so_name in a_so_name_list:
            pass
        else:
            print(so_name)

    print('')
    print(file_b_path, '缺少的 so 文件：')
    for so_name in total_so_list:
        if so_name in b_so_name_list:
            pass
        else:
            print(so_name)
