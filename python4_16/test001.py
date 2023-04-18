# 爬虫测试
# 导入包
import time

import requests
import re
import os
# 放入网址请求网页代码
request=requests.get("http://www.cgtpw.com/xgmn/12866.html")
# 防止网页中文乱码
request.encoding = request.apparent_encoding
url5=request.text
# 打印网页确定没问题
# print(url)
# <a>共26页: </a>
# 获取其他页面
num=int(re.findall('<a>共(.*?)页: </a>',url5)[-1]);
for tmp in range(1,num+1):
    if tmp==1:
        url6="http://www.cgtpw.com/xgmn/12866.html"
    else:
        url6="http://www.cgtpw.com/xgmn/12866_"+str(tmp)+".html"
    print(url6)
# http://www.cgtpw.com/d/file/xgmn/2021-09-24/77facce807db31adf8fa1cbb5697df9e.jpg
# <p align="center"><img src="http://www.cgtpw.com/d/file/xgmn/2021-09-24/0ecb8131ac2233c62ce7d79a1800d338.jpg" alt="" /></p>
# <p align="center"><img src="http://www.cgtpw.com/d/file/xgmn/2021-09-24/06813ae67721981acba4feffd8cd7e00.jpg" alt="" /></p>
    request=requests.get(url6)
    # 防止网页中文乱码
    request.encoding = request.apparent_encoding
    url6=request.text
    dir_name=re.findall('<h1>(.*?)</h1>',url6)[-1]

    # 创建文件夹
    if not os.path.exists('C:\mn\\'+dir_name):
        os.mkdir('C:\mn\\'+dir_name)

    list=re.findall('<p align="center"><img src="(.*?)" alt="" /></p>',url6)
    for txt in list:
        time.sleep(1)
        file_name=txt.split('/')[-1]
        request= requests.get(txt)
        with open('C:\mn\\'+dir_name+'/'+file_name,'wb') as f:
            f.write(request.content)





