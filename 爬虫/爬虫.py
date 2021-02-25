import  re
text=''
file=open('课表.txt',encoding='utf-8')
for line in file:
    text=text+line
r1=r'(?<=courseName =)(.+?)(?=;)'
class_name=re.findall(r1,text)
print(class_name)

r2=r'(?<=name:)(.+?)(?=",)'
class_teacher=re.findall(r2,text)
print(class_teacher)
file.close()
