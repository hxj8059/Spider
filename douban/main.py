import sys
from bs4 import BeautifulSoup
import re
import urllib.request
import xlwt
import sqlite3


def main():
    baseurl = "https://movie.douban.com/top250?start="
    # 1.爬取
    datalist = get_data(baseurl)
    savepath = ".\\movie250.db"
    insert_db(savepath, datalist)


findLink = re.compile(r'<a href="(.*?)">')
findImgSrc = re.compile(r'<img.*src="(.*?)"', re.S)
findTitle = re.compile(r'<span class="title">(.*?)</span>')
findRate = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
findComment = re.compile(r'<span>(\d*)人评价</span>')
findInq = re.compile(r'<span class="inq">(.*?)</span>')


def get_data(baseurl):
    datalist = []
    for i in range(10):
        url = baseurl + str(i*25)
        html = ask_url(url)
        # resolve
        soup = BeautifulSoup(html, "html.parser")
        # find matched string
        for item in soup.find_all("div", class_="item"):
            data = []      # information of one movie
            item = str(item)
            link = re.findall(findLink, item)
            print(link)
            data.append(link[0])
            img = re.findall(findImgSrc, item)
            data.append(img[0])
            print(img)
            title = re.findall(findTitle, item)
            data.append(title[0])
            if len(title) < 2:
                data.append("")
            else:
                data.append(title[1].replace('\xa0/\xa0', ''))
            rate = re.findall(findRate, item)
            data.append(rate[0])
            print(rate)
            comment = re.findall(findComment, item)
            data.append(comment[0])
            print(comment)
            inq = re.findall(findInq, item)
            if len(inq) != 0:
                data.append(inq[0])
            else:
                data.append("")
            print(inq)
            datalist.append(data)

    return datalist


def ask_url(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 Edg/91.0.864.54"
    }
    req = urllib.request.Request(url, headers=head, method="GET")
    html = ""
    try:
        response = urllib.request.urlopen(req)
        html = response.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


def save_data(save_path, datalist):
    print("saving")
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)
    sheet = book.add_sheet('douban250', cell_overwrite_ok=True)
    col = ("detail_link", 'img', 'name_cn', 'name_foreign', 'rate', 'comment', 'sentence')
    for i in range(0, 7):
        sheet.write(0, i, col[i])
    for i in range(0, 7):
        for j in range(0, len(datalist)):
            sheet.write(j+1, i, datalist[j][i])

    book.save(save_path)


def init_db(dbpath):
    sql = '''
        CREATE TABLE movie250
        (
        id integer primary key autoincrement,
        info_link text,
        img_link text,
        name_cn varchar,
        name_for varchar,
        rate numeric,
        comment numeric,
        inq text
        )
    '''
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()


def insert_db(dbpath, datalist):
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    sql = ""
    for data in datalist:
        for index in range(len(data)):
            if index == 4 or index == 5:
                continue
            else:
                data[index] = '"' + data[index] + '"'

        sql = '''
            INSERT INTO movie250 (
            info_link, img_link, name_cn, name_for, rate, comment, inq)
            values(%s);'''%",".join(data)
        print(sql)
        cursor.execute(sql)
        conn.commit()
    cursor.close()
    conn.close()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    init_db(".\\movie250.db")
    main()
