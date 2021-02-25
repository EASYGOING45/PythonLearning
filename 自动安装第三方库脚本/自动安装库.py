'''
第三方库的自动安装
通过os.system("  ")去自动输入命令行代码
'''
import os
libs={"numpy","matplotlib","pillow","sklearn"}
try:
    for lib in libs:
        os.system("pip install "+lib)
        print("Successful")
except:
    print("Failed Somehow")