import scrapy

class BrickSetSpider(scrapy.Spider):
    name = "ctf_crawler"
    start_urls = ['https://ctflearn.com/challenge/107']
