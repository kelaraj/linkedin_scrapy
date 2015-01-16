# Define item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

class LinkedinPipeline(object):
    def process_item(self, item, spider):
        # TODO: dedupe records, clean up HTML
        return item
