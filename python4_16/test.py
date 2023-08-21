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
    print("--------------------------")
    print(html)
    print("-----------------------")
    TotalStr = str(re.findall(r'resultList(.*?)regNo', html, re.S))
    print(TotalStr)

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


    BusinessScope = re.findall(r'"scope":"(.*?)"', TotalStr, re.S)

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
    'cookie': 'BIDUPSID=381DD96C2966B9CC44CC57CADD3B67D1; PSTM=1632724182; BAIDUID=381DD96C2966B9CCD0AB4379252D8022:FG=1; __yjs_duid=1_cf0d57675356f745bcbb2c45c59881491632793531463; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDSFRCVID=bKDOJexroG382q3HDDZtwituB2KKg7jTDYrEZguiLEnlccDVJeC6EG0PtOqPGZu-EHtdogKK0mOTH6KF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tJuf_DthfIt3fP36q45HMt00qxby26ndfg79aJ5nQI5nh-QP55J1hUPNhlJ0-nQG0jTlVpvKQUbmjRO206oay6O3LlO83h5MQGnMKl0MLPb5sbRPLjOD0tA4LxnMBMPjamOnaIQc3fAKftnOM46JehL3346-35543bRTLnLy5KJYMDFlejA2j65bDaRf-b-X-C72sJOOaCvW8pROy4oWK441DhjyqRj7aKTnKP3VbP5IhlvobTJ83M04K4oAaT38JGOM_Jb8WMQJoMQ2Qft20b3bb-RT0qOa3g5wWn7jWhk2Dq72y5jvQlRX5q79atTMfNTJ-qcH0KQpsIJM5-DWbT8IjHCDq6kjJJFOoIvt-5rDHJTg5DTjhPrMj4OWWMT-MTryKKJKaKTKOb7NX-QbMJ00LG5iB--f2HnRh4oNB-3iV-OxDUvnyxAZbn7pLUQxtNRJVnbcLpQmHlbVX4vobUPUDMc9LUkqW2cdot5yBbc8eIna5hjkbfJBQttjQn3hfIkj2CKLtCIWhKLCe503-RJH-xQ0KnLXKKOLVb5HWh7ketn4hUt254R-K47RXP5gbK5JLl_-WhvJMnc2QhrKQf4WWb3ebTJr32Qr-J39QfbpsIJM557fyp8z0M5RBx6QaKviaKJEBMb1MlvDBT5h2M4qMxtOLR3pWDTm_q5TtUJMeCnTDMFhe6oM-frDa4J3K4oa3RTeb6rjDnCr-xRUXUI82h5y05tOtjCeapbgytbbjtbGL65vyPbWMRORXRj4yDvtBlRNaJRjHpbKy4oTjxL1Db3JWboT3aQtsl5dbnboepvoD-cc3MvByPjdJJQOBKQB0KnGbUQkeq8CQft20b0EeMtjW6LEK5r2SC_KtCP53f; BDPPN=04a584e8a43b3c2543211c1ff0083491; log_guid=5c0734af5e94123684a6f61121e70a8f; _j47_ka8_=57; Hm_lvt_ad52b306e1ae4557f5d3534cce8f8bbf=1633747411,1633747424,1633747468; ZX_UNIQ_UID=ad0ed23cec5aa23f175c6abb6a19be38; Hm_lpvt_ad52b306e1ae4557f5d3534cce8f8bbf=1633748170; _s53_d91_=76b33b1f7b50d853e35a0ac59d45020eb588e5b4d4bffd71ed55400a95b4096de8657d250af19df5057cfea80e21ae451091cbf031ecc598c2ee5f212c2788df46767c12e766e00ad42a19c9113ccc138394669b0c028d0947c24e73ff8e3be8a67a5d51fb926dc1ac67756522b47e8ef0baeb5127f5f910146e9d5c27b446f16b1c90dfe4ff71d10043c846a542d5aff4cade220accfe9201f7dce1fb216c5dae97bdf76ae98a71591e3a195e035334ce024ed6aae1cfed2773365c5272a6f41811e03945bab155c60a5a10fe2c4cdb; _y18_s21_=1a10c202; H_PS_PSSID=34652_34441_34068_31254_34711_34525_34584_34505_34706_34107_26350_34419_34691_34671; delPer=0; PSINO=2; BDSFRCVID_BFESS=bKDOJexroG382q3HDDZtwituB2KKg7jTDYrEZguiLEnlccDVJeC6EG0PtOqPGZu-EHtdogKK0mOTH6KF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF_BFESS=tJuf_DthfIt3fP36q45HMt00qxby26ndfg79aJ5nQI5nh-QP55J1hUPNhlJ0-nQG0jTlVpvKQUbmjRO206oay6O3LlO83h5MQGnMKl0MLPb5sbRPLjOD0tA4LxnMBMPjamOnaIQc3fAKftnOM46JehL3346-35543bRTLnLy5KJYMDFlejA2j65bDaRf-b-X-C72sJOOaCvW8pROy4oWK441DhjyqRj7aKTnKP3VbP5IhlvobTJ83M04K4oAaT38JGOM_Jb8WMQJoMQ2Qft20b3bb-RT0qOa3g5wWn7jWhk2Dq72y5jvQlRX5q79atTMfNTJ-qcH0KQpsIJM5-DWbT8IjHCDq6kjJJFOoIvt-5rDHJTg5DTjhPrMj4OWWMT-MTryKKJKaKTKOb7NX-QbMJ00LG5iB--f2HnRh4oNB-3iV-OxDUvnyxAZbn7pLUQxtNRJVnbcLpQmHlbVX4vobUPUDMc9LUkqW2cdot5yBbc8eIna5hjkbfJBQttjQn3hfIkj2CKLtCIWhKLCe503-RJH-xQ0KnLXKKOLVb5HWh7ketn4hUt254R-K47RXP5gbK5JLl_-WhvJMnc2QhrKQf4WWb3ebTJr32Qr-J39QfbpsIJM557fyp8z0M5RBx6QaKviaKJEBMb1MlvDBT5h2M4qMxtOLR3pWDTm_q5TtUJMeCnTDMFhe6oM-frDa4J3K4oa3RTeb6rjDnCr-xRUXUI82h5y05tOtjCeapbgytbbjtbGL65vyPbWMRORXRj4yDvtBlRNaJRjHpbKy4oTjxL1Db3JWboT3aQtsl5dbnboepvoD-cc3MvByPjdJJQOBKQB0KnGbUQkeq8CQft20b0EeMtjW6LEK5r2SC_KtCP53f; BAIDUID_BFESS=3D228C3FC1B3512BAD3529CB3B6ACE85:FG=1; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2217c6313f4bb433-0ec3e42acbdd15-b7a1a38-1024000-17c6313f4bccf9%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2217c6313f4bb433-0ec3e42acbdd15-b7a1a38-1024000-17c6313f4bccf9%22%7D; ab_sr=1.0.1_M2I1NDRhNTY5NGMwY2EzOTdkZDg5N2YzNTM0NjVlNzAwMmJjNzY1M2I3NmNiYjkxMjVjMTAwMjY5NTg0OTEyZTI3NWI4YTFkYWUyYzRlYjM0OTMxNDc3OGYwMDI5MTRmOWNkOTlhN2E0ZTg1MDMwNTk4NmViYjkxZWZjZmVmMmY2NjQ1N2MwNmNmOGRkMGExNjY1MGNhNjU5OTFmMmNmNg==; RT="z=1&dm=baidu.com&si=3h8cfcpdixy&ss=kuj7h7p1&sl=0&tt=0&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=15q82&ul=113ud&hd=113y9&cl=47l83',
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
