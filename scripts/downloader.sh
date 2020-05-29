#!/bin/bash
# param: spider project, like: RadarHuabei

project=$1

# !!! Change my path into your work path.

export PATH=$PATH:/home/buzehao/miniconda3/bin

cd /data/buzehao/NMC/NMC/spiders

if [ ! -d /home/buzehao/logs ];then
  mkdir /home/buzehao/logs
fi

scrapy crawl $project > /home/buzehao/logs/log_$project
