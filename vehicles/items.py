# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class VehicleItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
    vin_number = scrapy.Field()
    vehicle_summary = scrapy.Field()
    top_features_specs = scrapy.Field()
