# 爬虫测试
# 导入包
import requests
import requests
import re
import os
headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.48'
}
#打开网址文件
f = open("D:\\Users\PC\Desktop\huanbao.txt") # 返回一个文件对象
fo=open('D:\\Users\PC\Desktop\huanbao_tmp.txt', "a")#打开一个环保储存文件，保存写入后的数据
fo1=open('D:\\Users\PC\Desktop\huanbao_res.txt', "a")#打开一个环保储存文件，保存写入后的数据
line = f.readline() # 调用文件的 readline()方法
while line:
    fo.write(line)#写入其他文件
    line=line.replace('\n', '')#替换掉换行符
    #通过URL获取到HTML内容
    request=requests.get(line,headers=headers)
    request.encoding = request.apparent_encoding
    #下载图片
    dir_name=t.dir_name(line,request,"",'<h1>(.*?)</h1>','D:\\mn\\')
    t.num2=t.num2+1
    print("下载总进度"+str(t.num2))
    t.downLoad(line,request,dir_name,'<img src="(.*?)" alt=".*?"( class=".*?"| /)>')
    if os.path.getsize(dir_name)==0:
        fo1.write(line+'\n')
    #继续读取下一行
    line = f.readline()