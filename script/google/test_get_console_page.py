from bs4 import BeautifulSoup
import urllib2
import time

#url = 'https://play.google.com/apps/publish/?account=8505122062204140606#AndroidMetricsErrorsPlace:p=com.mobile.security.antivirus.applock.wifi&appid=4972898036482753524&appVersion=PRODUCTION&errorType=ANR&clusterName=apps/com.mobile.security.antivirus.applock.wifi/clusters/b0e07d72&detailsAppVersion=PRODUCTION&detailsSpan=7'

url = 'https://play.google.com/apps/publish/?account=8505122062204140606#AndroidMetricsErrorsPlace:p=com.mobile.security.antivirus.applock.wifi&appid=4972898036482753524&appVersion=PRODUCTION&errorType=ANR'

cookie = '_ga=GA1.3-3.913382795.1548983425; _gid=GA1.3-3.1421209840.1551074128; NID=160=RSnjE7DCQyhSiu2fl_aR75779X7RqCcBUZqhus2guwQFRzOS0F2FAF3s4lC9L-fubU_l4vMTxluBPe20dPNqTUbLIZu6q_-HLCuNywcJMSYYl4n4bFEFw87v43fr7DusvYzu0FtPml7-dWkvE7DteKS3SjZPonE7C7Yp0ISV3WBFEWRi7VNuQr85dyjBUMkba6IRbeSCR-N2YahuhrIMnRLSzPV5ly5xH7lij1wK; SID=EwerY7rF6XWb9Np-RZ978hJLGF0jANsUxyW223nr2UcOZ_C6L-_QaC2UvlWRvUrHl2Po1g.; HSID=AnzwbTrNyM_yUwHIR; SSID=ADh111VjUq7v5SlCM; APISID=2g6lVbCV5Dv84_mS/AuxLpgoZXzZ4cqxJy; SAPISID=rsq9wWAKoyAvOKkv/Ano_OFj4YMBLsTBq_; SIDCC=AN0-TYuQFHPmeaUw_EwlXVXMR-EEvdTwFZn3Nr8oo8Katqe-Df6kOaaRw4oRdp4u_XcW4RLcVlk; 1P_JAR=2019-2-18-6; _ga=GA1.3.317551693.1550462451'
send_headers = {
    'Host': 'play.google.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Connection': 'keep-alive',
    'Cookie': cookie
}

req = urllib2.Request(url, headers=send_headers)
time.sleep(5)
page = urllib2.urlopen(req)

soup = BeautifulSoup(page, 'lxml')
#print soup.original_encoding
#print (soup).encode('utf-8')

file = open("titles.html", "w")
file.write(str(soup))
file.close()
print 'ok'
