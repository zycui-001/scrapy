# -*- coding: utf-8 -*-
import scrapy
from shiyanlou.items import CourseItem


class CoursesSpider(scrapy.Spider):
    name = 'courses'
    @property 
    def start_urls(self):
    	url_tmp1 = 'https://www.shiyanlou.com/courses/?category=all&course_type=all&fee=all&tag=all&page={}'
    	return (url_tmp1.format(i) for i in range(1, 25))
#    allowed_domains = ['shiyanlou.com']
#    start_urls = ['http://shiyanlou.com/']

    def parse(self, response):
        for course in response.css('div.course-body'):
        	item = CourseItem({
        		'name': course.css('div.course-name::text').extract_first(),
        		'description': course.css('div.course-desc::text').extract_first(),
        		'type': course.css('div.course-footer span.pull-right::text').extract_first(default='免费'),
        		'students': course.xpath('.//span[contains(@class, "pull-left")]/text()[2]').re_first('[^\d]*(\d*)[^\d]*')
        		})
        	yield item

