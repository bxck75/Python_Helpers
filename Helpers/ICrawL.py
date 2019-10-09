from icrawler.builtin import BaiduImageCrawler, BingImageCrawler, GoogleImageCrawler

def ICL(key='face', qty=100, out_dir='/content/images'):
    '''ICL(key='face', qty=100, out_dir='/content/images')'''  
    google_crawler = GoogleImageCrawler(
        feeder_threads=1,
        parser_threads=1,
        downloader_threads=4,
        storage={'root_dir': out_dir })
 
    filters = dict(
        size='medium',
        # color='orange',
        # license='commercial,modify',
        # date=((2017, 1, 1), (2017, 11, 30)),
        )    
    google_crawler.crawl(
        keyword=key, 
        filters=filters, 
        offset=0, 
        max_num=qty,
        min_size=(400,400), 
        max_size=None, 
        file_idx_offset=0,
        )
    bing_crawler = BingImageCrawler(
        downloader_threads=4,
        storage={'root_dir': out_dir }
        )
    bing_crawler.crawl(
        keyword=key, 
        filters=None, 
        offset=0, 
        max_num=qty
        )
    baidu_crawler = BaiduImageCrawler(
        storage={'root_dir': out_dir }
        )
    baidu_crawler.crawl(
        keyword=key, 
        offset=0, 
        max_num=qty,
        min_size=(200,200), 
        max_size=None
        )
