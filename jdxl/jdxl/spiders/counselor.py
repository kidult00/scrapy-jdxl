# -*- coding: utf-8 -*-
import scrapy
from jdxl.items import JdxlItem


class JdxlSpider(scrapy.Spider):
    name = "counselor"
    allowed_domains = ["jiandanxinli.com"]
    start_urls = ['http://jiandanxinli.com/experts']
    start_url_list = []

    for i in range(1,50):
        start_url_list.extend(['http://jiandanxinli.com/experts?&page=' + str(i)])
        # https://www.jiandanxinli.com/experts?&page=2

    start_urls = start_url_list

    def parse(self, response):

        for each in response.xpath('//a[@class="expert"]'):
            print(each)
            item=  JdxlItem()
            # 抓取姓名
            item['name'] = each.xpath('./div[@class="summary"]/strong/text()').extract()
            # 抓取 url
            item['url'] = each.xpath('./@href').extract()
            # 抓取简介
            item['info'] = each.xpath('./div[@class="summary"]//div[@class="content"]/text()').extract()
            # 抓取咨询方式、地点、价格等
            # 参考：[如何用scrapy提取不在标签内的文字？ - 知乎](https://www.zhihu.com/question/38080188)
            item['zx_type'] = each.xpath('./div[@class="info"]/i/following::text()').extract()[1]
            item['location'] = each.xpath('./div[@class="info"]/i/following::text()').extract()[2]
            item['price'] = each.xpath('./div[@class="info"]/i/following::text()').extract()[3]

            yield item
