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
    print(re.sub('([\\/:"*?<>|\x00-\x1F]+)','',re.findall(ze1,html)[-1]))
    list2=re.findall('http://www\.cgtpw\.com/(.*?)/.*?\.html',url)[-1]
    if len(url) ==0:
      return lujing+dir_name
    else:
      try:
        return lujing+list2+'\\'+re.sub('([\\/:"*?<>|\x00-\x1F]+)','',re.findall(ze1,html)[-1])#解决文件夹名称出现异常字符问题
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
    for url1 in urls:
      file_name=url1.split('/')[-1]
      try:
        file_name=re.findall('(.*?\.jpg)',file_name)[-1]
      except:
        return ""
      str2=dir_name+'/'+file_name
      if  os.path.exists(str2):
        return ""
      else:
        try:
          request1= requests.get(url1)
        except:
          return ''
        with open(dir_name+'/'+file_name,'wb') as f:
          f.write(request1.content)
          print(url1)
          print(dir_name)



t=StaticPicture()
sum_list5=[]
f = open("foo_sum_9.txt") # 返回一个文件对象
fo=open('foo_sum_9_download.txt', "a")
fo1=open('foo_sum_9_blank.txt','a')
line = f.readline() # 调用文件的 readline()方法
while line:
  fo.write(line)#写入其他文件
  line=line.replace('\n', '')#替换掉换行符
  #通过URL获取到HTML内容
  request=requests.get(line,headers=headers)
  request.encoding = request.apparent_encoding
  #下载图片
  dir_name=t.dir_name(line,request,"",'<h1>(.*?)</h1>','D:\\mn\\')
  print("匹配到的问价夹路径"+dir_name)
  t.num2=t.num2+1
  print("下载总进度"+str(t.num2))
  t.downLoad(line,request,dir_name,'<img src="(.*?)" alt=".*?"( class=".*?"| /)>')
  if os.path.getsize(dir_name)==0:#特殊情况文件路径中有：，普通替换无法实现
    fo1.write(line+'\n')
  #继续读取下一行
  line = f.readline()
fo1.close()
fo.close()
f.close()



