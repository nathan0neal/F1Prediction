# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class F1ResultsItem(scrapy.Item):
    place = scrapy.Field()
    driver = scrapy.Field()
    team_name = scrapy.Field()
    Number = scrapy.Field()
    laps = scrapy.Field()
    points = scrapy.Field()
    year = scrapy.Field()
    country = scrapy.Field()
    time = scrapy.Field()
    position = scrapy.Field()

    def visit(self, visitor):
        visitor.visit_race(self)
