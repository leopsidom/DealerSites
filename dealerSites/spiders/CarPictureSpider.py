from dealerSites.items import DealersitesItem
import datetime
import scrapy


class CarPictureSpider(scrapy.Spider):

    name = "car-pictures"
    start_urls = ["http://www.familydeal.com/search/used/tp/?yr=2016&pcdi_debug=true"]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'})

    def parse(self, response):
		# let's only gather Time U.S. magazine covers
        img = response.xpath("//img/@src")
        imageURL = [response.urljoin(url) if not url.startswith("http") else url for url in img.extract()]

		# grab the title and publication date of the current issue
        title = response.css("img").xpath("@alt").extract_first()

		# yield the result
        yield DealersitesItem(title=title, file_urls=imageURL)
