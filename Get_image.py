#_*_encoding:utf-8 _*_
"""
@Software: PyCharm
@Python: 3.X   X==5
@Time: 2017.9.15
@Contact:520@skyne.cn
@Author: SKYNE
"""
"""导入所需的第三库"""
import re, requests
from lxml import html
def Get_BookName():     ### 获取书名所在的网页，解析并匹配其中的书名，返回书名list###
    url = "http://www.jingyu.in/index.php/archives/327/"
    response = requests.get(url)
    Str = response.text.encode('utf-8')
    pattern = re.compile(r"《[\u4e00-\u9fa5]*》")   ### 匹配位于《》中的中文，也就是书名 ###
    results = pattern.findall(Str.decode('utf-8'))
    return set(results)                           ### set方法除去重复的书名 ###

def Get_BookImage(Booklist):
    Basic_url = "https://baike.baidu.com/item/"      ###  百度百科的url，后面加书名，直接用Get方式请求即可  ###
    Book_Dict = {}                                   ### 以字典方式存储书名及其书的的图片 ###
    for Book_Name in Booklist:
        url = Basic_url + Book_Name[1:-1:1]            ### 切片操作，取出书名前后的《》 ###
        print(url)
        response = requests.get(url= url, verify= False).text       ### verify= False 关闭ssl验证 ###
        selector = html.fromstring(response)
        Image_Url = selector.xpath("/html/body//div[@class='summary-pic']/a/img/@src")      ### 解析图片所在的URL ###
        Book_Dict[Book_Name] = Image_Url
    print(Book_Dict)


if  __name__  == '__main__':
    i = Get_BookName()
    Get_BookImage(i)