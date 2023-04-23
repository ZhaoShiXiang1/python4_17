

for i in range(1,11):
    num=0
    f = open("foo_sum.txt") # 返回一个文件对象
    str1='foo_sum_'+str(i)+'.txt'
    fo=open(str1, "a")
    line = f.readline() # 调用文件的 readline()方法
    while line:
        num=num+1
        if (i-1)*30000<num and num<i*30000:
            fo.write(line)#写入其他文件
        line = f.readline()
    fo.close()
    f.close()



# f = open("foo_sum.txt") # 返回一个文件对象
# fo=open('foo_sum_download.txt', "a")
# line = f.readline() # 调用文件的 readline()方法
# while line:
#     fo.write(line)#写入其他文件
#     line=line.replace('\n', '')#替换掉换行符
#     #通过URL获取到HTML内容
#     request=requests.get(line)
#     request.encoding = request.apparent_encoding
#     #下载图片
#     dir_name=t.dir_name(line,request,"",'<h1>(.*?)</h1>','D:\\mn\\')
#     t.num2=t.num2+1
#     print("下载总进度"+str(t.num2)+'/'+str(t.num1))
#     t.downLoad(line,request,dir_name,'<img src="(.*?)" alt=".*?"( class=".*?"| /)>')
#     #继续读取下一行
#     line = f.readline()
# fo.close()
# f.close()