# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class UouAlarmiItemArbeit(scrapy.Item):
	category = scrapy.Field() #카테고리
	date = scrapy.Field() #날짜
	name = scrapy.Field() #이름
	link = scrapy.Field() #링크
	title = scrapy.Field() #제목
	pass
	
class UouAlarmiItemRoom(scrapy.Item):
	category = scrapy.Field()
	num = scrapy.Field() #글번호
	location = scrapy.Field() #위치
	title = scrapy.Field() #제목
	cost = scrapy.Field() #비용
	date = scrapy.Field() #날짜
	link = scrapy.Field() #링크
	pass

class UouAlarmiItemBarter(scrapy.Item):
	category = scrapy.Field()
	num = scrapy.Field() #글번호
	title = scrapy.Field() #제목
	name = scrapy.Field() #글쓴이
	date = scrapy.Field() #날짜
	pass
