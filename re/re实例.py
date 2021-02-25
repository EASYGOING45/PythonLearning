import re

'''search'''
match=re.search(r'[1-9]\d{5}','BIT 100081')
if match:
    print(match.group(0))

'''match'''
new_match=re.match(r'[1-9]\d{5}','BIT 100081')
if match:
    match.group(0)
print(match.group(0))

'''findall'''
ls=re.findall(r'[1-9]\d{5}','BIT100081 TSU100084')

'''split'''
print("split方法测试")
print(re.split(r'[1-9]\d{5}','BIT100081 TSU100084'))
print("加入maxsplit之后")
print(re.split(r'[1-9]\d{5}','BIT100081 TSU100084',maxsplit=1))

'''finditer'''
for m in re.finditer(r'[1-9]\d{5}','BIT100081 TSU100084'):
    if m:
        print(m.group(0))

'''sub'''
print(re.sub(r'[1-9]\d{5}',':zipcode','BIT 100081'))

import re
pattern = re.compile('啦啦啦啊')
str = u''
print(pattern.search(str))
