#! python3
# coding:utf-8

import re
import requests
import json
import urllib.request
import urllib.error
import os
import sys

minimumsize = 10    # 文件的最小尺寸
print("fetching msg from %s \n" % sys.argv[1])  # 解释操作，输出你的待爬取地址
url = re.sub("#/", "", sys.argv[1]) # substitute, 消除"#/"得到新的url
r = requests.get(url)   # python开始读取url，内容全部放入r
contents = r.text   # 以 r 中的 text 内容赋予 contents
res = r'<ul class="f-hide">(.*?)</ul>'  # todo
mm = re.findall(res, contents, re.S | re.M) # todo
CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))  # todo

if(mm):
    contents = mm[0]
else:
    print('Can not fetch information form URL. Please make sure the URL is right.\n')
    os._exit(0)

res = r'<li><a .*?>(.*?)</a></li>'  # html 语言的 list 格式，用于 todo
mm = re.findall(res, contents, re.S | re.M) # 查找 todo

for value in mm:
    url = 'http://sug.music.baidu.com/info/suggestion'
    payload = {'word': value, 'version': '2', 'from': '0'}
    print(value)

    r = requests.get(url, params=payload)
    contents = r.text
    d = json.loads(contents, encoding="utf-8")
    if d is not None and 'data' not in d:
        continue
    songid = d["data"]["song"][0]["songid"]
    print("find songid: %s" % songid)

    url = "http://music.baidu.com/data/music/fmlink"
    payload = {'songIds': songid, 'type': 'flac'}
    r = requests.get(url, params=payload)
    contents = r.text
    d = json.loads(contents, encoding="utf-8")
    if('data' not in d) or d['data'] == '':
        continue
    songlink = d["data"]["songList"][0]["songLink"]
    print("find songlink: ")
    if(len(songlink) < 10):
        print("\tdo not have flac\n")
        continue
    print(songlink)

    songdir = "songs_dir"
    if not os.path.exists(songdir):
        os.makedirs(songdir)

    songname = d["data"]["songList"][0]["songName"]
    artistName = d["data"]["songList"][0]["artistName"]
    filename = ("%s/%s/%s-%s.flac" %
                (CURRENT_PATH, songdir, songname, artistName))

    f = urllib.request.urlopen(songlink)
    headers = requests.head(songlink).headers
    size = round(int(headers['Content-Length']) / (1024 ** 2), 2)
    #Download unfinished Flacs again.
    if not os.path.isfile(filename) or os.path.getsize(filename) < minimumsize: #Delete useless flacs
        print("%s is downloading now ......\n\n" % songname)
        if size >= minimumsize:
            with open(filename, "wb") as code:
                code.write(f.read())
        else:
            print("the size of %s (%r Mb) is less than 10 Mb, skipping" %
                  (filename, size))
    else:
        print("%s is already downloaded. Finding next song...\n\n" % songname)


print("\n================================================================\n")
print("Download finish!\nSongs' directory is %s/songs_dir" % os.getcwd())
