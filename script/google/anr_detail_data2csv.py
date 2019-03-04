# -*- coding: utf-8 -*-
# import csv
import re

from bs4 import BeautifulSoup, Comment, sys

reload(sys)
sys.setdefaultencoding('utf-8')

csv = open('testsss.csv', "w")


# with open('t.csv','wb') as myFile:
#     myWriter=csv.writer(myFile)
#     myWriter.writerow(['xxx\nyyy\nzzz\n'])



def pre_handle_data(html):
    soup = BeautifulSoup(html, 'lxml')
    for element in soup(text=lambda text: isinstance(text, Comment)):
        element.extract()

    div_detail = soup.find('div', class_='CVP2USC-Dc-b')
    div_detail_item = div_detail.findAll('div', class_='CVP2USC-Vp-d CVP2USC-xd-b')

    div_error_title = div_detail_item[0].find('div', class_='gwt-HTML')
    # print(' '.join(re.split(' +|\n+', div_error_title.string)).strip())
    print(' '.join(div_error_title.string.replace('\n', ' ').replace(',', '.').split()))
    div_error_infos = div_detail_item[0].findAll('div', class_='gwt-Label CVP2USC-dq-b')

    test_str = '['
    for div_error_info in div_error_infos:
        # print(' '.join(re.split(' +|\n+', div_error_info.string)).strip())
        s1 = div_error_info.string.replace('\n', ' ').replace(',', '.')
        s2 = ' '.join(s1.split())
        test_str = test_str + s2 + ','
        print(s2)
    test_str = test_str + 'abc ]'
    #csv.write(test_str)
    csv.write('xxx\nyyy\nzzz\n')

if __name__ == '__main__':
    file_object0 = open('AnrDetailPage.html')
    try:
        html = file_object0.read()
        pre_handle_data(html)
    finally:
        file_object0.close()
