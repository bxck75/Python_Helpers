from icrawler.builtin import BaiduImageCrawler, BingImageCrawler, GoogleImageCrawler

class ICrawl():
    def __init__(self, keyword='abc', max_qty=10, out_dir='icrawl_loot_images', min_wh=(200,200), max_wh=(800,800)):
        
        self.out_dir = out_dir
        self.keyword = keyword
        self.max_qty = max_qty
        self.min_wh = min_wh
        self.max_wh = max_wh
        path = '/content/crawled'.split('/')[len('/content/crawled'.split('/'))-1]
        print(path)
        self.google_crawler = GoogleImageCrawler(feeder_threads=1,parser_threads=1,downloader_threads=4, storage={})
        
        self.filters = dict(size='large', color='orange', license='commercial,modify', date=((2019, 1, 1), (2019, 6, 30)))
        
        def run(self):
            self.google_crawler.crawl(keyword=self.keyword, filters=self.filters, offset=0, max_num=self.max_qty,
                                        min_size=self.min_wh, max_size=self.max_wh, file_idx_offset=0)

        
        
        
        
#         bing_crawler = BingImageCrawler(downloader_threads=4,
#                                         storage={'root_dir': 'your_image_dir'})
#         bing_crawler.crawl(keyword='cat', filters=None, offset=0, max_num=1000)

#         baidu_crawler = BaiduImageCrawler(storage={'root_dir': 'your_image_dir'})
#         baidu_crawler.crawl(keyword='cat', offset=0, max_num=1000,
#                             min_size=(200,200), max_size=None)
