# 1593572846

import scrapy
import time
import scrapy.crawler as crawler
from multiprocessing import Process, Queue
from scrapy.crawler import CrawlerProcess
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor


def main():
    # target_board = ['Gossiping', 'Stock']
    target_board = 'Gossiping'
    runner = CrawlerRunner(get_project_settings())
    d = runner.crawl('PTTCrawler', target_board)
    d.addBoth(lambda _: reactor.stop())
    reactor.run()

    # time.sleep(1)


if __name__ == '__main__':
    main()
