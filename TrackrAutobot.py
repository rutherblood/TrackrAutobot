#sexyStringMeta=(('operation','toptenep'),('type','supply'),('bgrId',''),('committeeId',''),('xchType',''),('durFrom',''),('durTo',''),('subbgrname',''),('programType','null'),('categorybyselected',''),('scope','2'),('exchangetype','GI'),('categoryby','0'),('durationFrom','6'),('durationTo','78'),('btnAdd','Search'))
#sexyStringMeta2=(('operation','backgroundpopupEP'),('type','supply'),('bgrId','44'),('committeeId','4'),('xchType','GI'),('durFrom','6'),('durTo','78'),('subbgrname','International Marketing'),('programType','null'),('categorybyselected','0'),('scope','2'),('exchangetype','GI'),('categoryby','0'),('durationFrom','6'),('durationTo','78'),('btnAdd','Search'))

#src=urllib.request.urlopen('http://www.myaiesec.net',bye)
#constGinger='http://www.myaiesec.net/exchange/viewep.do?operation=executeAction&epId='

#Phase-0: Initialization
import http.cookiejar
import urllib.request
from html.parser import HTMLParser
sexyCookie=http.cookiejar.CookieJar()
src=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(sexyCookie))
epID=[]
emailID=[]
constGinger='http://www.myaiesec.net/exchange/viewep.do?operation=executeAction&epId='

#Phase I: Login
sexyString=urllib.parse.urlencode((('userName','twisha.aiesec@gmail.com'),('password','twishaigip'),('login','LOGIN')))
postString=bytes(sexyString, 'utf-8')
src.open('http://www.myaiesec.net/login.do',postString)

#Phase-II: Get EPs' list-page
sexyStringMeta2=(('operation','backgroundpopupEP'),('type','supply'),('bgrId','44'),('committeeId','4'),('xchType','GI'),('durFrom','6'),('durTo','78'),('subbgrname','International Marketing'),('programType','null'),('categorybyselected','0'),('scope','2'),('exchangetype','GI'),('categoryby','0'),('durationFrom','6'),('durationTo','78'),('btnAdd','Search'))
sexyString=urllib.parse.urlencode(sexyStringMeta2)
sNDPostString=bytes(sexyString,'utf-8')
respSrc = src.open('http://www.myaiesec.net/exchange/toptendemandsupply.do',sNDPostString)
sourceRaw=respSrc.read().decode()
respSrc.close()
print(sourceRaw)

#Phase-III:Readying Parsers to handle html source
class autoTrackrHTMLParser(HTMLParser):
	def handle_starttag(self, tag, attrs):
		global epID
		if tag=='a':
			if attrs[1][1][0:8]=='viewEP(\'' and attrs[1][1][len(attrs[1][1])-2:len(attrs[1][1])]=='\')':
				epID+=[attrs[1][1][8:len(attrs[1][1])-2]]
	
sexyParser=autoTrackrHTMLParser(strict=False)
	
class autoTrackrHTMLParser2(HTMLParser):
	def handle_data(self, data):
		global emailID
		if self.get_starttag_text()=='<a class="linkclass">':
			for i in range(len(data)):
				if data[i]=='@':
					emailID+=[data]
		
sexyEmailParser=autoTrackrHTMLParser2(strict=False)
	
#Phase-IV: Deploying Parser for extraction of EP IDs
sexyParser.feed(sourceRaw)
sexyParser.close() 

#Phase-V:
for i in range(len(epID)):
	respSrc = src.open(constGinger+epID[i])
	sourceRaw=respSrc.read().decode()
	respSrc.close()
	sexyEmailParser.feed(sourceRaw)
	sexyEmailParser.close() 

#Phase-VI: Print the email addresses in a file
oss=open('emailIDDataTrackrAutobot.txt','a')
for i in range(len(emailID)):
	print(emailID[i],file=oss)

oss.close()