# Scrapy settings for linkedin project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'linkedin'

SPIDER_MODULES = ['linkedin.spiders']
NEWSPIDER_MODULE = 'linkedin.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'thehackertrail (+http://www.thehackertrail.herokuapp.com)'

# Automatically throttles crawling speed based on load of both the Scrapy 
# server and the website being crawled
AUTOTHROTTLE_ENABLED = True

ITEM_PIPELINES = ["linkedin.pipelines.LinkedinPipeline"]