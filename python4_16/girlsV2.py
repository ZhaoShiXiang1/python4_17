import time
import requests
import re
import os

class StaticPicture:
    '此类针对取静态页面图片的处理'





    num1=0#记录网址总数
    num2=0
    # 最开始获取总网站对应规则的标签
    # 获取总网站标签
    def get_url_sum(self,url:str,ze:str):
         url_lists=[]
         str1=requests.get(url)
         print(str1)
         # 使用正表达式获取网页中需要的标签网址（或许的是截取的网址编号）
         list0=re.findall(ze,str1.text)
         # 12876  print(list0)测试获取是否异常
         list1=list(set(list0)) #去重
         # 遍历数组拼接网址，并开始下载图片
         for list2 in list1:
             url1='http://www.cgtpw.com/xgmn/'+list2+'.html'
             url_lists.append(url1)
             # 以下在循环中频繁下载图片
             # 放入网址请求网页代码
         return url_lists

    # 根据传入地址获取所有页数的地址和匹配出对应页数的正则
    # ze1:获取页数的正则 ze2：涉及url重命名的正则,徐娅拼接的正则
    def get_urls(self,url:str,ze1:str,ze2):

       list2=re.findall(ze2,url)[-1]
       # 第一步获取当前网页的html内容
       request=requests.get(url)
       # 防止网页中文乱码
       request.encoding = request.apparent_encoding
       html=request.text
    #获取其他页面
       num=int(re.findall(ze1,html)[-1])
       # 定义循环读取拼接所有网址
       for tmp in range(1,num+1):
           if tmp==1:
               url6=url
               url_list.append(url6)
           else:#这部分需要自定义，每个网址规律不一样
               url6='http://www.cgtpw.com/xgmn/'+str(list2)+"_"+str(tmp)+".html"
               url_list.append(url6)
           #循环遍历当前页面的剩余页数
       return url_list




    # 自定义文件名称(网页地址，文件夹名称，文件夹正则，文件名称，文件正则,路径)
    def dir_name (self,url:str,dir_name:str,ze1:str,lujing:str):
        if len(url) ==0:
            return lujing+dir_name
        else:
            request=requests.get(url)
            request.encoding = request.apparent_encoding
            html=request.text
            return lujing+re.findall(ze1,html)[-1]

    #下载文件的方法提供一个地址，文件夹路径，匹配网址的正则，单词下载等待的时间

    # ze:符合条件的图片格式 <p align="center"><img src="(.*?)" alt="" /></p>
    #time:单次下载需要等待的时间单位为秒
    def downLoad(self,url:str,dir_name:str,ze:str):
        # 创建文件夹
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)

        # 放入网址请求网页代码
        request=requests.get(url)
        # 防止网页中文乱码
        request.encoding = request.apparent_encoding
        HTML=request.text
        # 正则匹配到所有的图片地址
        urls=re.findall(ze,HTML)
        # 遍历下载
        for url in urls:
            print(url)
            #文件名称默认以后缀作为命名
            file_name=url.split('/')[-1]
            # time.sleep(time)
            request= requests.get(url)
            with open(dir_name+'/'+file_name,'wb') as f:
                f.write(request.content)




# 从首页获取所有相关的网页地址（匹配地址的规则需要自定义）
t=StaticPicture()
urls_lists=t.get_url_sum("http://www.cgtpw.com/",'<a href="/xgmn/(.*?).html".*?>.*?')
# 利用循环将页面其他隐藏页面网址全部获取
url_list =[]#存储网址
for lists in urls_lists :
    url_list=t.get_urls(lists,'<a>共(.*?)页: </a>','http://www.cgtpw.com/xgmn/(.*?).html')
t.num1=len(url_list)
for list3 in url_list:
    dir_name=t.dir_name(list3,"",'<h1>(.*?)</h1>','C:\mn\\')
    t.num2=t.num2+1
    print("下载总进度"+str(t.num2)+'/'+str(t.num1))
    t.downLoad(list3,dir_name,'<p align="center"><img src="(.*?)" alt="" /></p>')