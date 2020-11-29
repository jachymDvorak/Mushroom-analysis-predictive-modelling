# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 15:39:11 2020

@author: JáchymDvořák
"""

from mushroom_scraper.items import Mushroom
import scrapy

class MushroomSpider(scrapy.Spider):
    
    name = 'MushroomSpider'
    
    def start_requests(self):
        start_urls = ['https://www.nahoubach.cz/atlas-hub/#houby/']
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse_main)
            
    def parse_main(self, response):
        card_links = response.xpath('//*[@id="atlas_mushrooms"]//a/@href')
        urls_to_follow = card_links.extract()
        for url in urls_to_follow:
            yield response.follow(url = url, callback = self.parse_cards)
       
        next_page = response.xpath('//li[@class="next"]/a/@href').extract_first()
        if next_page is not None:
            next_page_url = response.urljoin(next_page)
            yield scrapy.Request(url = next_page_url, callback = self.parse_main)
   
    def parse_cards(self, response):
        item = Mushroom()
        item['jmeno'] = response.css('h1.block_heading::text').extract()
        item['latin'] = response.css('h1.block_heading > i::text').extract()
        item['vyskyt_doba'] = str(response.xpath('normalize-space(//*[@id="mushroom_detail"]/tbody/tr[1]/td[1]/text())').extract())
        item['vyskyt_misto'] = str(response.xpath('normalize-space(//*[@id="mushroom_detail"]/tbody/tr[2]/td[1]/text())').extract())
        item['jedla'] = str(response.xpath('normalize-space(//*[@id="mushroom_detail"]/tbody/tr[3]/td[1]/text())').extract())
        item['tren_tvar'] = str(response.xpath('normalize-space(//*[@id="mushroom_detail"]/tbody/tr[4]/td[1]/text())').extract())
        item['tren_barva'] = str(response.xpath('normalize-space(//*[@id="mushroom_detail"]/tbody/tr[7]/td[1]/text())').extract())
        item['tren_povrch'] = str(response.xpath('normalize-space(//*[@id="mushroom_detail"]/tbody/tr[6]/td[1]/text())').extract())
        item['konzistence'] = str(response.xpath('normalize-space(//*[@id="mushroom_detail"]/tbody/tr[5]/td[1]/text())').extract())
        item['klobouk_povrch'] = str(response.xpath('normalize-space(//*[@id="mushroom_detail"]/tbody/tr[4]/td[2]/text())').extract())
        item['klobouk_barva'] = str(response.xpath('normalize-space(/html/body/div[2]/section[1]/div/div[2]/div/div/div[1]/table/tbody/tr[1]/td[2]/text())').extract())
        item['klobouk_tvar'] = str(response.xpath('normalize-space(//*[@id="mushroom_detail"]/tbody/tr[2]/td[2]/text())').extract())
        item['vune'] = str(response.xpath('normalize-space(//*[@id="mushroom_detail"]/tbody/tr[8]/td[2]/text())').extract())
        item['chut'] = str(response.xpath('normalize-space(//*[@id="mushroom_detail"]/tbody/tr[7]/td[2]/text())').extract())
        item['hymenofor'] = str(response.xpath('normalize-space(//*[@id="mushroom_detail"]/tbody/tr[8]/td[1]/text())').extract())
        item['prsten'] = str(response.xpath('normalize-space(//*[@id="mushroom_detail"]/tbody/tr[5]/td[2]/text())').extract())
        item['pochva'] = str(response.xpath('normalize-space(//*[@id="mushroom_detail"]/tbody/tr[6]/td[2]/text())').extract())
        
        return item
        
