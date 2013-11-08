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
  start_urls = ["http://www.linkedin.com/directory/people-%s-%d-%d-%d" 
                % (alphanum, num_one, num_two, num_three) 
                  for alphanum in "abcdefghijklmnopqrstuvwxyz"
                  for num_one in centilist_one
                  for num_two in centilist_two
                  for num_three in centilist_three
                ]
  

  '''
  rules = (Rule 
            (SgmlLinkExtractor(allow=("-\d", "-\d-\d", "-\d-\d-\d")), 
              callback="parse_items",
              follow=True),
          )
  '''


  def parse_items(self, response):
    hxs = HtmlXPathSelector(response)
    sites = hxs.select('//ul[2]/li')
    items = []
#    for site in sites:
#      item = LinkedinItem()
#      item['name'] = site.select('a/text()').extract()
#      items.append(item)

    filename = "./testdata/" + response.url.split("/")[-1]
    open(filename, 'wb').write(response.body)