from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from linkedin.items import LinkedinItem

class DmozSpider(BaseSpider):
  name = "linkedin"
  allowed_domains = ["linkedin.com"]
  start_urls = ["http://www.linkedin.com/directory/people-%s" % alphanum 
                for alphanum in "abcdefghijklmnopqrstuvwxyz"]

  def parse(self, response):
    hxs = HtmlXPathSelector(response)
    sites = hxs.select('//ul[2]/li')
    items = []
#    for site in sites:
#      item = LinkedinItem()
#      item['name'] = site.select('a/text()').extract()
#      items.append(item)

    filename = "./testdata/" + response.url.split("/")[-1]
    open(filename, 'wb').write(response.body)