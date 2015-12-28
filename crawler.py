# -*- coding: utf-8 -*-

import urllib2
import cookielib
import re
from bs4 import BeautifulSoup

import threadManager


class Crawler(object):
    '''
    This class defines the crawler's task methods.
    '''

    def __init__(self, args):
        self.url = 'http://hk-bici.com/forum-2-'
        self.depth = args.depth
        # Provide 'User-Agent' to simulate Http request from users
        self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36'}
        self.keywords = args.keyword
        self.initiation = args.initiation
        # This instance of ThreadManager specified results handling function
        self.threadManager = threadManager.ThreadManager(args.threadNum, self.searchInfo)

    def entry(self):
        '''
        This method implements the crawler's function with arguments
        passed from command line options.
        '''

        if self.initiation:
            self.cookieInit()
        self.threadManager.startThread()
        for pageIndex in range(self.depth):
            self.threadManager.putTask(self.getPage, pageIndex+1)
        self.threadManager.blockThread()

    def searchInfo(self, page):
        '''
        This method handles results passed from getPage() function
        '''

        soup = BeautifulSoup(page)
        elements = soup.find_all(name='a', attrs={'class': re.compile('xst')})
        info = {}
        for element in elements:
            info[element.string.encode('utf-8')] = element['href']
        keylist = re.split('[\s\.\,+]', self.keywords)
        results = info.copy()
        for key in keylist:
            pattern = re.compile('.*?' + key + '.*?', re.S)
            for item in info:
                if (not re.match(pattern, item)) and item in results:
                    results.pop(item)
        for result in results:
            print result
            print results[result]
        return False

    def cookieInit(self):
        '''
        This method saves cookie information in a file which would be
        used later to pass the website's verification.
        '''

        # Name the cookie file in home directory
        filename = "cookie.txt"
        # The url for login simulating
        loginUrl = 'http://hk-bici.com/member.php?mod=logging&action=login&loginsubmit=yes&handlekey=login&loginhash=LaijH&inajax=1'
        # Form data encoded for login simulating
        formdata = "formhash=c97618ca&referer=http%3A%2F%2Fhk-bici.com%2Fforum-2-2.html&loginfield=username&username=wjq5858123&password=987456&questionid=0&answer=&cookietime=2592000&loginsubmit=true"
        request = urllib2.Request(loginUrl, formdata, self.headers)
        # An instance of MozillaCookieJar
        cookie = cookielib.MozillaCookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
        # Login the website and save the cookies information
        opener.open(request)
        cookie.save(filename, ignore_discard=True, ignore_expires=True)

    def getPage(self, pageindex):
        '''
        This method visits urls which contains information required and
        returns html page as a string.
        '''

        cookie = cookielib.MozillaCookieJar()
        # Load cookie information from the cookie file
        cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
        urllib2.install_opener(opener)
        # Create url which needs to be visited
        url = self.url + str(pageindex) + '.html'
        acrequest = urllib2.Request(url, None, self.headers)
        response = opener.open(acrequest)
        page = response.read()
        return page
