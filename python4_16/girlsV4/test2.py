import requests
import requests
import re
import os
headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.48'
}
class StaticPicture:
    ze=''
    num1=0#记录网址总数
    num2=0
    # 自定义文件夹名称(  网页地址，    网页内容 ,文件夹名称，  文件夹正则, 路径文件正则)
    def dir_name (self,url:str,request,dir_name:str,ze1:str,lujing:str):
        html=request.text
        list2=re.findall('http://www\.cgtpw\.com/(.*?)/.*?\.html',url)[-1]
        if len(url) ==0:
            return lujing+dir_name
        else:
            try:
                return lujing+list2+'\\'+re.findall(ze1,html)[-1]
            except:
                return ''
    # ze:符合条件的图片格式 <p align="center"><img src="(.*?)" alt="" /></p>
    #time:单次下载需要等待的时间单位为秒
    def downLoad(self,url:str,request,dir_name:str,ze:str):
        HTML=request.text
        list2=re.findall('http://www\.cgtpw\.com/(.*?)/.*?\.html',url)[-1]
        urls=[]
        # 创建文件夹
        if not os.path.exists(dir_name):
            try:
                os.mkdir(dir_name)
            except FileNotFoundError:
                os.makedirs(dir_name)
            except:
                dir_name='D:\\mn\\'+list2+'\\test'
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
            file_name=url.split('/')[-1]
            url=re.findall('(.*?)" .*?',url)[-1]
            try:
                file_name=re.findall('(.*?)" .*?',file_name)[-1]
            except:
                return ""
            str2=dir_name+'/'+file_name
            if  os.path.exists(str2):
                return ""
            else:
                request= requests.get(url)
                print("--------------")
                print(url)
                with open(dir_name+'/'+file_name,'wb') as f:
                    print("新增图片"+str2)
                    f.write(request.content)


t=StaticPicture()
line = 'http://www.cgtpw.com/bjnmn/575.html'
#通过URL获取到HTML内容
request=requests.get(line)
body=request
request.encoding = request.apparent_encoding
#下载图片
dir_name=t.dir_name(line,request,"",'<h1>(.*?)</h1>','D:\\mn\\')
t.num2=t.num2+1
print("下载总进度"+str(t.num2))
print(line)
t.downLoad(line,request,dir_name,'<img src="(.*?)" alt=".*?"( class=".*?"| /)>')


