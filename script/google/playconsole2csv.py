# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup, Comment, sys

reload(sys)
sys.setdefaultencoding('utf-8')
file_object = open('AnrTable.html')
try:
    htmlStr = file_object.read()

    soup = BeautifulSoup(htmlStr[:htmlStr.find('</table>') + 8])

    for element in soup(text=lambda text: isinstance(text, Comment)):
        element.extract()

    trs = soup.findAll('tr')

    csv = open('csvfile.csv', "w")
    csv.write('信息' + ',' + '位置' + ',' + '报告' + ',' + '受影响用户数量' + ',' + '详细错误信息' + '\n')

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

        print(errorDescription)
        print(errorLocation)
        print(reportsTotal)
        print(numAffected)

        # link
        href = 'https://play.google.com/apps/publish/?account=8505122062204140606' + \
            tr.find('a').get('href')
        print(href)

        row = errorDescription.replace('\n', '').replace(
            ',', '.') + ',' + errorLocation + ',' + reportsTotal + ',' + numAffected + ',' + href
        print(row)
        csv.write(row + '\n')

finally:
    file_object.close()
