# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import sys
import configparser
from datetime import datetime
from datetime import timedelta

from urllib.request import urlopen
from urllib.request import urlretrieve

import scrapy
from scrapy.exceptions import DropItem


class NmcPipeline(object):
    def process_item(self, item, spider):
        if item.get('savepath'):
            urlretrieve(item.get('url_new'), item.get('savepath'))
            print('Save {} file to: {}'.format(item.get('url_type'), item.get('savepath')))
        else:
            raise DropItem("No savepath %s" % item)

        return item


class ExistPipeline(object):
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('/data/buzehao/NMC/scrapy.cfg')
        self.savabase = config.get('savedir', 'SAVEDIR')

    def process_item(self, item, spider):
        bjt = datetime.strptime(item.get('url_bjt'), "%Y%m%d %H:%M")
        # save
        dest = self.checkdir(os.path.join(self.savabase, item.get('url_type')))
        filedir = self.checkdir(os.path.join(dest, bjt.strftime("%Y%m")))
        # test
        '''
        dest = os.path.join(self.savabase, item.get('url_type'))
        filedir = os.path.join(dest, bjt.strftime("%Y%m"))
        '''
        filesname = os.path.join(filedir, bjt.strftime('%Y%m%d%H%M')+'.png')

        if os.path.exists(filesname):
            raise DropItem("Already exists %s" % item)
        else:
            item['savepath'] = filesname
            return item

    def checkdir(self, pathname):
        if not os.path.exists(pathname):
            os.makedirs(pathname)
        assert os.path.exists(pathname)

        return pathname
