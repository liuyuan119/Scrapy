# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class Learning2Pipeline(object):
    # 重写初始化函数
    def __init__(self):
        # 此函数只会执行一次
        self.fw = open('qiubai1.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        # 将Item对象转为字典
        obj = dict(item)
        # 将python对象转为字符串
        str = json.dumps(obj, ensure_ascii=False)
        self.fw.write(str + '\n')
        return item

    # 关闭spider的时候,关闭资源文件
    def close_spider(self, spider):
        self.fw.close()
