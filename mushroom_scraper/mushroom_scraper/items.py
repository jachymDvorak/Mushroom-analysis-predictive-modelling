# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
import re
from scrapy.item import Item, Field
from scrapy.loader.processors import MapCompose

def remove_ws(value):
    value = value.strip()

class Mushroom(scrapy.Item):

    jmeno = scrapy.Field(input_processor=MapCompose(remove_ws))
    latin = scrapy.Field(input_processor=MapCompose(remove_ws))
    vyskyt_doba = scrapy.Field(input_processor=MapCompose(remove_ws))
    vyskyt_misto = scrapy.Field(input_processor=MapCompose(remove_ws))
    jedla = scrapy.Field(input_processor=MapCompose(remove_ws))
    tren_tvar = scrapy.Field(input_processor=MapCompose(remove_ws))
    tren_barva = scrapy.Field(input_processor=MapCompose(remove_ws))
    tren_povrch = scrapy.Field(input_processor=MapCompose(remove_ws))
    konzistence = scrapy.Field(input_processor=MapCompose(remove_ws))
    klobouk_povrch = scrapy.Field(input_processor=MapCompose(remove_ws))
    klobouk_barva = scrapy.Field(input_processor=MapCompose(remove_ws))
    klobouk_tvar = scrapy.Field(input_processor=MapCompose(remove_ws))
    vune = scrapy.Field(input_processor=MapCompose(remove_ws))
    chut = scrapy.Field(input_processor=MapCompose(remove_ws))
    hymenofor = scrapy.Field(input_processor=MapCompose(remove_ws))
    prsten = scrapy.Field(input_processor=MapCompose(remove_ws))
    pochva = scrapy.Field(input_processor=MapCompose(remove_ws))
    
    
