# -*- coding: utf-8 -*-
import csv
import json
import re
import time
from copy import deepcopy
from ..items import GetvidItem
import scrapy


class VidSpider(scrapy.Spider):
    name = 'vid'
    allowed_domains = ['video.qq.com']
    start_urls = [
        'https://union.video.qq.com/fcgi-bin/data?otype=json&tid=682&appid=20001238&appkey=6c03bbe9658448a4&union_platform=1&idlist=x0032o977cc,i0032qxbi2v,j0032ubhl9s,x0032o977cc,k00329wv1ed,t00329rbass,y00326sr9vu,y0032tb125l,x00323jocrm,m0032minvpq,h0032kvzna4,w0032ao1l6o,v0032w9abwz,l00323w4dhs,p0032ylqkg4,n0032mibckr,l0033tr603q,b0033kl134e,x003341ds7b,b00335ig86b,i0033tw7pdn,h0033evbn3l,g00336gt00t,w00336u0t1b,z0033e6jyez,w0033y11w1w,c0033vaqexb,k00331cqhio,s0033qy3cr5,c00339ka821']

    def parse(self, response):

        sFileName = 'targetid_vids.csv'

        with open(sFileName, newline='', encoding='UTF-8') as csvfile:
            rows = csv.reader(csvfile)
            for row in rows:
                # print(row)
                targetid = row[0]
                vid = row[1]
                for timestamp in range(45, 2686, 30):
                    damu_url = 'https://mfm.video.qq.com/danmu?otype=json&target_id={}%26vid%3D{}&timestamp={}'.format(
                        targetid, vid, timestamp)
                    print(damu_url)
                    yield scrapy.Request(url=damu_url, callback=self.parse_danmu)

    def parse_danmu(self, response):
        item = GetvidItem()
        data = json.loads(response.text, strict=False)
        # print(type(data))
        # print(data)
        time.sleep(1)
        comments = data['comments']
        print(comments)
        all_comments = []
        for datum in comments:
            # commentid = datum['commentid']  # 评论id
            item['content'] = datum['content']  # 评论内容
            item['upcount'] = datum['upcount']  # 点赞数
            item['opername'] = datum['opername']  # 用户名
            item['uservip_degree'] = datum['uservip_degree']  # 会员等级
            yield item

        #     each_danmu = [content, upcount, uservip_degree, opername]
        #     all_comments.append(each_danmu)
        # print(all_comments)
        # file_name = '《庆余年》弹幕test' + '.csv'
        # with open(file_name, 'a', encoding='utf-8', newline='') as file:
        #     csv_writer = csv.writer(file)
        #     for all_comment in all_comments:
        #         csv_writer.writerow(all_comment)
        # print('保存完毕')
