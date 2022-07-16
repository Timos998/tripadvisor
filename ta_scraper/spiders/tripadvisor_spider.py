import scrapy
from ..items import TaScraperItem
from scrapy import Request
from scrapy.linkextractors import LinkExtractor

class TripadvisorSpiderSpider(scrapy.Spider):
    name = 'tripadvisor_spider'
    #allowed_domains = ['tripadvisor.com']
    start_urls = ['https://www.tripadvisor.com/Hotels-g188590-Amsterdam_North_Holland_Province-Hotels.html',\
                  'https://www.tripadvisor.com/Hotels-g188632-Rotterdam_South_Holland_Province-Hotels.html',\
                  'https://www.tripadvisor.com/Hotels-g1024767-Haarlemmermeer_North_Holland_Province-Hotels.html',\
                  'https://www.tripadvisor.com/Hotels-g188633-The_Hague_South_Holland_Province-Hotels.html',\
                  'https://www.tripadvisor.com/Hotels-g188616-Utrecht-Hotels.html',\
                  'https://www.tripadvisor.com/Hotels-g806327-Almere_Flevoland_Province-Hotels.html',\
                  'https://www.tripadvisor.com/Hotels-g188582-Eindhoven_North_Brabant_Province-Hotels.html',\
                  'https://www.tripadvisor.com/Hotels-g1024752-Amstelveen_North_Holland_Province-Hotels.html',\
                  'https://www.tripadvisor.com/Hotels-g188572-Groningen-Hotels.html',\
                  'https://www.tripadvisor.com/Hotels-g188593-Haarlem_North_Holland_Province-Hotels.html',\
                  'https://www.tripadvisor.com/Hotels-g188630-Leiden_South_Holland_Province-Hotels.html',\
                  'https://www.tripadvisor.com/Hotels-g188575-Maastricht_Limburg_Province-Hotels.html',\
                  'https://www.tripadvisor.com/Hotels-g188605-Enschede_Overijssel_Province-Hotels.html',\
                  'https://www.tripadvisor.com/Hotels-g188613-Amersfoort-Hotels.html',\
                  'https://www.tripadvisor.com/Hotels-g227899-Noordwijk_South_Holland_Province-Hotels.html']

    #Select all urls 
    def parse(self, response):
        #items = TaScraperItem()

        #urls from review page
        urls = []
        for href in response.css('a.review_count::attr(href)').extract():
            url = response.urljoin(href)
            if url not in urls:
                urls.append(url)

                yield scrapy.Request(url, callback=self.parse_page)

        #url from next page in homepage
        next_page = response.xpath('//*[@id="taplc_main_pagination_bar_hotels_less_links_v2_0"]/div/div/div/a/@href').extract()
        if next_page:
            url = response.urljoin(next_page[-1])
            print(url)
            yield scrapy.Request(url, self.parse) #count_page

    def parse_page(self, response):

        review_page = response.css('div:nth-child(3) > div:nth-child(4) > div.WAllg._T > div.KgQgP.MC._S.b.S6.H5._a > a::attr(href)').extract()      

        if review_page:
            for i in range(len(review_page)):
                url = response.urljoin(review_page[i])
                yield scrapy.Request(url, self.parse_detail)

        next_page = response.css('a.ui_button.nav.next.primary::attr(href)').extract() #//*[@id="component_15"]/div/div[3]/div[13]/div/a/@href
        if next_page:
            url = response.urljoin(next_page[-1])
            print(next_page)
            yield scrapy.Request(url, self.parse_page)

       
    def parse_detail(self, response): 
        yield {
            'url' : response.css('head > link:nth-child(33)::attr(href)').extract(),
            'hotel_name' : response.css('.altHeadInline a::text').extract(),
            'review_title' : response.css('#HEADING::text').extract(),
            'review_text' : response.css('.fullText::text').extract(),
            'helpful_count' : response.css('#taplc_resp_sur_h_featured_review_container_0 .numHelp::text').extract(),
            'publish_date' : response.css('#taplc_resp_sur_h_featured_review_container_0 .ratingDate::text').extract(),
        }
