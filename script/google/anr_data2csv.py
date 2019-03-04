# -*- coding: utf-8 -*-
import csv
from bs4 import BeautifulSoup, Comment, sys

reload(sys)
sys.setdefaultencoding('utf-8')


# csv = open('csvfile.csv', "w")
# csv.write('信息' + ',' + '位置' + ',' + '报告' + ',' + '受影响用户数量' + ',' + '详细错误信息' + '\n')
# with open('t.csv','wb') as myFile:
#     myWriter=csv.writer(myFile)
#     myWriter.writerow(['信息', '位置', '报告', '受影响用户数量', '错误信息链接'])


def get_table_data(session_table, myWriter):
    trs = session_table.findAll('tr')
    for tr in trs:
        # div = tr.find('div', 'LTMPNY-od-a')
        # errors = div.findAll('p')
        # errorDescription
        # errorDescription = errors[0].get_text()
        # errorLocation
        # errorLocation = errors[1].get_text()

        pv = tr.findAll('p')
        errorDescription = ''
        errorLocation = ''
        reportsTotal = ''
        numAffected = ''
        for p in pv:
            if p.get('data-type') == 'errorDescription':
                errorDescription = p.get_text()
            elif p.get('data-type') == 'errorLocation':
                errorLocation = p.get_text()
            elif p.get('data-type') == 'reportsTotal':
                reportsTotal = p.get_text()
            elif p.get('data-type') == 'numAffected':
                numAffected = p.get_text()
        print(errorDescription + ' ---- ' + errorLocation + ' ---- ' + reportsTotal + ' ---- ' + numAffected)

        # link
        aaa = tr.find('a')
        if aaa is None:
            continue
        href = 'https://play.google.com/apps/publish/?account=8505122062204140606' + aaa.get('href')
        print(href)

        myWriter.writerow([errorDescription, errorLocation, reportsTotal, numAffected, 'xxx\nyyy\nzzz\n', href])
        # myWriter.writerow([errorDescription.replace('\n', ' '), errorLocation.replace('\n', ' '), reportsTotal.replace('\n', ' '), numAffected.replace('\n', ' '), href])

        # row = errorDescription.replace('\n', ' ').replace(',', '.') + ',' \
        #       + errorLocation.replace('\n', ' ').replace(',', '.') + ',' \
        #       + reportsTotal.replace('\n', ' ').replace(',', '.') + ',' \
        #       + numAffected.replace('\n', ' ').replace(',', '.') + ',' \
        #       + href
        # print(row)
        # csv.write(row + '\n')


def pre_handle_data(html, myWriter):
    soup = BeautifulSoup(html, 'lxml')
    for element in soup(text=lambda text: isinstance(text, Comment)):
        element.extract()

    session_tables = soup.findAll('section')
    for session_table in session_tables:
        if session_table.get('role') == 'article':
            get_table_data(session_table, myWriter)


if __name__ == '__main__':
    file_object0 = open('AnrPage0.html')
    file_object1 = open('AnrPage1.html')
    try:
        with open('t.csv', 'wb') as myFile:
            myWriter = csv.writer(myFile)
            myWriter.writerow(['信息', '位置', '报告', '受影响用户数量', '错误信息链接'])

            html = file_object0.read()
            pre_handle_data(html, myWriter)
            html = file_object1.read()
            pre_handle_data(html, myWriter)
    finally:
        file_object0.close()
        file_object1.close()
