from scrapy import Spider, Request
from bowery.items import BoweryItem

class Bowery(Spider):
	name = 'bowery_spider'
	allowed_urls = ['https://www.bowerypresents.com/']
	start_urls = ['https://www.bowerypresents.com/info/events/get?scope=all']

	def parse(self, response):
		total_pages = 20
		result_pages = ['https://www.bowerypresents.com/info/events/get?scope=all&page={}&rows=49'.format(x) for x in range(1, total_pages+1)]
		
		for url in result_pages:
			yield Request(url=url, callback=self.parse_result_page) # callback is name of function you want use to parse result of the response from this url

	def parse_result_page(self, response):
		rows = response.xpath('//*[@class="show-item"]')

		for i in range(0, len(rows)+1):
			headline_artist_name = rows[i].xpath('./div/div[2]/div/div/div/div/h3/a/text()').extract_first()
			other_artists_name = rows[i].xpath('./div/div[2]/div/div/div/div/h3/div/span/text()').extract_first()
			date = rows[i].xpath('./div/div[2]/div/div/ul/li[2]/p/text()').extract_first()
			time = rows[i].xpath('./div/div[2]/div/div/ul/li[2]/p/span/text()').extract_first()
			price = rows[i].xpath('./div/div[2]/div/div/ul/li[3]/p/text()').extract_first()
			venue = rows[i].xpath('./div/div[2]/div/div/ul/li/p/strong/text()').extract_first()
			location = rows[i].xpath('./div/div[2]/div/div/ul/li/p/span/text()').extract_first()
			button = rows[i].xpath('./div/div[2]/div/div[2]/a[2]/text()').extract_first()

			item = BoweryItem()
			item['headline_artist_name'] = headline_artist_name
			item['other_artists_name'] = other_artists_name
			item['date'] = date
			item['time'] = time
			item['price'] = price
			item['venue'] = venue
			item['location'] = location
			item['button'] = button
			yield item

