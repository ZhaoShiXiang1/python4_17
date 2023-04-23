import requests
import requests
import re
import os

class StaticPicture:
  ze=''
  num1=0#记录网址总数
  num2=0
  # 自定义文件夹名称(  网页地址，    网页内容 ,文件夹名称，  文件夹正则, 路径文件正则)
  def dir_name (self,url:str,request,dir_name:str,ze1:str,lujing:str):
    request.encoding = request.apparent_encoding
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
    request.encoding = request.apparent_encoding
    HTML=request.text
    list2=re.findall('http://www\.cgtpw\.com/(.*?)/.*?\.html',url)[-1]
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
      print(url)
      file_name=url.split('/')[-1]
      try:
        file_name=re.findall('(.*?)" .*?',file_name)[-1]
      except:
        return ""
      print(file_name)
      with open(dir_name+'/'+file_name,'wb') as f:
        f.write(request.content)



t=StaticPicture()
t.num1=272833
sum_list5=[]
f = open("foo_sum_6.txt") # 返回一个文件对象
fo=open('foo_sum_6_download.txt', "a")
line = f.readline() # 调用文件的 readline()方法
while line:
  fo.write(line)#写入其他文件
  line=line.replace('\n', '')#替换掉换行符
  #通过URL获取到HTML内容
  request=requests.get(line, timeout=10)
  request.encoding = request.apparent_encoding
  #下载图片
  dir_name=t.dir_name(line,request,"",'<h1>(.*?)</h1>','D:\\mn\\')
  t.num2=t.num2+1
  print("下载总进度"+str(t.num2)+'/'+str(t.num1))
  t.downLoad(line,request,dir_name,'<img src="(.*?)" alt=".*?"( class=".*?"| /)>')
  #继续读取下一行
  line = f.readline()
fo.close()
f.close()



