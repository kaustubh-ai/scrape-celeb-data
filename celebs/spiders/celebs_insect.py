# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import tweepy
from textblob import TextBlob
from time import sleep


class CelebsInsectSpider(scrapy.Spider):
    name = 'celebs_insect'
    allowed_domains = ['celebritynetworth.com']
    start_urls = ['http://celebritynetworth.com/list/top-50-bollywood-celebrities//']

    def parse(self, response):
        # names = response.xpath('//h2[@class="title"]/text()').extract()
        bio_urls = response.xpath('//a[@class="anchor clearfix"]/@href').extract()
        for i in bio_urls:
            yield Request(i, callback=self.parse_celebs)

    def parse_celebs(self, response):
        celeb_data = {}
        name = response.xpath('//h2[@class="title celeb_stats_table_header"]/text()').extract()[0]
        celeb_data['Name'] = name
        desc = '\n'.join(response.xpath('//div[@id="single__post_content"]/p/text()').extract())
        celeb_data['Description'] = desc

        table = response.xpath('//table[@class="celeb_stats_table"]/tr')
        for i, data in enumerate(table):
            entry = data.xpath('td//text()').extract()
            k, v = entry[0][:-1].replace(' ', '_'), entry[1]
            celeb_data[k] = v

        twitter_keys = {}
        with open('../secret.txt', 'r') as f:
            content = f.readlines()
            for i in content[1:]:
                k, v = i.split('=')[0][:-1], i.split('=')[-1].rstrip()[2:-1]
                twitter_keys[k] = v
        consumer_key = twitter_keys['consumer_key']
        consumer_secret = twitter_keys['consumer_secret']
        access_token = twitter_keys['access_token']
        access_token_secret = twitter_keys['access_token_secret']

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        l = []
        public_tweets = api.search(name, count=100)
        for tweet in public_tweets:
            analysis = TextBlob(tweet.text)
            l.append(analysis.sentiment)
        sents = [i.polarity for i in l]
        sent = round(sum(sents) / len(sents), 3)
        if sent >= 0.5:
            celeb_data['Sentiment'] = 'Positive'
        elif sent > -0.5 and sent < 0.5:
            celeb_data['Sentiment'] = 'Neutral'
        else:
            celeb_data['Sentiment'] = 'Negative'
        sleep(2)

        yield celeb_data
