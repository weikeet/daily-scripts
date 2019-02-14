from bs4 import BeautifulSoup, Comment

file_object = open('crashlytics_page.html')
try:
    htmlStr = file_object.read()

    htmlStr = htmlStr[htmlStr.find(
        '<table class="issues-table table color-dark-gray">'):]

    soup = BeautifulSoup(htmlStr[:htmlStr.find('</table>') + 8])

    for element in soup(text=lambda text: isinstance(text, Comment)):
        element.extract()

    trs = soup.findAll('tr')

    csv = open('csvfile.csv', "w")

    for tr in trs:
        title = tr.find('span', 'issue-title')
        subtitle = tr.find('div', 'issue-subtitle')
        issue = tr.find('span', 'issue-number')
        number = tr.find_all('div', 'stat')
        td = tr.find('td', 'cell-title')
        href = 'https://fabric.io'+td.find('a').get('href')

        row = title.string + ',' + subtitle.text.replace(issue.string, '') + ',' + issue.string + ',' + number[0].find(
            'span').text + ',' + number[1].find('span').text + ','+href
        print row
        csv.write(row + '\n')

finally:
    file_object.close()
