#! python3
# coding:utf-8

import re
import requests
import json
import urllib.request
import urllib.error
import os
import sys

minimumsize = 10  # 文件的最小尺寸
print("fetching msg from %s \n" % sys.argv[1])  # 获取命令行输入的第1项，第0项是py文件名
url = re.sub("#/", "", sys.argv[1])  # substitute, 消除"#/"
r = requests.get(url)  # 获取 url
contents = r.text   # 字符串格式的内容
res = r'<ul class="f-hide">(.*?)</ul>'  # 非贪婪匹配，无序的链接列表
# 在 contents 中搜索形似 res 的内容
# S - Space, M - Multi-line
# Dot Matches All | Multi-line
mm = re.findall(res, contents, re.S | re.M)
CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))  # 存储路径的 slash 是和转义的 \ 同向的
# print(__file__)   F:/exercises/NeteaseCloudMusicFlac/py3_main.py
# print(os.path.realpath(__file__)) F:\exercises\NeteaseCloudMusicFlac\py3_main.py
# print(CURRENT_PATH)   F:\exercises\NeteaseCloudMusicFlac

if(mm):
    contents = mm[0]  # findall 生成的 mm 数据类型是 list
else:
    print('Can not fetch information form URL. Please make sure the URL is right.\n')
    # todo
    os._exit(0)

res = r'<li><a .*?>(.*?)</a></li>'  # 有序的歌名列表
mm = re.findall(res, contents, re.S | re.M)  # 获取 mm 歌名 list

for value in mm:
    url = 'http://sug.music.baidu.com/info/suggestion'
    payload = {'word': value, 'version': '2', 'from': '0'}
    print(value)  # 歌名

    r = requests.get(url, params=payload)  # 获取 url， 同时赋予 params
    # print(r.url) -> http://sug.music.baidu.com/info/suggestion?word=value&version=2&from=0
    contents = r.text
    d = json.loads(contents, encoding="utf-8")  # 以 JSON 格式装载 contents
    if d is not None and 'data' not in d:  # url 里有东西，但是没有 data 时跳过
        print('No data. Skipping...\n')
        continue
    songid = d["data"]["song"][0]["songid"]  # 由于 "song" 的值是个列表，所以需要加个[0]，再指向 "songid"
    print("find songid: %s" % songid)  #   打印百度音乐上的 song id

    # 抽出 song link
    url = "http://music.baidu.com/data/music/fmlink"
    payload = {'songIds': songid, 'type': 'flac'}
    r = requests.get(url, params=payload)
    contents = r.text
    d = json.loads(contents, encoding="utf-8")
    if('data' not in d) or d['data'] == '':
        print('No data. Skipping...\n')
        continue
    songlink = d["data"]["songList"][0]["songLink"]
    print("find songlink: ")
    if(len(songlink) < 10):
        print("No flac for " + value + "\n")
        continue
    print(songlink)

    # 生成歌曲存放目录
    songdir = "songs_dir"
    if not os.path.exists(songdir):
        os.makedirs(songdir)

    # 生成文件地址
    songname = d["data"]["songList"][0]["songName"]
    artistName = d["data"]["songList"][0]["artistName"]
    filename = ("%s/%s/%s-%s.flac" %
                (CURRENT_PATH, songdir, songname, artistName))

    f = urllib.request.urlopen(songlink)
    headers = requests.head(songlink).headers
    size = round(int(headers['Content-Length']) / (1024 ** 2), 2)  # B -> KB -> MB, round - 四舍五入（2 位小数）
    # 开始写入文件
    if not os.path.isfile(filename) or os.path.getsize(filename) < minimumsize:  # Delete useless flacs
        print("%s is downloading now ......\n" % songname)
        if size >= minimumsize:
            with open(filename, "wb") as code:  # 写入歌曲文件
                code.write(f.read())  # 读取 f 全部内容，然后写入 code
        else:
            print("The size of %s (%r Mb) is less than 10 Mb, skipping...\n" %
                  (filename, size))
    else:
        print("%s is already downloaded. Finding next song...\n" % songname)


print("================================================================\n")
print("Download finish!\nSongs' directory is %s\\songs_dir" % os.getcwd())
