# 爬虫测试
# 导入包
import time

import requests
import re
import os

# 获取总网站标签
str1=requests.get("http://www.cgtpw.com/")
#先打看一下有没有问题
# print(url0)
# 使用正表达式获取标签网址（或许的是截取的网址编号）
list0=re.findall('<a href="/xgmn/(.*?).html".*?>.*?',str1.text)
# 12876  print(list0)测试获取是否异常
list1=list(set(list0))
# 遍历数组拼接网址，并开始下载图片
for list2 in list1:
    url='http://www.cgtpw.com/xgmn/'+list2+'.html'
    # 以下在循环中频繁下载图片
    # 放入网址请求网页代码


    # 第一步获取当前网页的页数
    request=requests.get(url)
    # 防止网页中文乱码
    request.encoding = request.apparent_encoding
    url5=request.text
    # 打印网页确定没问题
    # print(url)
    # <a>共26页: </a>
    # 获取其他页面
    num=int(re.findall('<a>共(.*?)页: </a>',url5)[-1])
    for tmp in range(1,num+1):
        if tmp==1:
            url6=url
            print(url6+"下载中......")
        else:
            url6='http://www.cgtpw.com/xgmn/'+str(list2)+"_"+str(tmp)+".html"
            print(url6+"下载中......")
        #循环遍历当前页面的剩余页数
        #



        # 放入网址请求网页代码
        request=requests.get(url6)
        # 防止网页中文乱码
        request.encoding = request.apparent_encoding
        url7=request.text
        # http://www.cgtpw.com/d/file/xgmn/2021-09-24/77facce807db31adf8fa1cbb5697df9e.jpg
        # <p align="center"><img src="http://www.cgtpw.com/d/file/xgmn/2021-09-24/0ecb8131ac2233c62ce7d79a1800d338.jpg" alt="" /></p>
        # <p align="center"><img src="http://www.cgtpw.com/d/file/xgmn/2021-09-24/06813ae67721981acba4feffd8cd7e00.jpg" alt="" /></p>
        # 创建标题名称作为文件夹
        dir_name=re.findall('<h1>(.*?)</h1>',url7)[-1]
        # 创建文件夹
        if not os.path.exists('C:\mn\\'+dir_name):
            os.mkdir('C:\mn\\'+dir_name)
        # 匹配到所有的图片地址
        list=re.findall('<p align="center"><img src="(.*?)" alt="" /></p>',url7)
        # 遍历下载
        for txt in list:
            # time.sleep(1)
            file_name=txt.split('/')[-1]
            request= requests.get(txt)
            with open('C:\mn\\'+dir_name+'/'+file_name,'wb') as f:
                f.write(request.content)






