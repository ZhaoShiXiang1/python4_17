#改脚本爬取网站上所有的美女图片,爬其他正规网站图片容易犯法
#<a href="/xgmn/" title="性感美女">性感美女</a>
#<a href="/qcmn/" title="清纯美女">清纯美女</a>
#<a href="/nymn/" title="内衣美女">内衣美女</a>
import random

import requests
import re
import os

class StaticPicture:
    '此类针对取静态页面图片的处理'
    ze=''
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
            try:
                return lujing+list2+'\\'+re.findall(ze1,html)[-1]
            except:
                return ''


    #下载文件的方法提供一个地址，文件夹路径，匹配网址的正则，单词下载等待的时间

    # ze:符合条件的图片格式 <p align="center"><img src="(.*?)" alt="" /></p>
    #time:单次下载需要等待的时间单位为秒
    def downLoad(self,url:str,dir_name:str,ze:str):
        urls=[]

        # 创建文件夹
        if os.path.exists(dir_name):
            if len(os.listdir(dir_name))==0:
                dir_name=dir_name
            else:
                return ''
        if not os.path.exists(dir_name):
            try:
                os.mkdir(dir_name)
            except FileNotFoundError:
                os.makedirs(dir_name)
            except:
                dir_name='D:\\mn\\xgmn\\test'

        # 放入网址请求网页代码
        request=requests.get(url,headers=headers)
        # 防止网页中文乱码
        request.encoding = request.apparent_encoding
        HTML=request.text
        # 正则匹配到所有的图片地址
        #加入判断根据判断调整正则格式
        tmp9=re.findall(ze,HTML)
        if len(tmp9)==0 and ze=='<img alt=".*?"(  | )src="(.*?)" />':
            ze='<img src="(.*?)" alt=".*?"( class=".*?"| /)>'
            tmp9=re.findall(ze,HTML)
        if len(tmp9)==0 and ze=='<img src="(.*?)" alt=".*?"( class=".*?"| /)>':
            ze='<img alt=".*?"(  | )src="(.*?)" />'
            tmp9=re.findall(ze,HTML)
        if ze=='<img alt=".*?"(  | )src="(.*?)" />':
            tmp5=1
        else:
            tmp5=0
        for tmp in tmp9:
            urls.append(tmp[tmp5])
        # 遍历下载
        for url in urls:
            # print(url)
            #文件名称默认以后缀作为命名
            file_name=url.split('/')[-1]
            # time.sleep(time)
            request= requests.get(url)
            try:
                with open(dir_name+'/'+file_name,'wb') as f:
                    f.write(request.content)
            except OSError:
                return ''




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
headers_list = [
            {
                'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
            }, {
                'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36'
            }, {
                'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36'
            }, {
                'user-agent': 'Mozilla/5.0 (iPad; CPU OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/87.0.4280.77 Mobile/15E148 Safari/604.1'
            }, {
                'user-agent': 'Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
            }, {
                'user-agent': 'Mozilla/5.0 (Linux; Android) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.109 Safari/537.36 CrKey/1.54.248666'
            }, {
                'user-agent': 'Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.188 Safari/537.36 CrKey/1.54.250320'
            }, {
                'user-agent': 'Mozilla/5.0 (BB10; Touch) AppleWebKit/537.10+ (KHTML, like Gecko) Version/10.0.9.2372 Mobile Safari/537.10+'
            }, {
                'user-agent': 'Mozilla/5.0 (PlayBook; U; RIM Tablet OS 2.1.0; en-US) AppleWebKit/536.2+ (KHTML like Gecko) Version/7.2.1.0 Safari/536.2+'
            }, {
                'user-agent': 'Mozilla/5.0 (Linux; U; Android 4.3; en-us; SM-N900T Build/JSS15J) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'
            }, {
                'user-agent': 'Mozilla/5.0 (Linux; U; Android 4.1; en-us; GT-N7100 Build/JRO03C) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'
            }, {
                'user-agent': 'Mozilla/5.0 (Linux; U; Android 4.0; en-us; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'
            }, {
                'user-agent': 'Mozilla/5.0 (Linux; Android 7.0; SM-G950U Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36'
            }, {
                'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G965U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36'
            }, {
                'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; SM-T837A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.80 Safari/537.36'
            }, {
                'user-agent': 'Mozilla/5.0 (Linux; U; en-us; KFAPWI Build/JDQ39) AppleWebKit/535.19 (KHTML, like Gecko) Silk/3.13 Safari/535.19 Silk-Accelerated=true'
            }, {
                'user-agent': 'Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; LGMS323 Build/KOT49I.MS32310c) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.0.0 Mobile Safari/537.36'
            }, {
                'user-agent': 'Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 550) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/14.14263'
            }, {
                'user-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Moto G (4)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
            }, {
                'user-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 10 Build/MOB31T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
            }, {
                'user-agent': 'Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
            }, {
                'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
            }, {
                'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5X Build/OPR4.170623.006) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
            }, {
                'user-agent': 'Mozilla/5.0 (Linux; Android 7.1.1; Nexus 6 Build/N6F26U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
            }, {
                'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 6P Build/OPP3.170518.006) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
            }, {
                'user-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 7 Build/MOB30X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
            }, {
                'user-agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows Phone 8.0; Trident/6.0; IEMobile/10.0; ARM; Touch; NOKIA; Lumia 520)'
            }, {
                'user-agent': 'Mozilla/5.0 (MeeGo; NokiaN9) AppleWebKit/534.13 (KHTML, like Gecko) NokiaBrowser/8.5.0 Mobile Safari/534.13'
            }, {
                'user-agent': 'Mozilla/5.0 (Linux; Android 9; Pixel 3 Build/PQ1A.181105.017.A1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.158 Mobile Safari/537.36'
            }, {
                'user-agent': 'Mozilla/5.0 (Linux; Android 10; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36'
            }, {
                'user-agent': 'Mozilla/5.0 (Linux; Android 11; Pixel 3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.181 Mobile Safari/537.36'
            }, {
                'user-agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
            }, {
                'user-agent': 'Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
            }, {
                'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 XL Build/OPD1.170816.004) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
            }, {
                'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1'
            }, {
                'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
            }, {
                'user-agent': 'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1'
            }
        ]

