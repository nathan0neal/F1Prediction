import scrapy
from urllib.parse import urljoin
from ..items import F1ResultsItem

class allResults(scrapy.Spider):

    name = "allResults"
    allowed_domains = ["www.formula1.com"]
    start_urls = ['https://www.formula1.com/en/results.html/{}/races.html'.format(i) for i in range(1958,2022)]
    def parse(self, response):
        raceLinks = response.xpath('//td//a/@href').extract()
        for p in raceLinks:
            url = urljoin(response.url, p)
            yield scrapy.Request(url, callback=self.parse_Races)

    def parse_Races(self, response):
        for q in response.css('tbody tr'):
            place = response.xpath('//title/text()').extract()
            country = response.url.split('/')[-2]
            year = response.url.split('/')[-5]
            position = q.css('td.dark::text').get()
            driver = q.css('td span::text').getall()[1]
            team_name = q.css('td.semi-bold::text').get()
            Number = q.css('td.dark.hide-for-mobile::text').get()
            laps = q.css('td.bold.hide-for-mobile::text').get()
            time = q.css('td.dark.bold::text').getall()[4]
            points = q.css('td.bold::text').getall()[-1]
            rank = response.url.split('/')[-3]
            yield{ 'circuit': place, 'position': position, 'driver':driver,
                   "team_name":team_name, 'No':Number, 'laps':laps, 'time':time, 'points':points, 'Year':year,
                   'Place':country, "Race Rank" : rank
                   }

