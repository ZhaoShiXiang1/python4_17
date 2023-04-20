import re
import requests



# request=requests.get('http://www.cgtpw.com/jpmn/')
# # 防止网页中文乱码
# request.encoding = request.apparent_encoding
# html=request.text
# print(html)
#获取其他页面
# num=str(re.findall('http://www.cgtpw.com/(.*?)/','http://www.cgtpw.com/jpmn/')[-1])
# print(num)

zeconcat='http://www\.'+str(re.findall('http://www.cgtpw.com/(.*?)/','http://www.cgtpw.com/jpmn/')[-1])+'\.com/(.*?)/.*?\.html'
print(zeconcat)