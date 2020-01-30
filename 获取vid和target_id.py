# coding:utf-8
import requests
import json
import re
import csv

url = [
    'https://union.video.qq.com/fcgi-bin/data?otype=json&tid=682&appid=20001238&appkey=6c03bbe9658448a4&union_platform=1&idlist=x0032o977cc,i0032qxbi2v,j0032ubhl9s,x0032o977cc,k00329wv1ed,t00329rbass,y00326sr9vu,y0032tb125l,x00323jocrm,m0032minvpq,h0032kvzna4,w0032ao1l6o,v0032w9abwz,l00323w4dhs,p0032ylqkg4,n0032mibckr,l0033tr603q,b0033kl134e,x003341ds7b,b00335ig86b,i0033tw7pdn,h0033evbn3l,g00336gt00t,w00336u0t1b,z0033e6jyez,w0033y11w1w,c0033vaqexb,k00331cqhio,s0033qy3cr5,c00339ka821'
    '',
    'https://union.video.qq.com/fcgi-bin/data?otype=json&tid=682&appid=20001238&appkey=6c03bbe9658448a4&union_platform=1&idlist=z00335p6vbp,k00334tnhys,u003383gn30,i0033o58mal,o0033cp869i,u0033m2j2uk,i0033dpqxcu,l0033n4arkh,j0033p7curk,v0033usud3k,e003358h201,b0033pcu7u1,l0033cu565q,a0033nbp009,t0033bfj2ht,e0033n97pay,c0033527yjb,t3054h9jkl3,w3053ouwlpy,h3053f72u0y,s30523vftij,i0033gz8p9t,n3048igrpe6,v3050zpwq5h,y3050wytfl5,k0033n47eyr,c0033hnuq1s,m3048ixy6bg,b30491zujdj,x30476hcxfu'
]

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'
}
episode_info = []
# v_ids = []

targetid_vids = []

for i in url:
    res = requests.get(url=i, headers=headers)
    res.encoding = res.apparent_encoding

    wenben = res.text
    wen = wenben.replace('QZOutputJson=', '')
    a = wen[-1]
    b = wen.replace(a, '')
    c = b.replace('null', "''")
    result = eval(c)
    # print(result)
    # print(type(result))

    for each_episode in result['results']:
        v_id = each_episode['id']
        # print(v_id)
        episode_name = each_episode['fields']['title']
        # print(episode_name,v_id)
        view_count = each_episode['fields']['view_all_count']
        episode = [episode_name, v_id, view_count]
        episode_info.append(episode)
        # v_ids.append(v_id)

exact_episode_info = episode_info[1:47]
for each_exact_episode_info in exact_episode_info:
    vid = each_exact_episode_info[1]
    # print(vid)
    target_id_url = 'https://access.video.qq.com/danmu_manage/regist?vappid=97767206&vsecret=c0bdcbae120669fff425d0ef853674614aa659c605a613a4&raw=1'

    data = {"wRegistType": 2,
            "vecIdList": [vid],
            "wSpeSource": 0,
            "bIsGetUserCfg": 1,
            "mapExtData": {vid: {
                "strCid": "rjae621myqca41h",
                "strLid": ""
            }
            }
            }

    response = requests.post(url=target_id_url, headers=headers, data=json.dumps(data))

    # print(data)
    # print(response.text)
    text = response.text
    targetid = re.findall("&targetid=(.*?)&vid", text)  # target_id
    target_id = targetid[0]  # target_id
    targetid_vid = [target_id,vid]
    targetid_vids.append(targetid_vid)
    print(target_id, vid)
print(targetid_vids)
file_name = 'targetid_vids' + '.csv'


with open(file_name, 'a', encoding='utf-8', newline='') as file:
    csv_writer = csv.writer(file)
    for all_comment in targetid_vids:
        csv_writer.writerow(all_comment)
print('保存完毕')