import scrapy
from urllib.parse import urljoin
from ..items import F1ResultsItem

class teamResults(scrapy.Spider):

    name = "teams"
    def start_requests(self):
        urls = ['https://www.formula1.com/en/results.html/2021/team.html',
                'https://www.formula1.com/en/results.html/2020/team.html',
                'https://www.formula1.com/en/results.html/2019/team.html',
                'https://www.formula1.com/en/results.html/2018/team.html',
                'https://www.formula1.com/en/results.html/2017/team.html',
                'https://www.formula1.com/en/results.html/2016/team.html',
                'https://www.formula1.com/en/results.html/2015/team.html',
                ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for q in response.css('tbody tr'):
            year = response.url.split('/')[-2]
            position = q.css('td.dark::text').get()
            team_name = q.css('td a::text').get()
            points = q.css('td.bold::text').get()
            yield{
                  "position":position, "team_name":team_name, 'points':points, "year":year
                  }

