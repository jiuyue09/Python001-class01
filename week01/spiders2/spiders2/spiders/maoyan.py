# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from time import sleep
from spiders2.items import Spiders2Item

class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['www.maoyan.com']
    base_url = 'http://www.maoyan.com'
    start_urls = [f'{base_url}/']

    def start_requests(self):
        url = f'{self.start_urls[0]}films?showType=3'
        yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        # print(str(response) + "影影之movie-item film-channel")
        movies = Selector(response=response).xpath('//div[@class="movie-item film-channel"]')
        # print(movies)
        for movie in movies[0:10]:
            link = movie.xpath("./a/@href")
            # print(link)
            detail_url = f'{self.base_url}{link.extract()[0]}'
            # print(detail_url)
            sleep(1)
            yield scrapy.Request(detail_url,callback=self.parse2)

        # soup = bs(response.text,'html.parser')
        # soup_conetnt = soup.find_all("div",attrs={"class":'movie-item film-channel'})
        # soup_conetnt_top_10 = soup_conetnt[0:10]
        # for i in soup_conetnt_top_10:
        #     getMovieDeatil(maoyan_base_url + i.find('a').get('href'));
        #     sleep(2)
        # pass

    def parse2(self, response):
        details = Selector(response=response).xpath('//div[@class="movie-brief-container"]')
        items = []
        for detail in details:
            name = detail.xpath('./h1/text()').extract_first().strip()
            li_elements = detail.xpath('./ul/li')
            # print(name_path,li_elements)
            style = []
            date = detail.xpath('./ul/li[2]/text()').extract_first().strip()
            for key,value in enumerate(li_elements):
                # print(value,value.extract())
                if(key == 0):
                    for style_element in value.xpath('./a/text()'):
                        # style = style_element.xpath('./a/text()')
                        style.append(style_element.extract().strip())
                        # print(style_element)
                # elif key == 2:
                #     date = value.extract()
            # print(name,style,date)
            item = Spiders2Item()
            item['name'] = name
            item['style'] = ",".join(style)
            item['date'] = date
            items.append(item)
            yield item
            
                   
