# import itchat
# import requests
#
# def get_response(msg):
#     apiUrl='http://openapi.tuling123.com/openapi/api/v2'
#     data={
#         'key':'f7ccdfdca20e4caa83e9490bf9fe1ea8',
#         'info':msg,
#         'userid':'晴川',
#     }
#     r=requests.post(apiUrl,data=data).json()  #发送post请求
#     return r.get('text')
#
# @itchat.msg_register(itchat.content.TEXT)     #接收消息
# def print_content(msg):
#     return get_response(msg['Text'])
#
# @itchat.msg_register([itchat.content.TEXT],isGroupChat=True) #接收群消息
# def print_content(msg):
#     return get_response(msg['Text'])
#
# itchat.auto_login(True)
# itchat.run()

import requests
import itchat
import json
import time
KEY='f7ccdfdca20e4caa83e9490bf9fe1ea8' #这个key也是你注册获得的。

def robot(input):
    apiUrl = 'http://openapi.tuling123.com/openapi/api/v2'
    datas={
        "reqType": 0,
        "perception": {
            "inputText": {
                "text": input
            },
            "inputImage": {
                "url": "imageUrl"
            },
            "selfInfo": {
                "location": {
                    "city": "xxx",
                }
            }
        },
        "userInfo": {
            "apiKey": ""+KEY,
             "userId": "userid" #这个是你申请到的userid
                      # "userId":"1"
        }
    }
    datas = json.dumps(datas)
    result= requests.post(apiUrl, data=datas).json()
    result=result.get('results')[0].get('values').get('text')
    return result
while True:   ####用于测试
    inputs=input('A:')
    info =robot(inputs)
    print(info)


face_engine = cv.CascadeClassifier("C:\\Users\\Lenovo\\anaconda3\\envs\\tensorflow\\Library\\etc\\haarcascades\\haarcascade_frontalface_default.xml")
eye_engine = cv.CascadeClassifier("C:\\Users\\Lenovo\\anaconda3\\envs\\tensorflow\\Library\\etc\\haarcascadeshaarcascade_eye.xml")
smile_engine = cv.CascadeClassifier("C:\\Users\\Lenovo\\anaconda3\\envs\\tensorflow\\Library\\etc\\haarcascades\\haarcascade_smile.xml")