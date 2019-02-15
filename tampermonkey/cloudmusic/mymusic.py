from bs4 import BeautifulSoup
import urllib2

url = 'https://music.163.com/#/user/home?id=67978110'

cookie = '_ntes_nnid=e0de828ac938ca52f2296b00b1c82ae8,1543543189293; _ntes_nuid=e0de828ac938ca52f2296b00b1c82ae8; _iuqxldmzr_=32; __utma=94650624.1634711043.1546516821.1546516821.1546516821.2; __utmz=94650624.1546516821.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; WM_TID=Wq%2FiGuzgz0lAREAVVUY80BJKxyO7ceK7; JSESSIONID-WYYY=2MRQxWFBN%5Cm49z2SH0czvEAd1ZgDP%5Cxloo2qZf0wVHtw3RwSAb71fsHmbsEgpotvTz4nmkFBsXz%2B%2BWKEcHob4Q0Ov%2FMvSTiW%2BmUh%2Bh3l2kvYe4M4dTdTp980wD8e2cOmA8%2FEjAaQIBVRV8aH1Eaw6crVoFSf0vgFkBgzCurkaCgM8fV6%3A1550218471299; WM_NI=PNE8nhQce2GcMIApkPl3ntt0TgEYsOpHawo%2FfNFGbofhp5VwvjB0I45NmJJOOt1kM4dRwlq52NIMOTd8WrLdPd30hfJOdt8HCtxs381Rhcyo9KOgQVFc6KEyYo5HjnkuT3M%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee94bb4a83b3bed3b86db59a8eb7d84f929e8ababc3b89e88eb3f44789949cd3ee2af0fea7c3b92a94928bd9ed6493bdabd3c6698f978f91ea5cb0eda295f73c98b98bbaf245b498af98ee25a6928aa8e165a6b8c0d6d57db6b68ed1cc40f792a3abc9458dacff8cd040a88eb98df43ff29287aece60a8e89993cf7094bcfdd1eb6e8a91ac95bb4481acb894b234f38ea884fc65fb958188d45e86bdfaacc8739bb1fba9e966a9ab9cd4d037e2a3; MUSIC_U=0e7bb3facdf25553f3831a007749b6f0baeec9256304ac960ed4f2afbe309be207f8c64ebba3756d5e124b1fc7558dd241049cea1c6bb9b6; __remember_me=true; __csrf=570d1382505a0da753e9931003988476'
#cookie ='ll="108090"; bid=BgSb5tqTgFg; _vwo_uuid_v2=D08B09F574612204835748D649E5182F3|d9376f8e3fe939ae6f67f8fc29fd8f58; viewed="1474824"; gr_user_id=1740613b-3148-4936-84d2-037f168725f4; push_noty_num=0; push_doumail_num=0; __utmv=30149280.9805; __yadk_uid=E22dC5IWLCUZnSLHYeg5Py3gD4nOk6zf; __utmz=30149280.1550054125.9.8.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1550202696%2C%22https%3A%2F%2Fbook.douban.com%2Fsubject%2F1474824%2F%22%5D; _pk_id.100001.8cb4=30addd92e79163c2.1546515350.4.1550202696.1548760951.; _pk_ses.100001.8cb4=*; __utma=30149280.447792835.1546515355.1550054125.1550202699.10; __utmc=30149280; __utmt=1; __utmb=30149280.1.10.1550202699; dbcl2="98051128:nOE4qQ8kuRQ"'

send_headers = {
    'Host': 'music.163.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Connection': 'keep-alive',
    'Cookie': cookie
}

req = urllib2.Request(url, headers=send_headers)
page = urllib2.urlopen(req)

soup = BeautifulSoup(page, 'html.parser')
#print soup.original_encoding
#print (soup).encode('utf-8')

file = open("result.html", "w")
file.write(str(soup))
file.close()
print 'ok'
