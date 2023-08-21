# -*- codeing = utf-8 -*-
from bs4 import BeautifulSoup  # 网页解析，获取数据
import re  # 正则表达式，进行文字匹配`
import xlwt  # 进行excel操作
import xlrd
import requests


def main():
  wb = xlrd.open_workbook(filename="D:/Users/PC/Desktop/huanbao.xls", formatting_info=True)
  CLsheet = wb.sheet_by_name("CL")

  savepath = "D:/Users/PC/Desktop/huanbaores.xls"  # 当前目录新建XLS，存储进去

  book = xlwt.Workbook(encoding="utf-8", style_compression=0)  # 创建workbook对象
  sheet = book.add_sheet('AQCdocu', cell_overwrite_ok=True)  # 创建工作表
  col = ("名称", "法人", "注册资本", "成立日期", "地址", "经营范围")
  for i in range(0, 6):
    sheet.write(0, i, col[i])  # 列名
  book.save(savepath)  # 保存
  count = 0
  for num in range(0, 600):


    Name = CLsheet.cell(num, 0).value
    print(Name)
    url = "https://aiqicha.baidu.com/s?q="+str(Name)+"&t=0"
    html = askURL(url)
    # print("--------------------------")
    # print(html)
    # print("-----------------------")
    TotalStr = str(re.findall(r'resultList(.*?)regNo', html, re.S))
    # print("--------------------------")
    # # print(html)
    # print("-----------------------")
    # print(TotalStr)
    # print("-----------------------")
    Name = re.findall(r'"titleName":"(.*?)"', TotalStr, re.S)
    print(Name)
    # 如果找不到，则continue
    if Name == []:
      continue
    # 只取Name[0]，其他同理
    sheet.write(count, 0, Name[0])
    book.save(savepath)

    LegalPerson = re.findall(r'"titleLegal":"(.*?)"', TotalStr, re.S)  # 通过正则表达式查找
    print(LegalPerson)
    sheet.write(count, 1, LegalPerson[0])
    book.save(savepath)

    RegisteredCapital = re.findall(r'"regCap":"(.*?)"', TotalStr, re.S)
    print(RegisteredCapital)
    sheet.write(count, 2, RegisteredCapital[0])
    book.save(savepath)

    EstablishDate = re.findall(r'validityFrom":"(.*?)"', TotalStr, re.S)
    print(EstablishDate)
    sheet.write(count, 3, EstablishDate[0])
    book.save(savepath)


    Location = re.findall(r'"titleDomicile":"(.*?)"', TotalStr, re.S)
    print(Location)
    sheet.write(count, 4, Location[0])
    book.save(savepath)


    BusinessScope = re.findall(r'"regNo":"(.*?)"', html, re.S)

    if len(BusinessScope) == 0:
      BusinessScope.append(1)
      sheet.write(count, 5, BusinessScope[0])
      book.save(savepath)
    else:
      sheet.write(count, 5, BusinessScope[0])
      book.save(savepath)


    count = count + 1


