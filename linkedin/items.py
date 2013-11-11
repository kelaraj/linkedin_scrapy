# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class LinkedinItem(Item):
  # define the fields for your item here:
  full_name = Field()
  first_name = Field()
  last_name = Field()
  headline_title = Field()
  locality = Field()
  industry = Field()
  current_roles = Field()
  education_institutions = Field()
