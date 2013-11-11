# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

class LinkedinPipeline(object):
    def process_item(self, item, spider):
        return item

# Add Mongodb pipeline, dedupe

# Clean HTML
# strip/clean headline_title, locality

# DUPLICATE CHECK

#from scrapy import signals
#from scrapy.exceptions import DropItem

#class LinkedinPipeline(object):

#    def __init__(self):
#        self.ids_seen = set()

#    def process_item(self, item, spider):
#        if item['id'] in self.ids_seen:
#            raise DropItem("Duplicate item found: %s" % item)
#        else:
#            self.ids_seen.add(item['id'])
#            return item
