from wordcloud import WordCloud
import collections
import jieba
import re
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import os

# 读取数据
with open('122.txt',encoding='utf-8') as f:
    data = f.read()
# 文本预处理  去除一些无用的字符   只提取出中文出来
result_list = []
# 文本分词
seg_list_exact = jieba.cut(data, cut_all=True)

for word in seg_list_exact:
    # 设置停用词并去除单个词
        result_list.append(word)


# 筛选后统计词频
word_counts = collections.Counter(result_list)
# path = 'D:/blibli/wordcloud/'
path = 'D:/blibli/wholewordcloud/'

img_files = os.listdir('D:/blibli/whole')
print(img_files)
for num in range(1, 3668):
    img = fr'D:/blibli/whole/mask_{num}.png'
    # 获取蒙版图片
    mask_ = 255 - np.array(Image.open(img))
    # 绘制词云
    plt.figure(figsize=(8, 5), dpi=200)
    my_cloud = WordCloud(
        background_color='cyan',  # 设置背景颜色  默认是black
        mask=mask_,      # 自定义蒙版
        mode='RGBA',
        max_words=500,
        font_path='simhei.ttf',   # 设置字体  显示中文
    ).generate_from_frequencies(word_counts)

    # 显示生成的词云图片
    plt.imshow(my_cloud)
    # 显示设置词云图中无坐标轴
    plt.axis('off')
    word_cloud_name = path + 'wordcloud_{}.png'.format(num)
    my_cloud.to_file(word_cloud_name)    # 保存词云图片
    print(f'======== 第{num}张词云图生成 ========')