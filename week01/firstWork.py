import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
import lxml.etree
from time import sleep


# 评分 //*[@id="interest_sectl"]/div[1]/div[2]/strong
# 上映日期//*[@id="info"]/span[10]
# 电影名称//*[@id="content"]/h1/span[1]
# soup = bs(response.text,'html.parser')

maoyan_base_url = 'https://maoyan.com'
mouyanURL = f'{maoyan_base_url}/films?showType=3'
uesr_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
ie_user_agent = 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729)'


def savaFile(content):
    moveFile = pd.DataFrame(data=content)
    moveFile.to_csv('./maoyao.csv',mode='a', encoding='UTF8', index=False, header=False)


def getMovieDeatil(url):
    detalResponse = requests.get(url,headers={'user-agent':uesr_agent})
    if(detalResponse.status_code == 200):
        detail_soup = bs(detalResponse.text,'html.parser')
        name = detail_soup.find("h1",attrs={"class":'name'}).text
        style_element = detail_soup.find_all("li",attrs={"class":'ellipsis'})
        style = ''
        data = ''
        for key,value in enumerate(style_element):
            if(key == 0):
                a_list = value.find_all('a')
                for tag in a_list:
                    style = style + ',' + tag.text
            elif key == 2:
                data = value.text
        print(name)
        savaFile([name,style,data])

def getMaoyanInfo():
    response = requests.get(mouyanURL,headers={'user-agent':ie_user_agent})
    if(response.status_code == 200):
        soup = bs(response.text,'html.parser')
        soup_conetnt = soup.find_all("div",attrs={"class":'movie-item film-channel'})
        soup_conetnt_top_10 = soup_conetnt[0:10]
        for i in soup_conetnt_top_10:
            getMovieDeatil(maoyan_base_url + i.find('a').get('href'));
            sleep(2)


getMaoyanInfo()

            

# for i in soup.find_all("div",attrs={"class":'hd'}):
#     for aTag in i.find_all("a"):
#         print(aTag.get('href'))
#         print(aTag.find('span',).text)

# selector = lxml.etree.HTML(response.text)
# name = selector.xpath('//*[@id="content"]/h1/span[1]/text()')
# print(name)
# date = selector.xpath('//*[@id="info"]/span[10]/text()')
# print(date)
# sort = selector.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()')
# print(sort)

# def get_url_content(url):
#     user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"
#     response = requests.get(url, headers={'user-agent': user_agent})
#     soup = bs(response.text,'html.parser')
#     for i in soup.find_all("div",attrs={"class":'hd'}):
#         for aTag in i.find_all("a"):
#             print(aTag.get('href'))
#             print(aTag.find('span',).text)

#moveurl = 'https://www.douban.com/movie/top250'
# move1url = 'https://movie.douban.com/subject/1292052/'


# urls = tuple(f'https://movie.douban.com/top250?start={pages * 25}&filter=' for pages in range(0,10))

# from time import sleep
# for url in urls:
#     get_url_content(url)
#     sleep(1)


# move_list = [name, date, sort]




# print(response.text);
