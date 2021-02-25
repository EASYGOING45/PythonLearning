import json,re,datetime
import requests,itchat,sxtwl
def getYMD():      #获得对应的农历
    ymc = [u"十一", u"十二", u"正", u"二", u"三", u"四", u"五", u"六", u"七", u"八", u"九", u"十"]
    rmc = [u"初一", u"初二", u"初三", u"初四", u"初五", u"初六", u"初七", u"初八", u"初九", u"初十",
           u"十一", u"十二", u"十三", u"十四", u"十五", u"十六", u"十七", u"十八", u"十九",
           u"二十", u"廿一", u"廿二", u"廿三", u"廿四", u"廿五", u"廿六", u"廿七", u"廿八", u"廿九", u"三十", u"卅一"]
    Gan = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
    Zhi = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]
    ShX = ["鼠", "牛", "虎", "兔", "龙", "蛇", "马", "羊", "猴", "鸡", "狗", "猪"]
    numCn = ["天", "一", "二", "三", "四", "五", "六", "七", "八", "九", "十"]
    lunar = sxtwl.Lunar()
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    rday = datetime.datetime.now().day
    day = lunar.getDayBySolar(year, month, rday)
    d = str(day.y) + "年" + str(day.m) + "月" + str(day.d) + "日"
    if day.Lleap:
        a = "润" + ymc[day.Lmc] + "月" + rmc[day.Ldi] + "日"
    else:
        a = ymc[day.Lmc] + "月" + rmc[day.Ldi] + "日"
    b = "星期" + numCn[day.week]
    c = Gan[day.Lyear2.tg] + Zhi[day.Lyear2.dz] + "年" + Gan[day.Lmonth2.tg] + Zhi[day.Lmonth2.dz] + "月" + Gan[
        day.Lday2.tg] + Zhi[day.Lday2.dz] + "日"
    txt = '今天日期：'+d + ', ' + b + '\n'+'中华农历: ' + a + ', ' + c
    return txt

print(getYMD())

def get_iciba_everyday_chicken_soup(xingming):
    url = 'http://open.iciba.com/dsapi/'
    r = requests.get(url)
    all = json.loads(r.text)
    Englis = all['content']
    Chinese = all['note']
    everyday_soup = '@喝一碗'+xingming+'的心灵鸡汤(^_^):'+'\n'+Englis+'\n'+Chinese+'\n'
    return everyday_soup

print(get_iciba_everyday_chicken_soup("易行"))

def getURLcode(location):#获取城市对应的代码
    url = "http://www.weather.com.cn/forecast/"
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    txt = r.text
    loc = re.findall(r' target="_blank">[\u4e00-\u9fa5]{1,5}?</a></li>', txt)
    cod = re.findall(r' <li><a href="http://www.weather.com.cn/weather1d/[0-9]{9}.shtml"', txt)
    loca, loca_1, code, code_1 = [], [], [], []
    a_cdict = {}
    for item in loc:
        loca.append(re.findall(r'target="_blank">(.*?)</a></li>', item))
    for i in range(len(loca)):
        loca_1.append(loca[i][0])
    loca_1.insert(47, '固原')#这个城市没有爬取到
    for item in cod:
        code.append(re.findall(r'[0-9]{9}', item))
    for i in range(len(code)):
        code_1.append(code[i][0])
    a_cdict = dict(zip(loca_1, code_1))
    return str(a_cdict[location])

city_code=getURLcode("西安")

def getURL(code):#获取城市对应的链接
    url = 'http://www.weather.com.cn/weather/'+code+'.shtml'
    return url


city_html=getURL(city_code)

def geturltext(xingming,html):#获取天气情况
    r = requests.get(html)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    tx = r.text
    aim = re.findall(r'<input type="hidden" id="hidden_title" value="(.*?)月(.*?)日(.*?)时(.*?) (.*?)  (.*?)  (.*?)"', tx)
    airdata = re.findall(r'<li class="li6">\n<i></i>\n<span>(.*?)</span>\n<em>(.*?)</em>\n<p>(.*?)</p>', tx)
    ult_index = re.findall(r'<li class="li1">\n<i></i>\n<span>(.*?)</span>\n<em>(.*?)</em>\n<p>(.*?)</p>\n</li>', tx)
    cloth_index = re.findall(r'<i></i>\n<span>(.*?)</span>\n<em>(.*?)</em>\n<p>(.*?)</p>\n</a>\n</li>\n<li class="li4">', tx)
    wash_index = re.findall(r'<li class="li4">\n<i></i>\n<span>(.*?)</span>\n<em>(.*?)</em>\n<p>(.*?)</p>', tx)
    txt1 = '@看一看'+xingming+'的天气预报(^_^):'+'\n'+getYMD()+'\n'
    txt2 = '天气情况: '+aim[0][5]+'\n'+'温度情况: '+aim[0][6]+'\n'
    # txt3 = '空气指数: '+airdata[0][0]+', '+airdata[0][2]+'\n'
    txt4 = '紫外线指数: '+ult_index[0][0]+', '+ult_index[0][2]+'\n'
    # txt5 = '穿衣指数: '+cloth_index[0][0]+', '+cloth_index[0][2]+'\n'
    # txt6 = '洗车指数: '+wash_index[0][0]+', '+wash_index[0][2]+'\n'
    txt = '\n'+txt1+txt2+txt4
    return txt

print(geturltext("易行",city_html))

def sentauto(nicheng,txt):
    itchat.auto_login()
    result = itchat.search_friends(nickName=nicheng)
    user_name = result[0]['UserName']
    itchat.send_msg(txt, user_name)

def main():
    print("-"*30+'程序使用说明'+"-"*30)
    print('此程序功能在于发送给固定的一人，每天双击运行扫描就可以发送天气预报以及中英文每日一句')
    print('1、数据来源：中国天气网（可能有些城市天气网上搜不到），爱词霸每日一句')
    print('2、只能使用昵称来搜索，微信号不可用。如果昵称有特殊字符，直接在微信下复制即可')
    print('3、只能发给一个人，一个人，一个人！不要三心二意')
    print('4、输完信息后会弹出二维码，微信扫一扫即可以发送成功')
    print("-" * 30 + '程序使用说明' + "-" * 30)
    xingming = input('你想以何种称呼发送此信息：')
    location = input('您的地点（不要输入‘市’字）用于查询天气情况：')
    nicheng = input('请输入对方的微信昵称（请确保昵称正确，否则查不到）:')
    code = getURLcode(location)
    html = getURL(code)
    text = get_iciba_everyday_chicken_soup(xingming)+geturltext(xingming,html)
    # sentauto(nicheng,text)
    return text

print(main())