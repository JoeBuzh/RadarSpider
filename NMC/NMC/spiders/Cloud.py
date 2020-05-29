# -*- coding: utf-8 -*-
import scrapy

import os
import re
from datetime import datetime, timedelta

from NMC.items import CloudItem


class CloudSpider(scrapy.Spider):
    name = 'Cloud'
    allowed_domains = ['http://www.nmc.cn/publish/satellite']
    start_urls = ['http://www.nmc.cn/publish/satellite/FY4A-true-color.htm']

    def parse(self, response):
        # img_urls = response.css('.img img::attr(data-original)').extract()  # old version       
        img_urls = response.css('.col-xs-2 div::attr(data-img)').extract()    # new version
        print('-'*100)
        print('\n'.join(img_urls))
        print('-'*100)

        for url in img_urls:
            item = CloudItem()
            item['url_raw'] = url
            url_new, url_utc, url_bjt = self.parse_img(url)
            item['url_new'] = url_new
            item['url_utc'] = url_utc
            item['url_bjt'] = url_bjt
            item['url_type'] = 'China_FY4A'

            yield item

    def parse_img(self, img_url: str) -> tuple:
        url_new = img_url.replace("/medium/", "/")
        url_utc, url_bjt = self.parse_utc(img_url)

        return url_new, url_utc, url_bjt

    def parse_utc(self, url: str) -> tuple:
        utc_str = re.findall(r'\d+.JPG', url)[0][:12]
        utc = datetime.strptime(utc_str, "%Y%m%d%H%M")
        bjt = utc + timedelta(hours=8)
        url_utc = utc.strftime("%Y%m%d %H:%M")
        url_bjt = bjt.strftime("%Y%m%d %H:%M")

        return url_utc, url_bjt

    def parse_time(self, time: str, formats: str) -> datetime:
        return datetime.strptime(time, formats)
