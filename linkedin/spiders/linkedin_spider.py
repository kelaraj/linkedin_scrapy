from scrapy.spider import BaseSpider

class DmozSpider(BaseSpider):
    name = "linkedin"
    allowed_domains = ["linkedin.com"]
    start_urls = [
        "http://www.linkedin.com/directory/people-%s" % alphanum for alphanum in 
        "abcdefghijklmnopqrstuvwxyz"
        ]

    def parse(self, response):
        filename = response.url.split("/")[-1]
        open(filename, 'wb').write(response.body)
