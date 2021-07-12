# -*- encoding: utf-8 -*-
from fake_useragent import UserAgent
import time
import numpy as np
import requests
import json
import csv
import io



# 保存评论数据
def commentSave(list_comment):
    file = io.open('data/kxz.csv', 'a+', encoding="utf-8", newline='')
    writer = csv.writer(file)
    writer.writerow(['用户ID','评论内容','购买时间','点赞数','回复数','得分','评价时间','型号'])
    for i in range(len(list_comment)):
        writer.writerow(list_comment[i])
    file.close()
    print('存入成功')


def getCommentData(format_url,proc,i,maxPage):

    sig_comment = []
    global list_comment
    # sku时为-1
    # product时为0
    cur_page = -1
    while cur_page < maxPage:
        cur_page += 1
        # url = 'https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv%s&score=%s&sortType=5&page=%s&pageSize=10&isShadowSku=0&fold=1'%(proc,i,cur_page)
        url = format_url.format(proc,i,cur_page) # 给字符串添上参数
        try:
            response = requests.get(url=url, headers=headers)
            time.sleep(np.random.rand()*2)
            jsonData = response.text
            startLoc = jsonData.find('{')
            jsonData = jsonData[startLoc:-2]
            jsonData = json.loads(jsonData)
            print(jsonData['comments'])
            pageLen = len(jsonData['comments'])
            print(pageLen)
            print("当前第%s页"%cur_page)
            for j in range(0, pageLen):
                userId = jsonData['comments'][j]['id']#用户ID
                content = jsonData['comments'][j]['content']#评论内容
                boughtTime = jsonData['comments'][j]['referenceTime']#购买时间
                voteCount = jsonData['comments'][j]['usefulVoteCount']#点赞数
                replyCount = jsonData['comments'][j]['replyCount']#回复数目
                starStep = jsonData['comments'][j]['score']#得分
                creationTime = jsonData['comments'][j]['creationTime']#评价时间
                referenceName = jsonData['comments'][j]['referenceName']#型号
                print(referenceName)
                sig_comment.append(userId)
                sig_comment.append(content)
                sig_comment.append(boughtTime)
                sig_comment.append(voteCount)
                sig_comment.append(replyCount)
                sig_comment.append(starStep)
                sig_comment.append(creationTime)
                sig_comment.append(referenceName)
                list_comment.append(sig_comment)
                sig_comment = []
        except:
            print('网络故障或者是网页出现了问题，300秒后重新连接')
            time.sleep(300)
            cur_page -= 1
            print("endwith:", proc)

if __name__ == "__main__":
    global list_comment
    ua = UserAgent()
    # sorttype6: 按时间排序
    # sorttype5: 默认排序
    # productPageComments 该页面所有商品评论
    # skuproductPageComments 只看该商品评论
    format_url = 'https://club.jd.com/comment/skuProductPageComments.action?callback=fetchJSON_comment98&{0}&score={1}&sortType=6&page={2}&pageSize=10&isShadowSku=0&fold=1'

    headers = {
    'Accept': '*/*',
    "User-Agent": 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36',
    "cookie": "shshshfpa=7f0f33e5-29c2-5743-cbef-cd29ea1c6c4e-1612804607; shshshfpb=mseL6VYdvZi7a1kZJk8JkSQ==; pinId=XUm9rEIO2Xo; pin=hxj8059; _tp=Mr5DeTjtTQ6RkhBWJ1noDQ==; _pst=hxj8059; cn=12; __jdu=16128046088392055531017; areaId=2; ipLoc-djd=2-2830-51803-0; PCSYCityID=CN_310000_310100_310115; jwotest_product=99; unpl=V2_ZzNtbRdfF0ciW0FVLEpUAmIGEVQSVhMRJ1tCViseDwBhBRsNclRCFnUUR1JnGFgUZwUZXEJcRx1FCEdkexhdB2UGEFpKV3MlRQtGZHopXAJnABtcR1BCHHwKTld6HVgBZQMTXURncxV9DHZUehhdBmcEE1REUUolPlMaCCgpWQRmAhBaS1ZLFkUJdlZ6GF4DZgYUX0JnFXt1CUdVehFfDWMBX11FV0AcdA1BVXIQXg1kAhZZRlVDFHUOdlVLGg==; __jdv=122270672|s.manmanbuy.com|t_1003343691_|tuiguang|d9ecfb60fb964428a0a5cb53a6b4778a|1625475717013; shshshfp=d662c0d5a31aae330ae7fb87cb82d7e1; JSESSIONID=63BDAA5A77F7B9E88B9BEDC4571CC446.s1; __jda=122270672.16128046088392055531017.1612804609.1625542788.1625619825.80; __jdc=122270672; wlfstk_smdl=pow0tpdfmdb91u7oa43grsxqs4iwsjyh; TrackID=1IwTtXdFV3JSpHMRWfvhQq2BuAOi0XLo2nbHS0Oa2DxqHABiFznqZh3OcAu3e1QGPdeXZcqg7hzapQWFdA-nji58DDjDECnAoo6XLFJBB-DpVrbsJJuunpLkgNzc4Npuj; thor=12C0B0AC1844F034C55C56862C4FBC9D9276C64F8AF5D0688C8810BD76E8B198982651D43B4502D828260E2168746D1D2C03132F7508BFE8116C806C31746FB2F8938A1F65519143CCFDAECDAB4932477E49610F57774A93A3A6218DFD609537FBF589E6C85A017DA6505717D22CA7CA459FA52F8F666E1DCEE792AC5B18D3812C55E985027FCD4287C807FF1C87CE77; ceshi3.com=203; 3AB9D23F7A4B3C9B=NT2EB5I5KBNFADHDLNNJ2BKYZOLOTBG3AORIEPRLNVIP67IMHL7K7YMRJ36EDAPYGOQO52MK3N5QYSHOO3FWINPGDI; __jdb=122270672.64.16128046088392055531017|80.1625619825; shshshsID=1054474ee684ae1c1e93ef3223fb0540_52_1625624992421",
    }

    # 对应的产品id参数
    shitou_list = []
    with open('kxzindexlist.csv', encoding='utf-8') as st:
        reader = csv.reader(st)
        for row in reader:
            p_id = 'productId=' + row[0]
            shitou_list.append(p_id)
    productid = shitou_list
    list_comment = [[]]
    sig_comment = []
    for proc in productid:#遍历产品列表
        print(proc)
        i = 0
        url = format_url.format(proc,0,0)
        print(url)
        try:
            response = requests.get(url=url, headers=headers)
            jsonData = response.text
            startLoc = jsonData.find('{')
            jsonData = jsonData[startLoc:-2]
            jsonData = json.loads(jsonData)
            print("最大页数%s"%jsonData['maxPage'])
            getCommentData(format_url,proc,i,jsonData['maxPage'])#遍历每一页
        except Exception as e:
            # i -= 1
            print("the error is ",e)
            print("wating 300s---")
            time.sleep(300)
            #commentSave(list_comment)
    print("爬取结束，开始存储-------")
    commentSave(list_comment)

