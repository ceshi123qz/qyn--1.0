# coding:utf-8
import csv
import random
import time
import requests
import json
import re

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36',
    'accept-language': 'zh-CN,zh;q=0.9',
    'referer': 'https://v.qq.com/x/cover/rjae621myqca41h/k00329wv1ed.html'
    # 'cookie': 'pgv_pvi=9774653440; RK=U+w8AUnwR7; ptcz=6cfd7f0934fe95f35af29cba8a911e4c5604d4d71d9df8f3980d008b743fc14d; tvfe_boss_uuid=192cd4fb4717477f; pgv_pvid=6986441214; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216685f5e1466d0-08ba11b0c1af94-8383268-2073600-16685f5e14715d%22%2C%22%24device_id%22%3A%2216685f5e1466d0-08ba11b0c1af94-8383268-2073600-16685f5e14715d%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.google.com.hk%2F%22%2C%22%24latest_referrer_host%22%3A%22www.google.com.hk%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%7D; pac_uid=1_1349852254; video_platform=2; video_guid=6e65802e77ab56d3; _video_qq_login_time_init=1580216418; main_login=qq; vqq_access_token=3F0714B100781024543597C006510EBE; vqq_appid=101483052; vqq_openid=0B672D2E9D37CD166295CEE0B0F270F0; vqq_vuserid=164622562; vqq_refresh_token=7E493C7D31F45E20D4FCB7E8FEF24510; vqq_vusession=rAIV8QtaxGCsobVz41Nm3w..; uid=178632541; pgv_info=ssid=s1180562430; vqq_next_refresh_time=5237; vqq_login_time_init=1580354432; login_time_last=2020-1-30 11:20:32'
}

# 读取targetid_vids.csv中的target_id和vid
reader = csv.reader(open('targetid_vids.csv'))
number_of_episode = 40  # 根据报错实时调整
for lis in reader:
    target_id = lis[0]
    vid = lis[1]
    number_of_episode += 1
    print(target_id, vid)
    # 尝试使用代理
    # proxies_list = []
    #
    # proxy = random.choice(proxies_list)
    # proxies = {'https': proxy}
    # print(proxies)
    for timestamp in range(45, 2686, 30):
        damu_url = 'https://mfm.video.qq.com/danmu?otype=json&target_id={}%26vid%3D{}&timestamp={}'.format(
            target_id, vid, timestamp)
        print(damu_url)

        response = requests.get(url=damu_url, headers=headers)
        data = json.loads(response.text, strict=False)
        # print(type(data))
        print(data)
        time.sleep(1)

        comments = data['comments']
        print(comments)
        all_comments = []
        for datum in comments:
            # commentid = datum['commentid']  # 评论id
            content = datum['content']  # 评论内容
            upcount = datum['upcount']  # 点赞数
            opername = datum['opername']  # 用户名
            uservip_degree = datum['uservip_degree']  # 会员等级
            each_danmu = [content, upcount, uservip_degree, opername]
            all_comments.append(each_danmu)
        print(all_comments)
        file_name = '《庆余年》弹幕test' + '.csv'
        print('正在保存第', number_of_episode, '集弹幕')
        with open(file_name, 'a', encoding='utf-8', newline='') as file:
            csv_writer = csv.writer(file)
            for all_comment in all_comments:
                csv_writer.writerow(all_comment)
        print('保存完毕')
