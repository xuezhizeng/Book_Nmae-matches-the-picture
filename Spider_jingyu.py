#_*_encoding:utf-8 _*_
"""
@Software: PyCharm
@Python: 3.X   X==6
@Time: 2017.9.15
@Contact:520@skyne.cn
@Author: SKYNE
"""
"""导入所需的第三库"""
import requests, re

### 只是简单地构造URL循环，不断的匹配页面中的书名 ###

def Get_Name():
    All_Name = [ ]
    Jing_Url = "http://jingyu.in/index.php/archives/"
    for i in range(350):
        All_Url = Jing_Url + str(i)
        response = requests.get(url=All_Url)
        if response.status_code == 200:
            response = re.sub('[:·，]', '', response.text)     ### 此前发现个问题，书名中包含:·，时，无法匹配。故先删除掉这些字符 ###
            pattern = re.compile(r"《[\u4e00-\u9fa5]*》")      ### 匹配位于《》中的中文，也就是书名 ###
            results = pattern.findall(response)
            print(results)
            All_Name = All_Name + list(set(results))         ### 去重，以及添加到list中 ###
    return All_Name

def Write_Name(Name_List):
    with open('Book_Name.txt','a', encoding='utf-8') as f:   #### 此处需要指定文件编码格式，不然会乱码 ###
        for i in Name_List:
            f.writelines(i + '\n')

if  __name__  == '__main__':
    Name_List = Get_Name()
    Write_Name(Name_List= Name_List)