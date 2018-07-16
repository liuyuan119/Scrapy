# -*- coding: utf-8 -*-
import scrapy


class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'
    allowed_domains = ['www.qiushibaike.com']
    start_urls = ['http://www.qiushibaike.com/']

    def parse(self, response):
        div_list = response.xpath("//div[starts-with(@id, 'qiushi_tag_')]")
        items = []
        for div in div_list:
            # 在scrapy中于要求把用extract()函数,对xpath进行转化为unicode字符串然后在进行操作(数据提取)
            img_url = div.xpath("./div[@class='author clearfix']//img//@src").extract()[0]
            name = div.xpath("./div[@class='author clearfix']//img//@alt").extract_first()
            age = div.xpath("./div[@class='author clearfix']//div//text()").extract_first()
            content = div.xpath("./a/div[@class='content']//span//text()").extract_first()
            item = {
                "img_url": img_url,
                "name": name,
                "age": age,
                "content": content
            }
            items.append(item)
        return items
