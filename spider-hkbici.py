#coding=utf-8
import urllib  
import urllib2  
import cookielib
import re
import sys

reload(sys)
sys.setdefaultencoding('utf8')

class HKBC:
	def __init__(self,baseurl,pagenum,kw = ''):
		self.url = baseurl
		self.depth = pagenum
		#构建header的dict结构
		self.headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36'}
		self.keyword = kw 


	def main(self):
		for x in range(self.depth):
			page = self.getpage(x + 1)
			info = self.getinfo(page)
			if self.keyword == '':
				for item in info:
					print item.decode('utf-8')
					print info[item]
			else:
				for item in self.search(info,self.keyword):
					print item.decode('utf-8')

	def search(self,info,key):
		pattern = re.compile('.*?'+ key + '.*?',re.S)
		results = []
		for item in info:
			title = info[item]
			if re.match(pattern,title):
				results.append(item)
				results.append(title)
		return results		
			

	def getinfo(self,page):
		pattern = re.compile('<em>.*?</em> <a href="(.*?)".*?class="xst" >(.*?)</a>',re.S)
		results = re.findall(pattern,page)
		info = {}
		for result in results:
			info[result[0]] = result[1]
		return info

	def getpage(self,pageindex):
		'''
		#cookie存放文件
		filename = "cookie.txt"
		'''
		#创建MozillaCookieJar实例用以保存cookie
		cookie = cookielib.MozillaCookieJar()
		#从文件中读取cookie
		cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
		#创建opener对象
		opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie)) 
		#安装opener方法
		urllib2.install_opener(opener)
		
		'''
		#cookie文件初始化所用代码
		#创建登录url
		loginurl = 'http://hk-bici.com/member.php?mod=logging&action=login&loginsubmit=yes&handlekey=login&loginhash=LaijH&inajax=1'
		#formdata提交已编码的表单内容
		formdata = "formhash=c97618ca&referer=http%3A%2F%2Fhk-bici.com%2Fforum-2-2.html&loginfield=username&username=wjq5858123&password=987456&questionid=0&answer=&cookietime=2592000&loginsubmit=true"
		request = urllib2.Request(loginurl,formdata,self.headers) 
		#登录并保存cookies 
		response = opener.open(request)
		cookie.save(ignore_discard = True,ignore_expires = True)
		'''
		
		
		url = self.url + str(pageindex) + '.html'
		acrequest = urllib2.Request(url,None,self.headers)
		response = opener.open(acrequest)
		page = response.read()
		return page



print "Please type in searching depth(page):"
pagenum = int(raw_input())
url = 'http://hk-bici.com/forum-2-'
print "Please type in the keyword for searching:"
kw = raw_input()
#pagenum = 20
#kw = ''
hkbc = HKBC(url,pagenum,kw)
hkbc.main()


