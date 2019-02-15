from bs4 import BeautifulSoup
import urllib2

#url = 'https://www.douban.com'
url = 'https://book.douban.com/mine?status=do'
#cookie ='ll="108090"; bid=BgSb5tqTgFg; _vwo_uuid_v2=D08B09F574612204835748D649E5182F3|d9376f8e3fe939ae6f67f8fc29fd8f58; viewed="1474824"; gr_user_id=1740613b-3148-4936-84d2-037f168725f4; push_noty_num=0; push_doumail_num=0; __utmv=30149280.9805; __yadk_uid=E22dC5IWLCUZnSLHYeg5Py3gD4nOk6zf; __utmz=30149280.1550054125.9.8.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1550202696%2C%22https%3A%2F%2Fbook.douban.com%2Fsubject%2F1474824%2F%22%5D; _pk_id.100001.8cb4=30addd92e79163c2.1546515350.4.1550202696.1548760951.; _pk_ses.100001.8cb4=*; __utma=30149280.447792835.1546515355.1550054125.1550202699.10; __utmc=30149280; __utmt=1; __utmb=30149280.1.10.1550202699; dbcl2="98051128:nOE4qQ8kuRQ"'
cookie = 'll="108090"; bid=BgSb5tqTgFg; _vwo_uuid_v2=D08B09F574612204835748D649E5182F3|d9376f8e3fe939ae6f67f8fc29fd8f58; viewed="1474824"; gr_user_id=1740613b-3148-4936-84d2-037f168725f4; __yadk_uid=YteEtMSpwQSN3qsfuzHA0BsQRxlGMVJf; push_noty_num=0; push_doumail_num=0; __utmv=30149280.9805; Hm_lvt_6e5dcf7c287704f738c7febc2283cf0c=1547085934; __utmz=30149280.1550054125.9.8.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmc=30149280; dbcl2="98051128:nOE4qQ8kuRQ"; ck=etnL; ap_v=0,6.0; __utma=30149280.447792835.1546515355.1550202699.1550214901.11; __utmt=1; douban-profile-remind=1; __utmt_douban=1; __utmb=30149280.5.10.1550214901; __utma=81379588.455446908.1547084957.1550054125.1550214918.8; __utmc=81379588; __utmz=81379588.1550214918.8.8.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/people/98051128/; __utmb=81379588.1.10.1550214918; _pk_ref.100001.3ac3=%5B%22%22%2C%22%22%2C1550214919%2C%22https%3A%2F%2Fwww.douban.com%2Fpeople%2F98051128%2F%22%5D; _pk_id.100001.3ac3=c1fef8fa844f4838.1547084957.8.1550214919.1550054126.; _pk_ses.100001.3ac3=*'
send_headers = {
    'Host': 'www.douban.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Connection': 'keep-alive',
    'Cookie': cookie
}

req = urllib2.Request(url, headers=send_headers)
page = urllib2.urlopen(req)

soup = BeautifulSoup(page, 'html.parser')
print soup.original_encoding
print (soup).encode('utf-8')

file = open("title.html", "w")
file.write(str(soup))
file.close()
print 'ok'
