# -*- coding: utf-8 -*-
import json
import pinyin
import requests
from bs4 import BeautifulSoup

res = requests.get('https://search.maven.org/artifact/com.airbnb.android/lottie')
# res = requests.get('https://mvnrepository.com/artifact/com.airbnb.android/lottie')
print(res.text)
