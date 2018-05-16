from scrapy import Spider, Request
from seatgeek.items import SeatgeekItem

class Seatgeek(Spider):
	name = 'seatgeek_spider'
	allowed_urls = ['https://seatgeek.com/']
	start_urls = [
	"https://seatgeek.com/venues/music-hall-of-williamsburg/tickets",
	"https://seatgeek.com/venues/brooklyn-steel-1/tickets",
	'https://seatgeek.com/venues/rough-trade-nyc/tickets',
	"https://seatgeek.com/venues/aisle-5-1/tickets", 
	"https://seatgeek.com/venues/fete-music-hall-2/tickets",
	"https://seatgeek.com/venues/gasa-gasa/tickets",
	"https://seatgeek.com/venues/great-scott/tickets",
	"https://seatgeek.com/venues/rams-head-live/tickets",
	"https://seatgeek.com/venues/royale-boston/tickets",
	"https://seatgeek.com/venues/saturn/tickets",
	"https://seatgeek.com/venues/starland-ballroom/tickets",
	"https://seatgeek.com/venues/terminal-5/tickets",
	"https://seatgeek.com/venues/terminal-west/tickets",
	"https://seatgeek.com/venues/the-earl/tickets",
	"https://seatgeek.com/venues/the-national/tickets",
	"https://seatgeek.com/venues/the-norva/tickets",
	"https://seatgeek.com/venues/the-sinclair/tickets",
	"https://seatgeek.com/venues/underground-arts/tickets",
	"https://seatgeek.com/venues/variety-playhouse/tickets"

	]


	# these venues only have one page of tickets 
	#x Fête Music Hall - Lounge       4
	#x Gasa Gasa                     17
	#x Great Scott                   50
	#x Rams Head Live!               22
	#x Starland Ballroom              6
	#x Terminal 5                     7
	#x The EARL                       6
	#x The National                  31
	# Underground Arts              14

	def parse(self, response):
		try:
			text = response.xpath('//li[@class="page numbered paging-last"]/a/text()').extract()

		except:
			pass

		try:
			total_pages = int(text[0])
		except:
			pass

			# Music Hall of Williamsburg
		if str(response) == '<200 https://seatgeek.com/venues/music-hall-of-williamsburg/tickets>':
			venue = ['https://seatgeek.com/venues/music-hall-of-williamsburg/tickets?page={}'.format(x) for x in range(1, total_pages+1)]
			
			# Brooklyn Steel
		elif str(response) == '<200 https://seatgeek.com/venues/brooklyn-steel-1/tickets>':
			venue = ['https://seatgeek.com/venues/brooklyn-steel-1/tickets?page={}'.format(x) for x in range(1, total_pages+1)]
 			
 			# Aisle 5
		elif str(response) == '<200 https://seatgeek.com/venues/aisle-5-1/tickets>':
			venue = ['https://seatgeek.com/venues/aisle-5-1/tickets?page={}'.format(x) for x in range(1, total_pages+1)]

			# Fête Music Hall
		elif str(response) == '<200 https://seatgeek.com/venues/fete-music-hall-2/tickets>':
			venue = ['https://seatgeek.com/venues/fete-music-hall-2/tickets']

			# Gasa Gasa                     17
		elif str(response) == '<200 https://seatgeek.com/venues/gasa-gasa/tickets>':
 			venue = ['https://seatgeek.com/venues/gasa-gasa/tickets']

			# Great Scott                   50
		elif str(response) == '<200 https://seatgeek.com/venues/great-scott/tickets>':
 			venue = ['https://seatgeek.com/venues/great-scott/tickets']

			# Rams Head Live!               22
		elif str(response) == '<200 https://seatgeek.com/venues/rams-head-live/tickets>':
 			venue = ['https://seatgeek.com/venues/rams-head-live/tickets']

			# Royale                        19
		elif str(response) == '<200 https://seatgeek.com/venues/royale-boston/tickets>':
 			venue = ['https://seatgeek.com/venues/royale-boston/tickets?page={}'.format(x) for x in range(1, total_pages+1)]

			# Saturn                        27
		elif str(response) == '<200 https://seatgeek.com/venues/saturn/tickets>':
 			venue = ['https://seatgeek.com/venues/saturn/tickets?page={}'.format(x) for x in range(1, total_pages+1)]

			# Starland Ballroom              6
		elif str(response) == '<200 https://seatgeek.com/venues/starland-ballroom/tickets>':
 			venue = ['https://seatgeek.com/venues/starland-ballroom/tickets']

			# Terminal 5                     7
		elif str(response) == '<200 https://seatgeek.com/venues/terminal-5/tickets>':
 			venue = ['https://seatgeek.com/venues/terminal-5/tickets']

			# Terminal West                  9
		elif str(response) == '<200 https://seatgeek.com/venues/terminal-west/tickets>':
 			venue = ['https://seatgeek.com/venues/terminal-west/tickets?page={}'.format(x) for x in range(1, total_pages+1)]

			# The EARL                       6
		elif str(response) == '<200 https://seatgeek.com/venues/the-earl/tickets>':
 			venue = ['https://seatgeek.com/venues/the-earl/tickets']

			# The National                  31
		elif str(response) == '<200 https://seatgeek.com/venues/the-national/tickets>':
 			venue = ['https://seatgeek.com/venues/the-national/tickets?page={}'.format(x) for x in range(1, total_pages+1)]

			# The NorVa                     28
		elif str(response) == '<200 https://seatgeek.com/venues/the-norva/tickets>':
 			venue = ['https://seatgeek.com/venues/the-norva/tickets?page={}'.format(x) for x in range(1, total_pages+1)]

			# The Sinclair                  55
		elif str(response) == '<200 https://seatgeek.com/venues/the-sinclair/tickets>':
 			venue = ['https://seatgeek.com/venues/the-sinclair/tickets?page={}'.format(x) for x in range(1, total_pages+1)]

			# Underground Arts              14
		elif str(response) == '<200 https://seatgeek.com/venues/underground-arts/tickets>':
 			venue = ['https://seatgeek.com/venues/underground-arts/tickets']

			# Variety Playhouse              7
		elif str(response) == '<200 https://seatgeek.com/venues/variety-playhouse/tickets>':
 			venue = ['https://seatgeek.com/venues/variety-playhouse/tickets?page={}'.format(x) for x in range(1, total_pages+1)]

 			# Rough Trade
		else:
			venue = ['https://seatgeek.com/venues/rough-trade-nyc/tickets?page={}'.format(x) for x in range(1, total_pages+1)]

		result_pages = venue

		for url in result_pages:
			yield Request(url=url, callback=self.parse_result_page) # callback is name of function you want use to parse result of the response from this url

		

	def parse_result_page(self, response):
		rows = response.xpath('//*[@class="carousel-content-wrapper"]/div')
		#showUrls = response.xpath('//a[@class="event-listing-title"]/@href').extract()

		for i in range(0, len(rows)+1):
			artist_name = rows[i].xpath('./div[2]/a/span/text()').extract_first()
			date = rows[i].xpath('./div/div[1]/text()').extract_first()
			time = rows[i].xpath('./div/div[2]/text()').extract_first()
			price = rows[i].xpath('./a/text()').extract_first()
			venue = rows[i].xpath('./div[2]/div/span/a/span/text()').extract_first()




			# artist_name = response.xpath('//span[@class="event-listing-title"]/text()').extract()
			# date = response.xpath('//div[@class="event-listing-date"]/text()').extract()
			# time = response.xpath('//div[@class="event-listing-time"]/text()').extract()
			# price = response.xpath('//a[@class="event-listing-button"]/text()').extract()

			#listUrls = ['https://seatgeek.com/' + x for x in showUrls]

			item = SeatgeekItem()
			item['artist_name'] = artist_name
			item['date'] = date
			item['time'] = time
			item['price'] = price
			item['venue'] = venue
			yield item

	# 	for url in listUrls:
	# 		yield Request(url=url, callback=self.parse_show_page)

	# def parse_show_page(self, response):
	# 	venue_address = response.xpath('//div[@class="event-info"]/h3/a/text()').extract()
	# 	venue = venue_address[0]
	# 	# print(50*"=")
	# 	# print(venue)
	# 	# print(50*"=")
	# 	# return

	# 	item = SeatgeekItem()
	# 	item['venue'] = venue
		
	# 	yield item

