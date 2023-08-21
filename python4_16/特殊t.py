
import re
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def gpt3_5(session):
    num20=1
    driver = webdriver.Chrome()
    # 打开网页
    driver.get('https://chat.wuguokai.cn/#/chat/')

    # 定位文本框
    try:
      input_element = driver.find_element_by_class_name('n-input__textarea-el')
    except:
      driver.quit()
      gpt3_5(session)
    # if len(input_element)==0:
    #     driver.quit()
    #     return '网络波动请重试'
    # print(input_element)
    # str1:str=sys.argv[1]
    # 输入关键字
    input_element.send_keys(session)
    input_element.send_keys(Keys.ENTER)

#提高响应效率
    time.sleep(3)
    html = driver.page_source
    str2= re.findall('</blockquote>[\s\S]+',html)[-1]
    str3=re.findall('</blockquote>\n([\s\S]+)</div></div></div></div><div class="flex flex-col">',str2)[-1]
    # str4=str3
    str4=str3.replace('<p>','').replace('</p>','\n')
    if len(str4) == 17:
        driver.quit()
        num20+=1
        if num20==15:
            return '响应超时，请稍后再试吧'
        print('---------------')
        gpt3_5(session)








    time.sleep(10)
    wait = WebDriverWait(driver,10000)
    # wait.until(EC.presence_of_element_located((By.ID,'content_left')))
    # print(driver.current_url)
    # print(driver.get_cookies())
    # print(driver.page_source)
    # 获取网页源代码
    html = driver.page_source
    # print(html)
    # print("------------------------------")
    str2= re.findall('</blockquote>[\s\S]+',html)[-1]
    str3=re.findall('</blockquote>\n([\s\S]+)</div></div></div></div><div class="flex flex-col">',str2)[-1]
    # str4=str3
    str4=str3.replace('<p>','').replace('</p>','\n')
    # lens=len(str3)
    # str4='您好:'
    # for tmp in str3:
    #     str4+='\n'+tmp
    driver.quit()
    print(str4)
    # if len(str4) == 17:
    #     print('---------------')
    #     gpt3_5(session)

    return str4
    # 关闭浏览器
if __name__ == '__main__':
    # session:str = sys.argv[1]
    session:str = "写一首古诗"
    gpt3_5(session)







