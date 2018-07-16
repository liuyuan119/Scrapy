# -*- coding: utf-8 -*-
import scrapy


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        # print(response)
        # print(type(response))
        # print(response.url)
        # print(response.headers)
        # print(response.text)  # 返回文本类型的数据
        # print(response.body)  # 返回二进制b类型的数据
        yield response
