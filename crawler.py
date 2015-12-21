# -*- coding: utf-8 -*-

import urllib2
import cookielib
import re
from bs4 import BeautifulSoup


class Crawler(object):

    def __init__(self,args):
        self.url = 'http://hk-bici.com/forum-2-'
        self.depth = args.depth
        # 构建header的dict结构
        self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36'}
        self.keywords = args.keyword
        self.initiation = args.initiation

    def start(self):
        if self.initiation:
            self.cookieInit()
        for pageIndex in range(self.depth):
            results = self.search(self.getInfo(self.getPage(pageIndex+1)))
            for result in results:
                print result
                print results[result]

    def search(self, info):
        keylist = re.split('[\s\.\,+]', self.keywords)
        results = info.copy()
        for key in keylist:
            pattern = re.compile('.*?' + key + '.*?', re.S)
            for item in info:
                if (not re.match(pattern, item)) and item in results:
                    results.pop(item)
        return results

    def getInfo(self, page):
        soup = BeautifulSoup(page)
        elements = soup.find_all(name='a', attrs={'class': re.compile('xst')})
        info = {}
        for element in elements:
            info[element.string.encode('utf-8')] = element['href']
        return info

    def cookieInit(self):
        # cookie存放文件
        filename = "cookie.txt"
        # cookie文件初始化所用代码
        # 创建登录url
        loginUrl = 'http://hk-bici.com/member.php?mod=logging&action=login&loginsubmit=yes&handlekey=login&loginhash=LaijH&inajax=1'
        # formdata提交已编码的表单内容
        formdata = "formhash=c97618ca&referer=http%3A%2F%2Fhk-bici.com%2Fforum-2-2.html&loginfield=username&username=wjq5858123&password=987456&questionid=0&answer=&cookietime=2592000&loginsubmit=true"
        request = urllib2.Request(loginUrl, formdata, self.headers)
        cookie = cookielib.MozillaCookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
        # 登录并保存cookies
        opener.open(request)
        cookie.save(filename, ignore_discard=True, ignore_expires=True)

    def getPage(self, pageindex):
        # 创建MozillaCookieJar实例用以保存cookie
        cookie = cookielib.MozillaCookieJar()
        # 从文件中读取cookie
        cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
        # 创建opener对象
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
        # 安装opener方法
        urllib2.install_opener(opener)
        url = self.url + str(pageindex) + '.html'
        acrequest = urllib2.Request(url, None, self.headers)
        response = opener.open(acrequest)
        page = response.read()
        return page
