# -*- coding: utf-8 -*-
from scrapy import Spider, Request
from wallhaven.items import WallhavenItem

class LatestSpider(Spider):
    name = 'latest'
    allowed_domains = ['alpha.wallhaven.cc']
    start_urls = ['https://alpha.wallhaven.cc/latest']


    def parse(self, response):
        base_url = 'https://alpha.wallhaven.cc/latest'
        page_info = response.xpath('//div[@id="thumbs"]//section[@class="thumb-listing-page"]//h2/text()').extract()[1]
        total_page = int(page_info.split('/')[1].strip())   #总页数
        # print('#total_page: ', total_page)

        query_str = '?page='

        '''
        爬取所有最新发布图页面
        '''
        for page in range(1, 1 + 1):
            url = base_url + query_str + str(page)
            # print('--- --- page:', page)
            yield Request(url, self.parse)

        '''
        爬取单页所有图链接
        '''
        page_img_links = response.xpath('//div[@id="thumbs"]//ul//li/figure/a[1]/@href').extract()
        # print('------ all links:', page_img_links)
        for img_link in page_img_links:
            yield Request(img_link, self.parse_single)

    '''
    单页图数据
    '''
    def parse_single(self, response):
        url = 'https:' + response.xpath('//main[@id="main"]//img[@id="wallpaper"]/@src').extract_first()
        title = response.xpath('//main[@id="main"]//img[@id="wallpaper"]/@alt').extract_first()
        data_id = response.xpath('//main[@id="main"]//img[@id="wallpaper"]/@data-wallpaper-id').extract_first()
        img_w = response.xpath('//main[@id="main"]//img[@id="wallpaper"]/@data-wallpaper-width').extract_first()
        img_h = response.xpath('//main[@id="main"]//img[@id="wallpaper"]/@data-wallpaper-height').extract_first()
        print('&_& url:', url)
        item = WallhavenItem()
        item['url'] = url
        item['title'] = title
        item['data_id'] = data_id
        item['img_w'] = img_w
        item['img_h'] = img_h
        print('--- --- item:', item)
        yield item

