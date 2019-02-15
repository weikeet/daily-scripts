from bs4 import BeautifulSoup
import urllib2

#url = 'https://play.google.com/apps/publish/?account=8505122062204140606#AndroidMetricsErrorsPlace:p=com.mobile.security.antivirus.applock.wifi&appid=4972898036482753524&appVersion=PRODUCTION&errorType=ANR&clusterName=apps/com.mobile.security.antivirus.applock.wifi/clusters/b0e07d72&detailsAppVersion=PRODUCTION&detailsSpan=7'
url = 'https://play.google.com/apps/publish/?account=8505122062204140606#AndroidMetricsErrorsPlace:p=com.mobile.security.antivirus.applock.wifi&appid=4972898036482753524&appVersion=PRODUCTION&errorType=ANR'
cookie = '_ga=GA1.3-3.913382795.1548983425; _gid=GA1.3-3.1279545592.1550059544; NID=160=NyZLPM6CMZJ-RhaBGHbJqlujH4C9WJcEzKwF8AX20-I3r3Ay1u5DIZ8Fx8RYXWS5r7XVy2G9MkD-WwzMj9KyY33NaZNVOshd3Ua6NYWRE2N-msF8jiBwF345wgkcwtLgLNprI2uByZDcoLPOIsN0fV_d_594ceZoC0-zKE-8k_3pG1dv8jOlE09y1vTYYYD37wOZbiZQZKWq6s4Eh3DWuOz2WTalrQzUF1nHK2Ys; SID=EwerY7rF6XWb9Np-RZ978hJLGF0jANsUxyW223nr2UcOZ_C6L-_QaC2UvlWRvUrHl2Po1g.; HSID=AnzwbTrNyM_yUwHIR; SSID=ADh111VjUq7v5SlCM; APISID=2g6lVbCV5Dv84_mS/AuxLpgoZXzZ4cqxJy; SAPISID=rsq9wWAKoyAvOKkv/Ano_OFj4YMBLsTBq_; SIDCC=AN0-TYvYVSA3b39zsHEcIDhC3Umo7GF5iPovy7IIFSK7ARLIhAEd6Ghfaof5_gsbPMhCkbAuD5I; 1P_JAR=2019-02-01-09'

send_headers = {
    'Host': 'play.google.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Connection': 'keep-alive',
    'Cookie': cookie
}

req = urllib2.Request(url, headers=send_headers)
page = urllib2.urlopen(req)

soup = BeautifulSoup(page, 'lxml')
#print soup.original_encoding
#print (soup).encode('utf-8')

file = open("titles.html", "w")
file.write(str(soup))
file.close()
print 'ok'
