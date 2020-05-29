# -*- coding: utf-8 -*-
import scrapy

import os
import re
from datetime import datetime
from datetime import timedelta

from NMC.items import RadarItem
from NMC.items import RadarHuabeiItem
from NMC.items import RadarHuananItem
from NMC.items import RadarHuazhongItem
from NMC.items import RadarHuadongItem
from NMC.items import RadarDongbeiItem
from NMC.items import RadarXibeiItem
from NMC.items import RadarXinanItem


class RadarSpider(scrapy.Spider):
    name = 'Radar'
    allowed_domains = ['http://www.nmc.cn/publish/radar']
    start_urls = ['http://www.nmc.cn/publish/radar/chinaall.html']

    def parse(self, response):
        img_urls = response.css('.col-xs-2 div::attr(data-img)').extract()
        print('-'*100)

        for url in img_urls:
            item = RadarItem()
            item['url_raw'] = url
            url_new, url_utc, url_bjt = self.parse_img(url)
            item['url_new'] = url_new
            item['url_utc'] = url_utc
            item['url_bjt'] = url_bjt
            item['url_type'] = 'China_Radar'

            yield item
        
    def parse_img(self, img_url: str) -> tuple:
        url_new = img_url.replace("/medium/", "/")
        url_utc, url_bjt = self.parse_utc(img_url)

        return url_new, url_utc, url_bjt

    def parse_utc(self, url: str) -> tuple:
        utc_str = re.findall(r'\d+.PNG', url)[0][:12]
        utc = datetime.strptime(utc_str, "%Y%m%d%H%M")
        bjt = utc + timedelta(hours=8)
        url_utc = utc.strftime("%Y%m%d %H:%M")
        url_bjt = bjt.strftime("%Y%m%d %H:%M")

        return url_utc, url_bjt

    def parse_time(self, time: str, formats: str) -> datetime:
        return datetime.strptime(time, formats)


class RadardongbeiSpider(RadarSpider):
    name = 'RadarDongbei'
    allowed_domains = ['http://www.nmc.cn/publish/radar']
    start_urls = ['http://www.nmc.cn/publish/radar/dongbei.html']

    def parse(self, response):
        urls = response.css('.col-xs-2 div::attr(data-img)').extract()
        print('-'*100)

        for url in urls:
            item = RadarDongbeiItem()
            item['url_raw'] = url
            item['url_new'] = url
            item['url_utc'] = self.parse_utc(url)[0]
            item['url_bjt'] = self.parse_utc(url)[1]
            item['url_type'] = 'Dongbei_Radar'

            yield item


class RadarhuabeiSpider(RadarSpider):
    name = 'RadarHuabei'
    allowed_domains = ['http://www.nmc.cn/publish/radar']
    start_urls = ['http://www.nmc.cn/publish/radar/huabei.html']

    def parse(self, response):
        urls = response.css('.col-xs-2 div::attr(data-img)').extract()
        print('-'*100)

        for url in urls:
            item = RadarHuabeiItem()
            item['url_raw'] = url
            item['url_new'] = url
            item['url_utc'] = self.parse_utc(url)[0]
            item['url_bjt'] = self.parse_utc(url)[1]
            item['url_type'] = 'Huabei_Radar'

            yield item


class RadarhuananSpider(RadarSpider):
    name = 'RadarHuanan'
    allowed_domains = ['http://www.nmc.cn/publish/radar']
    start_urls = ['http://www.nmc.cn/publish/radar/huanan.html']

    def parse(self, response):
        urls = response.css('.col-xs-2 div::attr(data-img)').extract()
        # times = response.css('.time::text').extract()
        print('-'*100)

        for url in urls:
            item = RadarHuananItem()
            item['url_raw'] = url
            item['url_new'] = url
            item['url_utc'] = self.parse_utc(url)[0]
            item['url_bjt'] = self.parse_utc(url)[1]
            item['url_type'] = 'Huanan_Radar'

            yield item


class RadarhuazhongSpider(RadarSpider):
    name = 'RadarHuazhong'
    allowed_domains = ['http://www.nmc.cn/publish/radar']
    start_urls = ['http://www.nmc.cn/publish/radar/huazhong.html']

    def parse(self, response):
        urls = response.css('.col-xs-2 div::attr(data-img)').extract()
        # times = response.css('.time::text').extract()
        print('-'*100)

        for url in urls:
            item = RadarHuazhongItem()
            item['url_raw'] = url
            item['url_new'] = url
            item['url_utc'] = self.parse_utc(url)[0]
            item['url_bjt'] = self.parse_utc(url)[1]
            item['url_type'] = 'Huazhong_Radar'

            yield item


class RadarhuadongSpider(RadarSpider):
    name = 'RadarHuadong'
    allowed_domains = ['http://www.nmc.cn/publish/radar']
    start_urls = ['http://www.nmc.cn/publish/radar/huadong.html']

    def parse(self, response):
        urls = response.css('.col-xs-2 div::attr(data-img)').extract()
        # times = response.css('.time::text').extract()
        print('-'*100)

        for url in urls:
            item = RadarHuadongItem()
            item['url_raw'] = url
            item['url_new'] = url
            item['url_utc'] = self.parse_utc(url)[0]
            item['url_bjt'] = self.parse_utc(url)[1]
            item['url_type'] = 'Huadong_Radar'

            yield item


class RadarxibeiSpider(RadarSpider):
    name = 'RadarXibei'
    allowed_domains = ['http://www.nmc.cn/publish/radar']
    start_urls = ['http://www.nmc.cn/publish/radar/xibei.html']

    def parse(self, response):
        urls = response.css('.col-xs-2 div::attr(data-img)').extract()
        # times = response.css('.time::text').extract()
        print('-'*100)

        for url in urls:
            item = RadarXibeiItem()
            item['url_raw'] = url
            item['url_new'] = url
            item['url_utc'] = self.parse_utc(url)[0]
            item['url_bjt'] = self.parse_utc(url)[1]
            item['url_type'] = 'Xibei_Radar'

            yield item


class RadarxinanSpider(RadarSpider):
    name = 'RadarXinan'
    allowed_domains = ['http://www.nmc.cn/publish/radar']
    start_urls = ['http://www.nmc.cn/publish/radar/xinan.html']

    def parse(self, response):
        urls = response.css('.col-xs-2 div::attr(data-img)').extract()
        # times = response.css('.time::text').extract()
        print('-'*100)

        for url in urls:
            item = RadarXinanItem()
            item['url_raw'] = url
            item['url_new'] = url
            item['url_utc'] = self.parse_utc(url)[0]
            item['url_bjt'] = self.parse_utc(url)[1]
            item['url_type'] = 'Xinan_Radar'

            yield item