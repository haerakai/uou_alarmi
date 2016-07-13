# -*- coding:utf-8 -*-
__author__ = 'haerakai & molkoo'

import scrapy
from uou_alarmi.items import UouAlarmiItem
import urllib
import os

class UouSpider(scrapy.Spider):
	name = "uou_spider"

	def start_requests(self):
		yield scrapy.Request("http://www.ulsan.ac.kr/utopia/info/arbeit/arbeit.aspx?o=L", self.parse_arbeit)
		yield scrapy.Request("http://www.ulsan.ac.kr/utopia/info/barter/barter.aspx?o=L", self.parse_barter)

	def parse_arbeit(self, response):
		for sel in response.xpath('//tbody/tr'):
			item = UouAlarmiItem()
						
			item['source'] = 'utopia'
			item['category'] = 'arbeit'
			item['date'] = sel.xpath('td[1]/span/text()').extract()[0]
			item['name'] = sel.xpath('td[2]/span/a/@title').extract()[0]
			item['title'] = sel.xpath('td[3]/span[1]/a/@title').extract()[0]
			item['link'] = sel.xpath('td[3]/span[1]/a/@href').extract()[0]
			item['number'] = 'None'

			print 'a'*50
			print item['title']
			
			yield item

	def parse_barter(self, response):
		for sel in response.xpath('//tbody/tr'):
			item = UouAlarmiItem()

			item['source'] = 'utopia'
			item['category'] = 'barter'
			item['date'] = sel.xpath('td[6]/span/text()').extract()[0]
			item['name'] = sel.xpath('td[3]/span/@title').extract()[0]
			item['title'] = sel.xpath('td[2]/span[2]/a/@title').extract()[0]
			item['link'] = sel.xpath('td[2]/span[2]/a/@href').extract()[0]
			item['number'] = sel.xpath('td[1]/span/text()').extract()[0]
			
			print 'b'*50
			print item['title']

			yield item
