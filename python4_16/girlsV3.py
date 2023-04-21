#改脚本爬取网站上所有的美女图片,爬其他正规网站图片容易犯法
#<a href="/xgmn/" title="性感美女">性感美女</a>
#<a href="/qcmn/" title="清纯美女">清纯美女</a>
#<a href="/nymn/" title="内衣美女">内衣美女</a>

import requests
import re
import os

class StaticPicture:
    '此类针对取静态页面图片的处理'
    num1=0#记录网址总数
    num2=0
    # 最开始获取总网站对应规则的标签
    # 1.获取总网站主页中首次跳转的一级目录(一共九个)
    def get_one_catalog(self,url:str,ze:str):
        #再套一层取首页网站上面的三个标签网址并做好拼接
        one_catalog=[]
        str1=requests.get(url)
        # print(str1)
        #使用固定模块进行解码
        # print(str1.text.replace(';', '').replace('&#x', '\\u').encode('utf-8').decode('unicode_escape'))
        # 使用正表达式获取网页中需要的标签网址（或许的是截取的网址编号）
        list0=re.findall(ze,str1.text.replace(';', '').replace('&#x', '\\u').encode('utf-8').decode('unicode_escape'))#固定格式解码*#x
        # print(list0)
        list1=list(set(list0)) #去重
        # 遍历数组拼接网址，并开始下载图片
        for list2 in list1:
            url1='http://www.cgtpw.com'+list2
            one_catalog.append(url1)
            # 以下在循环中频繁下载图片
            # 放入网址请求网页代码
        return one_catalog
    #根据总网站获取总网站目录下面所有的网址

    #2.根据首次跳转的一级目录获取全部的一级目录（取页数进行拼接）
    # 根据传入地址获取所有页数的地址和匹配出对应页数的正则
    # ze1:获取页数的正则 ze2：涉及url重命名的正则,徐娅拼接的正则
    def get_one_catalog_sum(self,url:str,ze1:str):
        one_catalog_sum=[]
        #http://www.cgtpw.com/ctmn/
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
                one_catalog_sum.append(url6)
            else:#这部分需要自定义，每个网址规律不一样
                url6=url+'index_'+str(tmp)+".html"
                one_catalog_sum.append(url6)
            #循环遍历当前页面的剩余页数
        return one_catalog_sum
    #3.根据一级目录获取二级目录
    def get_two_catalog(self,url:str,ze:str):
        #再套一层取首页网站上面的三个标签网址并做好拼接
        two_catalog=[]
        str1=requests.get(url)
        # print(str1)
        #使用固定模块进行解码
        # print(str1.text.replace(';', '').replace('&#x', '\\u').encode('utf-8').decode('unicode_escape'))
        # 使用正表达式获取网页中需要的标签网址（或许的是截取的网址编号）
        list0=re.findall(ze,str1.text)
        # print(list0)
        list1=list(set(list0)) #去重
        # 遍历数组拼接网址，并开始下载图片
        for list2 in list1:
            url1='http://www.cgtpw.com'+list2
            two_catalog.append(url1)
            # 以下在循环中频繁下载图片
            # 放入网址请求网页代码
        return two_catalog
    #4.根据二级目录获取隐藏部分的二级目录
    # 根据传入地址获取所有页数的地址和匹配出对应页数的正则
    # ze1:获取页数的正则 ze2：涉及url重命名的正则,徐娅拼接的正则
    def get_two_catalog_sum(self,url:str,ze1:str,ze2):
        two_catalog_sum=[]
        list2=re.findall(ze2,url)[-1]
        # 第一步获取当前网页的html内容
        request=requests.get(url)
        # 防止网页中文乱码
        request.encoding = request.apparent_encoding
        html=request.text
        #获取其他页面(排除索引越界问题)
        tmp1=re.findall(ze1,html)
        if len(tmp1)==0:
            url6=url
            two_catalog_sum.append(url6)
        else:
            num=int(re.findall(ze1,html)[-1])
            # 定义循环读取拼接所有网址
            for tmp in range(1,num+1):
                if tmp==1:
                    url6=url
                    two_catalog_sum.append(url6)
                else:#这部分需要自定义，每个网址规律不一样
                    url6=str(list2)+"_"+str(tmp)+".html"
                    two_catalog_sum.append(url6)
                #循环遍历当前页面的剩余页数
        return two_catalog_sum

    # 自定义文件夹名称(  网页地址，  文件夹名称，  文件夹正则, 路径文件正则)
    def dir_name (self,url:str,dir_name:str,ze1:str,lujing:str):
        list2=re.findall('http://www\.cgtpw\.com/(.*?)/.*?\.html',url)[-1]
        if len(url) ==0:
            return lujing+dir_name
        else:
            request=requests.get(url)
            request.encoding = request.apparent_encoding
            html=request.text

            return lujing+list2+'\\'+re.findall(ze1,html)[-1]

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




