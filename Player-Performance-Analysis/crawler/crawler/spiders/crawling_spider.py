import scrapy
from crawler.items import MyItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class MySpider(CrawlSpider):
    name = "my_spider"

    start_urls = [
        'http://espncricinfo.com/cricketers',
    ]

    allowed_domains = ['espncricinfo.com']
    visited_urls = set()
    new_links_count = 0  

    rules = (
        Rule(
            LinkExtractor(allow="cricketers"),
            callback="parse_item",
            follow=True
        ),
    )

    def parse_item(self, response):

        for link in response.css('a::attr(href)').extract():
            if self.should_follow_link(link):
                item = MyItem()
                item['url'] = response.urljoin(link)
                yield item

        self.new_links_count += 1  

    def should_follow_link(self, link):
        if "/bowling-batting-stats" in link and link not in self.visited_urls:
            self.visited_urls.add(link)
            return True

        return False


    def closed(self, reason):
        if self.new_links_count == 0:
            self.logger.info("No new links to follow. Stopping the spider.")
            raise scrapy.exceptions.CloseSpider(reason='No new links')
