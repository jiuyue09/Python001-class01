# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# from pandas as pd

import pymysql

class Spiders2Pipeline:
    def process_item(self, item, spider):
        # name = item["name"]
        # style = item["style"]
        # date = item["date"]
        # output = f'|{name}|\t|{style}|\t|{date}|\n\n'
        # print(output)
        # moveFile = pd.DataFrame(data=output)
        # moveFile.to_csv('./maoyaoscrapy.csv',mode='a', encoding='UTF8', index=False, header=False)
        # with open('./movie.csv','a+',encoding='utf-8') as article:
        #     article.write(output)

        self.saveWithMysql(item)
        return item


    
    def saveWithMysql(self,item):
        print('开始')
        conn = pymysql.connect(
            host = 'localhost',
            port = 3306,
            user = 'root',
            password = '123456',
            db = 'python_data'
        )
        name = item["name"]
        style = item["style"]
        date = item["date"]
        mysqls = f'INSERT INTO movies(title,time,style) VALUES("{name}","{date}","{style}")'
        print(mysqls)
        try:
            cur = conn.cursor()
            print('链接',cur)
            cur.execute(mysqls)
            cur.close()

            conn.commit()
        except:
            conn.rollback()
        conn.close()


