d# -*- coding: utf-8 -*
import os
import gridfs
import pymongo
import scrapy
import re
import requests
from bs4 import BeautifulSoup
from paperbot.items import PaperbotItem
from itertools import chain

control_chars = ''.join(map(chr, chain(range(0, 9), range(11, 32), range(127, 160))))
CONTROL_CHAR_RE = re.compile('[%s]' % re.escape(control_chars))

import configparser

config = configparser.ConfigParser()
config.read('./../lib/config.cnf')

import time

def print_time():
    tm = time.localtime(time.time())
    string = time.strftime('%Y-%m-%d %I:%M:%S %p', tm)
    return string


class scuba_diving_safetySpider(scrapy.Spider):
    name = 'scuba_diving_safety'
    allowed_domains = ['https://pubmed.ncbi.nlm.nih.gov/']
    start_urls = ['https://pubmed.ncbi.nlm.nih.gov/?term=Scuba%20diving%20safety&filter=simsearch1.fha&filter=years.2012-2022']

    def __init__(self):
        scrapy.Spider.__init__(self)
        self.start_urls = 'https://pubmed.ncbi.nlm.nih.gov/?term=Scuba%20diving%20safety&filter=simsearch1.fha&filter=years.2012-2022'
        self.client = pymongo.MongoClient(config['DB']['MONGO_URI'])
        self.db = self.client['attchment']
        self.fs = gridfs.GridFS(self.db)

    def start_requests(self):
        yield scrapy.Request(self.start_urls, self.parse, dont_filter=True)

    def parse(self, response):
        #total page num
        total_page_str = response.xpath('//*[@id="search-results"]/div[6]/div/label[2]/text()').get()
        last_page_no = int(total_page_str.split(" ")[1])
        page_no = 1

        while True:
            if page_no > last_page_no:
                break
            link = "https://pubmed.ncbi.nlm.nih.gov/?term=Scuba%20diving%20safety&filter=simsearch1.fha&filter=years.2012-2022&page=" + str(page_no)
            print("link:", link)
            yield scrapy.Request(link, callback=self.parse_each_pages, meta={'link': link}, dont_filter=True)
            page_no += 1
            print("page_no:", page_no)

    def parse_each_pages(self, response):
        link = response.meta['link']
        htmls = requests.get(link)
        bs = BeautifulSoup(htmls.content, 'html.parser')

        for partial_url in bs.findAll("a", "docsum-title"):
            time.sleep(1)
            url = "https://pubmed.ncbi.nlm.nih.gov" + partial_url["href"]
            print("url:", url)

            yield scrapy.Request(url, callback=self.parse_post, meta={'url': url}, dont_filter=True)

    def parse_post(self, response):
        original_url = response.meta['url']
        item = PaperbotItem()

        htmls = requests.get(original_url)
        bs = BeautifulSoup(htmls.content, 'html.parser')

        title = bs.find("h1", "heading-title").get_text()
        print("title:", title)

        writer_list = []
        for writer in bs.findAll("a", "full-name"):
            #tag객체의 존재 여부 확인 -> 특정 tag가 문서마다 존재하지 않을 수 있음
            if str(type(writer)) == "<class 'NoneType'>":
                writers = None
            else:
                writer_list.append(writer.get_text())
        writers = ', '.join(writer_list)
        print("writers", writers)

        date = bs.find("span", "cit")
        if str(type(date)) == "<class 'NoneType'>":
            date = None
        else:
            date = date.get_text().split(";")[0]
        print("date:", date)

        abstract = bs.find("div", "abstract-content selected").get_text()
        print("abstract:", abstract)

        #abstract이 없다면 의미없는 데이터이기 때문에 만약 글자 수가 20자 미만일 경우, 해당 문서는 DB에 저장X
        if len(abstract) > 20:
            item[config['VARS']['VAR1']] = title.strip()
            if writers is not None:
                item[config['VARS']['VAR3']] = writers.strip()
            if date is not None:
                item[config['VARS']['VAR4']] = date.strip()
            item[config['VARS']['VAR2']] = abstract.strip()
            item[config['VARS']['VAR6']] = "https://pubmed.ncbi.nlm.nih.gov/"
            item[config['VARS']['VAR8']] = original_url
            item[config['VARS']['VAR14']] = print_time()
            yield item