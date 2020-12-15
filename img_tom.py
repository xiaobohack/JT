# -*- coding: utf-8 -*-
# @Time    : 2020/12/15 21:28
# @Author  : Da Bai
# @file    :img_tom.py
# @softawre:PyCharm

from lxml import etree

import requests

url = 'https://tom180.com/meinvxiezhen/'

res = requests.get(url)
res.encoding = 'utf-8'
print(res.status_code)
typic = etree.HTML(res.text)

list_div = typic.xpath('.//*[@class="tvpic"]/a/@href')

for pic in list_div:
	img_list = 'https://tom180.com'+pic
	img = requests.get(img_list)
	img.encoding = 'utf-8'
	img_list1 = etree.HTML(img.text)
	list_url = img_list1.xpath('.//*[@class="container xiezhen"]/img/@src')
	list_name = img_list1.xpath('.//*[@class="container jianjie"]/ul/li[2]/text()')
	print(list_name)
	print(list_url)

