#_*_encoding:utf-8 _*_
"""
@Software: PyCharm
@Python: 3.X   X==5
@Time: 2017.9.15
@Contact:520@skyne.cn
@Author: SKYNE
"""
"""导入所需的第三库"""
import  requests
from lxml import html
def Get_BookName():     ### 获取书名所在的网页，解析并匹配其中的书名，返回书名list###
    All_Name = []
    with open('Book_Name.txt', 'r+', encoding='utf-8') as f:    ### 打开书名文件，取出书名，并遍历书名，存至list中 ###
        lines = f.readlines()
        for line in lines:
            All_Name.append(line)
    return All_Name
def Get_BookImage(Booklist):
    Basic_url = "https://baike.baidu.com/item/"                ### 百度百科的首页 ###
    for Book_Name in Booklist:
        url = Basic_url + Book_Name[1:-2:1]                    ###  构造搜索的URL  ###
        print(url)
        response = requests.get(url= url, verify= False).text
        selector = html.fromstring(response)
        Image_Url = selector.xpath("/html/body//div[@class='summary-pic']/a/img/@src")   ### 定位图片所在的位置，并取出来 ###
        print(Image_Url)
        try:
            with open('Book_Image.txt', 'a+', encoding='utf-8') as f:      ### 以markdown的用法，获得永久的图片链接。 ###
                line = "![" + Book_Name[ 1:-2:1 ] + "](" + Image_Url[ 0 ] + ")"
                f.writelines(line)
                f.writelines('\n\n')
        except IndexError as e:                                          ### 数组越界，匹配不到时，略过。 ###
            pass
if  __name__  == '__main__':
    i = Get_BookName()
    Get_BookImage(i)
