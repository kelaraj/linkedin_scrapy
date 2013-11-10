from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from linkedin.items import LinkedinItem

class LinkedinSpider(CrawlSpider):
  name = "linkedin"
  allowed_domains = ["linkedin.com"]
  centilist_one = [i for i in xrange(1,100)]
  centilist_two = [i for i in xrange(1,100)]
  centilist_three = [i for i in xrange(1,100)]
  '''
  start_urls = ["http://www.linkedin.com/directory/people-%s-%d-%d-%d" 
                % (alphanum, num_one, num_two, num_three) 
                  for alphanum in "abcdefghijklmnopqrstuvwxyz"
                  for num_one in centilist_one
                  for num_two in centilist_two
                  for num_three in centilist_three
                ]
  '''
  start_urls = ["http://www.linkedin.com/directory/people-a-23-23-2"]

  rules = (
      Rule(SgmlLinkExtractor(allow=('\/pub\/.+', ))
                            , callback='parse_item'),
  )

  def parse_item(self, response):
    if response:
      hxs = HtmlXPathSelector(response)
      item = LinkedinItem()
      item['name'] = hxs.select('//span/span/text()').extract()
      # route duplicates
      if not item['name']:
        # parse each name in list
        # get each link from the profile page, pass it to parse_item
        #//*[@id="results"]/li[1]/div/h3/a/strong[2]
        #for profile in profile_list:
        #  self.parse_item(profile)
        print "duplicates"
        #return
      else:
        #first_name = item["name"][0]
        #last_name = item["name"][2]
        # insert into database
        print "not duplicates"
        #return
