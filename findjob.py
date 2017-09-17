#python requests测试
from bs4 import BeautifulSoup
import requests
from urllib import request
import re 
import time
#打开文件

#伪装浏览器
headers = {'User-Agent' : r'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)' }
address='http://sou.zhaopin.com/jobs/searchresult.ashx?jl=653&kw=c%2b%2b&sm=0&sg=6729587202404b258ac42bedd469d049&p='
for y in range(15):
    address =  address+str(y)
    req=request.Request(address, headers=headers)
    page=request.urlopen(req).read()
    r=page.decode('utf-8')
    nresult=[]
    f = open('jobtable.txt', 'a+',encoding='utf-8')
#print(r.content)
#python 爬虫BeautifulSoup测试#根据类筛选公司，职位，月薪，地址
    soup = BeautifulSoup(r,"html.parser")
    result = soup.select('.gsmc')
    result2 =soup.select('.zwyx')
    result3 = soup.select('.gzdd')
    result4 = soup.select('.zwmc')
#正则表达式匹配，千万不能加括号，原因不明
    result = re.findall('[\u4e00-\u9fa5]+', str(result))
    result2 = re.findall('[\u4e00-\u9fa5]+|\d+-\d+', str(result2))
    result3 = re.findall('[\u4e00-\u9fa5]+', str(result3))
    result4 = re.findall('>.*[\u4e00-\u9fa5]+.*<', str(result4))
#滤除<>
    for i in result4:
        B=i.strip('<')
        nresult.append(B.strip('>'))#[\u4e00-\u9fa5]+[0-9a-zA-Z\_/()-]+[\u4e00-\u9fa5]+|[\u4e00-\u9fa5]+
    length= len(result4)
    for i in range(length):
        f.write(nresult[i]+"\n")  #职位
        time.sleep(0.01)          #
        f.write(result[i])        #公司
        time.sleep(0.01)
        f.write(result2[i])       #月薪  
        time.sleep(0.01)
        f.write(result3[i]+"\n")  #地址
        time.sleep(0.01)
#关闭文件
    f.close()
