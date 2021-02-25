import requests
import re

#根据Network中各个链接返回的内容来判断选择哪个链接
url = "http://bkjw.chd.edu.cn/eams/courseTableForStd!courseTable.action"

#根据General中的Request Method来判断用get方法还是post方法
#在这个项目中用到post，因此将下面的Form data传入,headers中要加入cookie
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75',
    'Cookie': 'semester.id=83; JSESSIONID=BD641358E30A3B284959865EFDA2B5FE.node1'
    }

data = {
        'ignoreHead': '1',
        'setting.kind': 'std',
        'startWeek': '',
        'semester.id': '83',
        'ids': '160790'
        }
r = requests.post(url,headers = headers,data = data)
r.encoding = r.apparent_encoding
html = r.text
print(html)













