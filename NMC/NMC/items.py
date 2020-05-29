# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NmcItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    '''
        定义爬取的几类图片共同属性
    '''
    url_raw = scrapy.Field()
    url_new = scrapy.Field()
    url_utc = scrapy.Field()
    url_bjt = scrapy.Field()
    url_type = scrapy.Field()
    savepath = scrapy.Field()


class MeteorItem(NmcItem):
    '''
        定义天气分析图爬虫数据项
    '''
    def __init__(self):
        super().__init__()


class CloudItem(NmcItem):
    '''
        定义卫星云图爬虫数据项
    '''
    def __init__(self):
        super().__init__()


class RadarItem(NmcItem):
    '''
        定义雷达拼图-全国爬取数据项
    '''
    def __init__(self):
        super().__init__()


class RadarDongbeiItem(RadarItem):
    '''
        定义雷达拼图-东北爬取数据项
    '''
    def __init__(self):
        super().__init__()


class RadarHuabeiItem(RadarItem):
    '''
        定义雷达拼图-华北爬取数据项
    '''
    def __init__(self):
        super().__init__()

    
class RadarHuananItem(RadarItem):
    '''
        定义雷达拼图-华南爬取数据项
    '''
    def __init__(self):
        super().__init__()


class RadarHuazhongItem(RadarItem):
    '''
        定义雷达拼图-华中爬取数据项
    '''
    def __init__(self):
        super().__init__()


class RadarHuadongItem(RadarItem):
    '''
        定义雷达拼图-华东爬取数据项
    '''
    def __init__(self):
        super().__init__()


class RadarXibeiItem(RadarItem):
    '''
        定义雷达拼图-西北爬取数据项
    '''
    def __init__(self):
        super().__init__()


class RadarXinanItem(RadarItem):
    '''
        定义雷达拼图-西南爬取数据项
    '''
    def __init__(self):
        super().__init__()