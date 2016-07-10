# -*- coding:utf-8 -*-
__author__ = 'haerakai & molkoo'

import scrapy
import urllib
import os

class UouSpider(scrapy.Spider):
	name = "uou_spider"
	allowed_domains = ["ulsan.ac.kr"]
	start_urls = [
		"http://www.ulsan.ac.kr/utopia/info/arbeit/arbeit.aspx?o=L"
	]

	def parse(self, response):
		home = os.path.expanduser("~")
		path_last = home + '/uou_alarmi/uou_alarmi/spiders/last'
		path_crawldb = home + '/uou_alarmi/uou_alarmi/spiders/crawldb'

		dates = []
		names = []
		titles = []
		links = []

		for sel in response.xpath('//tbody/tr'):
			dates.append(sel.xpath('td[1]/span/text()').extract()[0])
			names.append(sel.xpath('td[2]/span/a/@title').extract()[0])
			titles.append(sel.xpath('td[3]/span[1]/a/@title').extract()[0])
			links.append(sel.xpath('td[3]/span[1]/a/@href').extract()[0])

		if not os.path.exists(path_last):
			last = '0'
		else:
			with open(path_last, 'r') as f:
				last = f.read()

		n = len(links)
		with open(path_crawldb, 'w+') as f:
			for i in range(0,n):
				if int(last) >= int(str(links[i].encode('utf-8')[-5:])):
					break
				f.write(dates[i].encode('utf-8')+'\n')
				f.write(names[i].encode('utf-8')+'\n')
				f.write(titles[i].encode('utf-8')+'\n')
				f.write(links[i].encode('utf-8')+'\n')

		with open(path_last, 'w+') as f:
			last = str(links[0].encode('utf-8')[-5:])
			f.write(last.encode('utf-8'))

		os.system('~/.virtualenvs/alarmi/bin/python ~/uou_alarmi_bot/broad.py')

			
