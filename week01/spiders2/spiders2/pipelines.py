# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# from pandas as pd

class Spiders2Pipeline:
    def process_item(self, item, spider):
        name = item["name"]
        style = item["style"]
        date = item["date"]
        output = f'|{name}|\t|{style}|\t|{date}|\n\n'
        # print(output)
        # moveFile = pd.DataFrame(data=output)
        # moveFile.to_csv('./maoyaoscrapy.csv',mode='a', encoding='UTF8', index=False, header=False)
        with open('./movie.csv','a+',encoding='utf-8') as article:
            article.write(output)
        return item
