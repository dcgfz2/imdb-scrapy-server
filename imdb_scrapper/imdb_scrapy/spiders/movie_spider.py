import scrapy
from imdb_scrapy.items import MovieItem

class MovieSpider(scrapy.Spider):
    name = "movie"
    start_urls = ["https://www.imdb.com/chart/top/"]

    def parse(self, response):
        urls = response.css('td[class=titleColumn] a').xpath('@href').extract()
        for entry in urls:
            yield scrapy.Request(response.urljoin(entry), callback=self.parse_movie)

    def parse_movie(self, response):
        item = MovieItem()
        item['title'] = response.css('div[class=title_wrapper]').xpath('//h1/text()').extract()[0].replace('\xa0',' ')
        item['image_url'] = response.css('div[class=poster] img::attr(src)').extract()[0]
        item['page_url'] = response.urljoin('')
        item['mpaa'] = response.css('div[class=title_wrapper]').xpath('//div[@class="subtext"]/text()').extract()[0].replace(' ','').replace('\n','')
        item['genre'] = response.css('div[class=title_wrapper]').xpath('//div[@class="subtext"]/a/text()').extract()[0]
        item['year'] = response.css('div[class=title_wrapper]').xpath('//span[@id="titleYear"]/a/text()').extract()[0]
        item['rating'] = response.css('div[class=ratingValue]').xpath('//span[@itemprop="ratingValue"]/text()').extract()[0]
        item['director'] = response.css('div[class=credit_summary_item]').xpath('a/text()').extract()[0]

        yield item
