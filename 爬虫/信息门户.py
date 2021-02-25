import re
from bs4 import BeautifulSoup
from pip._vendor import requests

url="http://bkjw.chd.edu.cn/eams/courseTableForStd!courseTable.action"

r = requests.get(url)
r.encoding=r.apparent_encoding

print(r.text)