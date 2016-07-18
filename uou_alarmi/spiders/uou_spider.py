# -*- coding:utf-8 -*-
__author__ = 'haerakai & molkoo'

import scrapy
import urllib
import os
import MySQLdb.cursors

from uou_alarmi.items import UouAlarmiItemArbeit, UouAlarmiItemRoom, UouAlarmiItemBarter

class UouSpider(scrapy.Spider):
	name = "uou_spider"

	def start_requests(self):
		try:
			self.conn = MySQLdb.connect(user='user', passwd='passwd', db='uou_alarmi', host='localhost', charset='utf8', use_unicode='True')
			self.cursor = self.conn.cursor()

			self.cursor.execute('select arbeit, room, barter from uou_alarmi_last')
			self.result = self.cursor.fetchone()
		except MySQL.Error, e:
			print "Error %d: %s" % (e.args[0], e.args[1])
			sys.exit(1)
			
		yield scrapy.Request("http://www.ulsan.ac.kr/utopia/info/arbeit/arbeit.aspx?o=L", self.parse_arbeit)
		yield scrapy.Request("http://www.ulsan.ac.kr/utopia/info/room/room.aspx?o=L", self.parse_room)
		yield scrapy.Request("http://www.ulsan.ac.kr/utopia/info/barter/barter.aspx?o=L", self.parse_barter)

	def parse_arbeit(self, response):
		item = UouAlarmiItemArbeit()
		flag = 0
		
		for sel in response.xpath('//tbody/tr'):
			item['category'] = 'arbeit'
			item['date'] = sel.xpath('td[1]/span/text()').extract()[0]
			item['name'] = sel.xpath('td[2]/span/a/@title').extract()[0]
			item['title'] = sel.xpath('td[3]/span[1]/a/@title').extract()[0]
			item['link'] = sel.xpath('td[3]/span[1]/a/@href').extract()[0]
			item['num'] = sel.xpath('td[3]/span[1]/a/@href').extract()[0][-5:]	
			if self.result[0] >= int(item['num']):
				break

			yield item
		self.cursor.execute('update uou_alarmi_last set arbeit = %s' % response.xpath('//tbody/tr[1]/td[3]/span[1]/a/@href').extract()[0][-5:])
		self.conn.commit()

	def parse_room(self, response):
		item = UouAlarmiItemRoom()
		
		for sel in response.xpath('//tbody/tr'):
			item['category'] = 'room'
			item['num'] = sel.xpath('td[1]/span/text()').extract()[0]
			item['location'] = sel.xpath('td[2]/span/text()').extract()[0]
			item['title'] = sel.xpath('td[3]/span[1]/a/@title').extract()[0]
			item['cost'] = sel.xpath('td[4]/span/text()').extract()[0]
			item['date'] = sel.xpath('td[5]/span/text()').extract()[0]
			item['link'] = sel.xpath('td[3]/span[1]/a/@href').extract()[0]
			if self.result[1] >= int(item['num']):
				break
			
			yield item
		self.cursor.execute('update uou_alarmi_last set room = %s' % response.xpath('//tbody/tr[1]/td[1]/span/text()').extract()[0])
		self.conn.commit()

	def parse_barter(self, response):
		item = UouAlarmiItemBarter()

		for sel in response.xpath('//tbody/tr'):
			item['category'] = 'barter'
			item['num'] = sel.xpath('td[1]/span/text()').extract()[0]
			item['title'] = sel.xpath('td[2]/span[2]/a/@title').extract()[0]
			item['name'] = sel.xpath('td[3]/span/text()').extract()[0]
			item['date'] = sel.xpath('td[6]/span/text()').extract()[0]
			item['link'] = sel.xpath('td[2]/span[2]/a/@href').extract()[0]
			if self.result[2] >= int(item['num']):
				break
				
			yield item
		self.cursor.execute('update uou_alarmi_last set barter = %s' % response.xpath('//tbody/tr[1]/td[1]/span/text()').extract()[0])
		self.conn.commit()