# 得到指定一个URL的网页内容
def askURL(url):

  headers = {
    'Accept': 'application / json, text / plain, * / *',
    'Accept - Encoding': 'gzip, deflate, br',
    'Accept - Language': 'en - US, en;q = 0.9',
    'Connection': 'keep - alive',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'cookie': 'BIDUPSID=5B3BA4EA7E7F9229998A6FC371853E39; PSTM=1692090074; BAIDUID=5B3BA4EA7E7F922902428BCA19187D43:FG=1; log_guid=9b7a5dc64252634b3d585e73fcb3e3fa; _j47_ka8_=57; BDUSS=ktwNEtrNkZpd1hOUnBoSDdVYzVTd2s3S3VPZTRrQmZ3T0tBMndiSWJnb1hjZ1psRVFBQUFBJCQAAAAAAAAAAAEAAADELAGPd3dzc2FkYWQyNDY4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABfl3mQX5d5kQ; BDUSS_BFESS=ktwNEtrNkZpd1hOUnBoSDdVYzVTd2s3S3VPZTRrQmZ3T0tBMndiSWJnb1hjZ1psRVFBQUFBJCQAAAAAAAAAAAEAAADELAGPd3dzc2FkYWQyNDY4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABfl3mQX5d5kQ; BDPPN=f754612400026197bbdd13d70d1cd20d; login_type=passport; _t4z_qc8_=xlTM-TogKuTwh5-gwgTjk84AA707sBGehQmd; Hm_lvt_ad52b306e1ae4557f5d3534cce8f8bbf=1692329123,1692581307; H_PS_PSSID=26350; BA_HECTOR=a5852gak80ak8h0ga48k21al1ie5ib01p; BAIDUID_BFESS=5B3BA4EA7E7F922902428BCA19187D43:FG=1; ZFY=iRjFTsgqGUWr590q37OROwrLkSqJSu:BTDq:B8jnmusIM:C; BDRCVFR[tkCtGyA-aFD]=mk3SLVN4HKm; delPer=0; PSINO=2; _fb537_=xlTM-TogKuTwrDl8yqK3hpxzRMMRI2ONYKC5G38y8nJldJHMNWigU4gmd; log_first_time=1692587564360; ab169258680=78aba9cd3257846fa38c22365ce5e3551692588140102; Hm_lpvt_ad52b306e1ae4557f5d3534cce8f8bbf=1692588141; log_last_time=1692588141126; _s53_d91_=7491325a0df0365e5851c54f1182e4e6044a384efbe5f2b5e6c4c0726350cc0164e5140c5c187775077410bdff4ab4a59f7f2c3cc3b8be6a7ab1cc62f2f8c7e122cf7eb9fb27b5b9938f77c273ef73f6732e3508fda46e1a57bb08fad9261d646c53b80970e94594a48abdd0200fdc8ab523608a5b63df78a7c1716ab53e9eb20dcd60cb417c75c8478f01e4d7b5e3a75351c80eb82897d7a681167501f0261583680bc116a171e5e87d6117d5898b796cc05546668d595ad3c1138396a4e89174e45d0c8c753bb400327e69746ef53bdd1c2730bbe4a6a80e96a6a959456da5; _y18_s21_=a89965fa; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; ab_sr=1.0.1_OWU4MjVjM2VkM2VmYzE4MTViNzIzOGJhZTU1N2I0YzA5ZGI1NmE0MWI3NWMzZTU2M2JiZDkyNzY5MmI0ZjcwZjIxYWQ3ZThiYTdjZWNkMTU0YjRkZTFkOWE5MTg3MzBlMTUzNDY0ZTE3MWYzNjQxNWY0Y2VhM2JlZjBkZDA2YjcxMjhiNTJlNTM2YTE1ODIxYjY4OTcyYmMwYWZhZmNiZg==; RT="z=1&dm=baidu.com&si=4c2835c8-8b51-465d-a828-8a31c36cd704&ss=llk77grr&sl=f&tt=iot&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=2380c&nu=vgd4itr&cl=238al&ul=56u5n"',
    'Host': 'aiqicha.baidu.com',
    'Referer': 'https: // aiqicha.baidu.com / s?q = % E5 % 88 % B6 % E9 % 80 % A0 & t = 0',
    'sec - ch - ua': '";Not A Brand";v = "99", "Chromium";v = "94"',
    'sec - ch - ua - platform': '"Windows"',
    'Sec - Fetch - Dest': 'empty',
    'Sec - Fetch - Mode': 'cors',
    'Sec - Fetch - Site': 'same - origin',
  }

  response = requests.get(url, headers=headers)
  print(response.status_code)
  response.encoding = response.apparent_encoding
  html = response.text
  return html.encode("utf-8").decode("unicode_escape")

if __name__ == "__main__":  # 当程序执行时
  main()
  print("爬取完毕！")
