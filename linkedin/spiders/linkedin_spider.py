from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from linkedin.items import LinkedinItem

# compile to C using Cython if processing speed becomes a constraint

class LinkedinSpider(CrawlSpider):
  
  """
  Define the crawler's start urls, set its follow rules, parse HTML
  and assign values to an item. Processing occurs in ../pipelines.py
  """

  name = "linkedin"
  allowed_domains = ["linkedin.com"]
  
  # TODO: uncomment following lines for full spidering
  '''
  centilist_one = (i for i in xrange(1,100))
  centilist_two = (i for i in xrange(1,100))
  centilist_three = (i for i in xrange(1,100))
  start_urls = ["http://www.linkedin.com/directory/people-%s-%d-%d-%d" 
                % (alphanum, num_one, num_two, num_three) 
                  for alphanum in "abcdefghijklmnopqrstuvwxyz"
                  for num_one in centilist_one
                  for num_two in centilist_two
                  for num_three in centilist_three
                ]
  '''
  # temporary start url, remove for production
  start_urls = ["http://www.linkedin.com/directory/people-a-23-23-2"]
  # TODO: allow /in/name urls too? (LinkedIn custom URLs)
  rules = (Rule(SgmlLinkExtractor(allow=('\/pub\/.+', ))
                , callback='parse_item'),
          )

  def parse_item(self, response):
    if response:
      hxs = HtmlXPathSelector(response)
      item = LinkedinItem()
      # is this the best way to check that I'm scraping the right page?
      item['full_name'] = hxs.select('//*[@id="name"]/span/span/text()').extract()
      if not item['full_name']:
        # recursively parse list of duplicate profiles
        # NOTE: Results page only displays 25 of possibly many more names;
        # LinkedIn requests authentication to see the rest. Need to resolve
        # Fake account and log-in?
        
        # TODO: add error checking here to ensure I'm getting the right links
        # and links from "next>>" pages
        multi_profile_urls = hxs.select('//*[@id="result-set"]/li/h2/strong/ \
                                          a/@href').extract()
        for profile_url in multi_profile_urls:
          yield Request(profile_url, callback=self.parse_item)
      else:
        # add meta fields (date crawled/updated, etc)
        item['first_name'] = item['full_name'][0]
        item['last_name'] = item['full_name'][1]
        item['full_name'] = hxs.select('//*[@id="name"]/span/span/text()').extract()
        item['headline_title'] = hxs.select('//*[@id="member-1"]/p/text() \
                                            ').extract()
        item['locality'] = hxs.select('//*[@id="headline"]/dd[1]/span/text() \
                                            ').extract()
        item['industry'] = hxs.select('//*[@id="headline"]/dd[2]/text() \
                                            ').extract()
        item['current_roles'] = hxs.select('//*[@id="overview"]/dd[1]/ul/li/ \
                                                          text()').extract()
        # TODO: dynamically check for header of field, assign to object
        # via variable
        if hxs.select('//*[@id="overview"]/dt[2]/text()\
                                ').extract() == [u' \n       Education\n    ']:
          item['education_institutions'] = hxs.select('//*[@id="overview"]/\
                                                dd[2]/ul/li/text()').extract()
        # for debugging
        print item
