#!/usr/bin/python2
# -*- coding:utf8 -*-
                  
import urllib
import urllib2
import re
import os
import time
import socket
import thread
import threading
def get_html(url):
    socket.setdefaulttimeout(5)
    papg = urllib.urlopen(url)
    html = papg.read()
    print(html)      
    html = unicode(html,"utf8").encode("utf8")
    return html

def get_page_name(html):
    imgre1 = re.compile(r'"bdDesc":"(\S+)","bdMini"')
    imgl2 = re.findall(imgre1, html)
    return imgl2[0]
def get_tag_list(html):
    szurlre = re.compile(r'<a href="(http://www.5442.com/tag/.*?.html)" class')
    tag_list = re.findall(szurlre, html)
    return tag_list

def get_page_num(html):
    szurlre = re.compile(r'(\d+).html\'>末页')
    szresult = re.findall(szurlre, html)
    if len(szresult) == 0:
        page_num = 0
    else:
        page_num = int(szresult[0])
#    print page_num
    return page_num

def get_page_num2(html):
    szurlre = re.compile(r'<a href="index_\S+">(\d+)</a>')
    szresult = re.findall(szurlre, html)
    if len(szresult) == 0:
        page_num = 0
    else:
        page_num = int(szresult.pop())
   # print page_num
    return page_num

#获得单页的相册
def get_ablum_list(html):
    szurlre = re.compile(r'<li class="pure-u-1-2 pure-u-lg-1-4"><a href="(\S+)" title=')
    ablum_list = re.findall(szurlre, html);
    return ablum_list
#获得相册的名称
def get_ablum_name(html):
    szurlre = re.compile(r'<title>(\S+)</title>')
    ablum_name = re.findall(szurlre, html)
    return ablum_name[0]
#获得图片地址
def get_photo_url(html):
    imgre = re.compile(r'<img src="(\S+)"')
    imgl1 = re.findall(imgre, html)
    return iur_l
#获得单页的图片
def get_photo2(i_url, dir, photo_num):
    if photo_num!=1:
        i_url=i_url+'index_%s.html'%(photo_num-1)
    print(i_url)
    return 0;
    header0={"User-Agent":"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1"}
    header1={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0"}
    header2={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) likeGecko"}
    header3={"User-Agent": "NOKIA5700/ UCWEB7.0.2.37/28/999"}
    header4={"User-Agent":"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E) "}
    header5={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1"}
    header6={"User-Agent":"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E) "}
    header7={"User-Agent":"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0"}
    header8={"User-Agent":"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0) "}
    User_Agent_headers_list=[header0,header1,header2,header3,header4,header5,header6,header7,header8]
    i=0
    while i<=8:
        try:
            headers=User_Agent_headers_list[i]
            req=urllib2.Request(imgurl,headers=headers)
            resp = urllib2.urlopen(req,data=None,timeout=17)
            data = resp.read()
            fp = open('/home/sunbei/Desktop/photo/东京食尸鬼/%s/%s.jpg'%(dir,photo_num), "wb")
            fp.write(data)
            fp.close
            print('成功:%s'%photo_num)
            i=9
        except:
            i=i+1
            if i==9:
               print("失败:%s"%imgurl)
               try:
                   fp =open('/home/sunbei/Desktop/photo/东京食尸鬼/error.txt', "a")
               except:
                   fp =open('/home/sunbei/Desktop/photo/东京食尸鬼/error.txt', "w")
               fp.write(imgurl)
               fp.close
                 
def thread_download(i_url, ablum_name, photo_page_num):
    for i in range(1, photo_page_num):
     #     print i 
           get_photo2(i_url, ablum_name, i)
          
def thread1(ablum_url):
    ablum_url = "http://www.fzdm.com/manhua/117/%s"%ablum_url
    print ("网址:%s"%ablum_url)
    try:
        photo_html = get_html(ablum_url)
            # print("d")
    except:
           return 0  
    # print("r")
    photo_page_num = get_page_num2(photo_html)
    print("页数:%s"%photo_page_num)
    ablum_name = get_page_name(photo_html)
    # print photo_page_num
    photo_num = 1
    #创建相册对应的目录
    ui_ablum_name = ablum_name
    try:
         os.mkdir("/home/sunbei/Desktop/photo/东京食尸鬼/"+ui_ablum_name)
    except:
         print "目录已经存在"
    thread.start_new_thread(thread_download,(ablum_url, ablum_name,photo_page_num))  
     
#url = "http://www.fzdm.com/manhua/117/"
url='http://www.fzdm.com/manhua/117/RE80/index_1.html'
baseurl = "http://www.fzdm.com/manhua/"
html = get_html(url)
print(html)
print ("一共有页")
page_num = get_page_num(html)
print ("一共有%s页"%page_num)
print ("一共有%s页"%page_num)
print ("一共有%s页"%page_num)
try:
    os.mkdir("/home/sunbei/Desktop/photo/东京食尸鬼")
except:
    print "目录已经存在"
ablum_list = get_ablum_list(html)
for ablum_url in ablum_list:
    thread1(ablum_url)