# # 从首页获取所有相关的网页地址（匹配地址的规则需要自定义）
# t=StaticPicture()
# #获取首页几大模块的网址（目前八个）
# one_catalog=t.get_one_catalog("http://www.cgtpw.com/",'<a href="(.*?)" title=".{4,5}">.{4,5}</a>')
# print(one_catalog)
# one_catalog_sum=t.get_one_catalog_sum('http://www.cgtpw.com/jpmn/','<li><a href="/'+str(re.findall('http://www.cgtpw.com/(.*?)/','http://www.cgtpw.com/jpmn/')[-1])+'/index_(\d*?)\.html">尾页</a><li>')
# print(one_catalog_sum)
# two_catalog=t.get_two_catalog('http://www.cgtpw.com/ctmn/index_2.html','<a href="(.*?)" title=".*?" target=".*?"><img src=.*? alt=".*?"></a>')
# print("------------------")
# print(two_catalog)
# print("=====================")
# urls=t.get_two_catalog_sum('http://www.cgtpw.com/ctmn/12600.html','<a>共(.*?)页: </a>','(.*?).html')
# print(urls)
# print("++++++++++++++++++++")
# print(t.dir_name('http://www.cgtpw.com/ctmn/12600.html',"",'<h1>(.*?)</h1>','D:\\mn\\'))
#########################################################################################################
# 获取首页几大模块的网址（目前八个）
t=StaticPicture()
sum_list5=[]
one_catalog=t.get_one_catalog("http://www.cgtpw.com/",'<a href="(.*?)" title=".{4,5}">.{4,5}</a>')#获取首页8个目录下当页一级目录
print(one_catalog)
for list1 in one_catalog:
    one_catalog_sum=t.get_one_catalog_sum(list1,'<li><a href="/'+str(re.findall('http://www.cgtpw.com/(.*?)/',list1)[-1])+'/index_(\d*?)\.html">尾页</a><li>')#获取8个目录下所有的一级目录
    for list2 in one_catalog_sum:
        two_catalog=t.get_two_catalog(list2,'<a href="(.*?)" title=".*?" target=".*?"><img src=.*? alt=".*?"></a>')#获取一级目录下面当页的二级目录
        for list3 in two_catalog:
            print(sum_list5)
            sum_list5=t.get_two_catalog_sum(list3,'<a>共(.*?)页: </a>','(.*?).html')#取一级目录下面所有的二级目录

t.num1=len(sum_list5)
#             for list4 in two_catalog_sum:
#                 dir_name=t.dir_name(list4,"",'<h1>(.*?)</h1>','D:\\mn\\')
#                 t.num2=t.num2+1
#                 print("下载总进度"+str(t.num2)+'/'+str(t.num1))
#                 t.downLoad(list4,dir_name,'<p align="center"><img src="(.*?)" alt="" /></p>')
################################################################################################

#####################################只下载xxmn
# t=StaticPicture()
# sum_list=[]
# two_catalog=t.get_two_catalog('http://www.cgtpw.com/xgmn/','<a href="(.*?)" title=".*?" target=".*?"><img src=.*? alt=".*?"></a>')#获取一级目录下面当页的二级目录
# for list3 in two_catalog:
#     two_catalog_sum=t.get_two_catalog_sum(list3,'<a>共(.*?)页: </a>','(.*?).html')#取一级目录下面所有的二级目录
#     t.num1=len(two_catalog_sum)
#     for list4 in two_catalog_sum:
#         dir_name=t.dir_name(list4,"",'<h1>(.*?)</h1>','D:\\mn\\')
#         t.num2=t.num2+1
#         print("下载总进度"+str(t.num2)+'/'+str(t.num1))
#         t.downLoad(list4,dir_name,'<p align="center"><img src="(.*?)" alt="" /></p>')