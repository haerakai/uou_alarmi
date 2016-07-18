# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from __future__ import unicode_literals
import MySQLdb.cursors

class UouAlarmiPipeline(object):
	def __init__(self):
		try:
			self.conn = MySQLdb.connect(user='alarmi', passwd='alarmi', db='uou_alarmi', host='localhost', charset='utf8', use_unicode='True')
			self.cursor = self.conn.cursor()

			self.cursor.execute("delete uou_alarmi_barter, uou_alarmi_arbeit, uou_alarmi_room from uou_alarmi_barter, uou_alarmi_arbeit, uou_alarmi_room")
			self.conn.commit()

		except MySQLdb.Error, e:
			print "Error %d: %s" % (e.args[0], e.args[1])
			sys.exit(1)

	def process_item(self, item, spider):
		category = item['category']
		#num = int(item['num'])
		
		if category=='arbeit': #모두 저장
		#if ((category=='arbeit') & (self.row[0]<num)): #해당 번호 위로 저장- arbeit
			try:	
				self.cursor.execute("insert into uou_alarmi.uou_alarmi_arbeit(date, name, link, title, num) values(%s, %s, %s, %s, %s)", (item['date'].encode('utf-8'), item['name'].encode('utf-8'), "http://www.ulsan.ac.kr/utopia/info/arbeit/"+item['link'].encode('utf-8'), item['title'].encode('utf-8'), item['num'].encode('utf-8')))
		
			except MySQLdb.Error, e:
				print "Error %d: %s" % (e.args[0], e.args[1])
				sys.exit(1)

		elif category=='room': #모두 저장
		#elif((category=='room') & (self.row[1]<num)): #해당 번호 위로 저장- room
			try:
				self.cursor.execute("insert into uou_alarmi.uou_alarmi_room(num, title, cost, link, location, date) values(%s, %s, %s, %s, %s, %s)", (item['num'].encode('utf-8'), item['title'].encode('utf-8'), item['cost'].encode('utf-8'), "http://www.ulsan.ac.kr/utopia/info/room/"+item['link'].encode('utf-8'), item['location'].encode('utf-8'), item['date'].encode('utf-8')))

			except MySQLdb.Error, e:
				print "Error %d: %s" % (e.args[0], e.args[1])
				sys.exit(1)
		else: #모두 저장
		#elif((category=='barter') & (self.row[2]<num)): #해당 번호 위로 저장 - barter
			try:
				self.cursor.execute("insert into uou_alarmi.uou_alarmi_barter(date, name, num, title, link) values(%s, %s, %s, %s, %s)", (item['date'].encode('utf-8'), item['name'].encode('utf-8'), item['num'].encode('utf-8'), item['title'].encode('utf-8'), "http://www.ulsan.ac.kr/utopia/info/barter/"+item['link'].encode('utf-8')))

			except MySQLdb.Error, e:
				print "Error %d: %s" % (e.args[0], e.args[1])
				sys.exit(1)

		self.conn.commit()
		return item

	def spider_closed(self, spider):
		self.conn.close()
