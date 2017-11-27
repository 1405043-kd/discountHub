# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from catalog.models import Book


class OlxPipeline(object):
    def process_item(self, item, spider):
        try:
            book = Book.objects.get(summary=item['url'])
            print "Book already exist"
            return item
        except Book.DoesNotExist:
            pass

        book = Book()
        
        book.title = item['title']
#        book.author = item['discount']
        book.summary = item['url']
       	book.save()
        return item

