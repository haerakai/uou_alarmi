# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from __future__ import unicode_literals
import json
import codecs

class UouAlarmiPipeline(object):
	def __init__(self):
		self.arbeit_file = codecs.open('arbeit.json', 'w', encoding='utf-8')    	
		self.room_file = codecs.open('room.json', 'w', encoding='utf-8')
		self.barter_file = codecs.open('barter.json', 'w', encoding='utf-8')

	def process_item(self, item, spider):
        	line = json.dumps(dict(item), ensure_ascii=False)+"\n"
		category = item['category']
		
		if category=='arbeit':
			self.arbeit_file.write(line)

		elif category=='room':
			self.room_file.write(line)

		else:
			self.barter_file.write(line)
		return item

	def spider_closed(self, spider):
		self.barter_file.close()
		self.room_file.close()
		self.arbeit_file.close()
