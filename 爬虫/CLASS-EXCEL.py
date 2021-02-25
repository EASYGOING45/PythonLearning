import  re
text=''
file=open('课表.txt',encoding='utf-8')
for line in file:
    text=text+line
r1=r'(?<=courseName =)(.+?)(?=")'
result=re.findall(r1,text)
print(result)
file.close()
