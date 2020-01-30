import requests
import json
import csv
import time

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36',
    'accept-language': 'zh-CN,zh;q=0.9'
}


def getyijiddanmu(timestamp):
    url = 'https://mfm.video.qq.com/danmu?otype=json&target_id=4456190387%26vid%3Di0032qxbi2v&timestamp={}&_=1580217203910'.format(
        timestamp)
    response = requests.get(url, headers=headers)
    data = json.loads(response.text, strict=False)
    print(data)
    comments = data['comments']
    all_comment = []
    for datum in comments:
        commentid = datum['commentid']  # 评论id
        content = datum['content']  # 评论内容
        upcount = datum['upcount']  # 点赞数
        opername = datum['opername']  # 用户名
        uservip_degree = datum['uservip_degree']  # 会员等级
        each_danmu = (opername, commentid, content, upcount, uservip_degree)
        all_comment.append(each_danmu)
    file_name = '《庆余年》第一集弹幕' + '.csv'
    print('正在保存时间戳（timestamp）=', timestamp, '的弹幕')
    with open(file_name, 'a', encoding='utf-8', newline='') as file:
        csv_writer = csv.writer(file)
        for i in all_comment:
            csv_writer.writerow(i)
    print('保存完毕')


for timestamp in range(15, 2716, 30):
    time.sleep(1)
    getyijiddanmu(timestamp)
