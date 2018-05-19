# -*- coding: utf-8 -*-
import scrapy


class ShopcluesSpider(scrapy.Spider):
    name = "shopclues"
    start_urls = (
        'https://www.shopclues.com/mobiles-featured-store-4g-smartphone.html',
    )

    custom_settings = {
    	'FEED_URI' : 'tmp/shopclues.csv'
    }

    def parse(self, response): 
     	titles = response.css('img::attr(title)').extract()
      	images = response.css('img::attr(data-img)').extract()
       	prices = response.css('.p_price::text').extract()
       	discounts = response.css('.prd_discount::text').extract()

       	for item in zip(titles,images,prices,discounts):
       			yield {       
       				'title' : item[0],
       				'price' : item[2],
       				'image_urls' : [item[1],],
 					'discounts' : item[3],
 					}