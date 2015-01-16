from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from linkedin.items import LinkedinItem


class LinkedinSpider(CrawlSpider):

    """
    Define the crawler's start URIs, set its follow rules, parse HTML
    and assign values to an item. Processing occurs in ../pipelines.py
    """

    name = "linkedin"
    allowed_domains = ["linkedin.com"]

    # Uncomment the following lines for full spidering
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
    
    # Temporary start_urls for testing; remove and use the above start_urls in production
    start_urls = ["http://www.linkedin.com/directory/people-a-23-23-2"]
    # TODO: allow /in/name urls too?
    rules = (Rule(SgmlLinkExtractor(allow=('\/pub\/.+')), callback='parse_item'))

    def parse_item(self, response):
        if response:
            hxs = HtmlXPathSelector(response)
            item = LinkedinItem()
            # TODO: is this the best way to check that we're scraping the right page?
            item['full_name'] = hxs.select('//*[@id="name"]/span/span/text()').extract()
            if not item['full_name']:

                # recursively parse list of duplicate profiles
                # NOTE: Results page only displays 25 of possibly many more names;
                # LinkedIn requests authentication to see the rest. Need to resolve

                # TODO: add error checking here to ensure I'm getting the right links
                # and links from "next>>" pages
                multi_profile_urls = hxs.select('//*[@id="result-set"]/li/h2/strong/ \
                                          a/@href').extract()
                for profile_url in multi_profile_urls:
                    yield Request(profile_url, callback=self.parse_item)
            else:
                item['first_name'], 
                item['last_name'], 
                item['full_name'],
                item['headline_title'],
                item['locality'], 
                item['industry'], 
                item['current_roles'] = item['full_name'][0], 
                                        item['full_name'][1], 
                                        hxs.select('//*[@id="name"]/span/span/text()').extract(),
                                        hxs.select('//*[@id="member-1"]/p/text()').extract(),
                                        hxs.select('//*[@id="headline"]/dd[1]/span/text()').extract(),
                                        hxs.select('//*[@id="headline"]/dd[2]/text()').extract(),
                                        hxs.select('//*[@id="overview"]/dd[1]/ul/li/text()').extract()
                # TODO: add metadata fields

                if hxs.select('//*[@id="overview"]/dt[2]/text()').extract() == [u' \n       Education\n    ']:
                    item['education_institutions'] = hxs.select('//*[@id="overview"]/dd[2]/ul/li/text()').extract()
                print item
        else:
            print "Uh oh, no response."
            return