headers = random.choice(headers_list)
t=StaticPicture()
t.num1=272833
sum_list5=[]
# one_catalog=t.get_one_catalog("http://www.cgtpw.com/",'<a href="(.*?)" title=".{4,5}">.{4,5}</a>')#获取首页8个目录下当页一级目录
# print(one_catalog)
one_catalog=['http://www.cgtpw.com/xgmn/']
print(one_catalog)
for list1 in one_catalog:
    if list=='http://www.cgtpw.com/mnmx/'or list=='http://www.cgtpw.com/mnmx/':
        t.ze='<img alt=".*?"(  | )src="(.*?)" />'
    else:
        t.ze='<img src="(.*?)" alt=".*?"( class=".*?"| /)>'
    one_catalog_sum=t.get_one_catalog_sum(list1,'<li><a href="/'+str(re.findall('http://www.cgtpw.com/(.*?)/',list1)[-1])+'/index_(\d*?)\.html">尾页</a><li>')#获取8个目录下所有的一级目录
    for list2 in one_catalog_sum:
        two_catalog=t.get_two_catalog(list2,'<a href="(.*?)" title=".*?" target=".*?"><img src=.*? alt=".*?"></a>')#获取一级目录下面当页的二级目录
        for list3 in two_catalog:
            two_catalog_sum=t.get_two_catalog_sum(list3,'<a>共(.*?)页: </a>','(.*?).html')#取一级目录下面所有的二级目录
            fo = open("foo_3.txt", "a")
            for list4 in two_catalog_sum:
                fo.write(list4+'\n')
                dir_name=t.dir_name(list4,"",'<h1>(.*?)</h1>','D:\\mn\\')
                t.num2=t.num2+1
                print("下载总进度"+str(t.num2)+'/'+str(t.num1))
                t.downLoad(list4,dir_name,t.ze)
            fo.close()
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
# t.downLoad('http://www.cgtpw.com/mnmx/11677.html','test3','<img alt=".*?"(  | )src="(.*?)" />')