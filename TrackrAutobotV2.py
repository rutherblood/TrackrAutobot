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
nextPage=['http://www.myaiesec.net/exchange/toptendemandsupply.do',True]
constGinger='http://www.myaiesec.net/exchange/viewep.do?operation=executeAction&epId='

sexyString=urllib.parse.urlencode((('userName','twisha.aiesec@gmail.com'),('password','twishaigip'),('login','LOGIN')))
postString=bytes(sexyString, 'utf-8')

sexyStringMeta=(('operation','backgroundpopupEP'),('type','supply'),('bgrId','44'),('committeeId','4'),('xchType','GI'),('durFrom','6'),('durTo','78'),('subbgrname','International Marketing'),('programType','null'),('categorybyselected','0'),('scope','2'),('exchangetype','GI'),('categoryby','0'),('durationFrom','6'),('durationTo','78'),('btnAdd','Search'))
sexyString=urllib.parse.urlencode(sexyStringMeta)
sNDPostString=bytes(sexyString,'utf-8')

def stringMatcherCustom(string1,string2):
	str2Count=0
	count=[]
	temp=1-len(string2)
	#matchValue=False
	for i in range(len(string1)):
		if string1[i]==string2[str2Count]:
			while(1==1):
				if str2Count<len(string2)-1:
					str2Count+=1
					break
				else:
					count+=[i]
					str2Count=0
					break
				break
			continue
		else:
			str2Count=0
			continue
		continue
	for i in range(len(count)):
		count[i]+=temp
		continue
	return count
		
class autoTrackrHTMLParser(HTMLParser):
	def handle_starttag(self, tag, attrs):
		global epID
		if tag=='a':
				if attrs[1][1][0:8]=='viewEP(\'' and attrs[1][1][len(attrs[1][1])-2:len(attrs[1][1])]=='\')':
					epID+=[attrs[1][1][8:len(attrs[1][1])-2]]
				
	def handle_data(self,data):
		global nextPage
		count=0
		localGinger='/exchange/toptendemandsupply.do?page='
		getMatch=stringMatcherCustom(data,localGinger)
		#getMatch2=stringMatcherCustom(data,'Next')
		if len(getMatch)!=0 and len(stringMatcherCustom(data,'Next'))!=0:
			nextPage=['http://www.myaiesec.net/exchange/toptendemandsupply.do',True]
			while 1==1:
				if data[getMatch[len(getMatch)-1]+len(localGinger)+count]=='\'':
					break
				else:
					nextPage[0]=nextPage[0]+'?page='+data[getMatch[len(getMatch)-1]+len(localGinger)+count]
					count+=1
					continue
				continue
		else:
			nextPage[1]=nextPage[1] or False
			
sexyParser=autoTrackrHTMLParser(strict=False)
	
class autoTrackrHTMLParser2(HTMLParser):
	def handle_data(self, data):
		global emailID
		if self.get_starttag_text()=='<a class="linkclass">':
			for i in range(len(data)):
				if data[i]=='@':
					emailID+=[data]
		
sexyEmailParser=autoTrackrHTMLParser2(strict=False)
			
#Phase I: Login
src.open('http://www.myaiesec.net/login.do',postString)

while nextPage[1]==True:
	nextPage[1]=False
	#Phase-II: Get EPs' list-page
	respSrc = src.open(nextPage[0],sNDPostString)
	sourceRaw=respSrc.read().decode()
	respSrc.close()
	print(sourceRaw)
		
	#Phase-III: Deploying Parser for extraction of EP IDs
	sexyParser.feed(sourceRaw)
	sexyParser.close() 

	#Phase-IV: Extract email IDs
	for i in range(len(epID)):
		respSrc = src.open(constGinger+epID[i])
		sourceRaw=respSrc.read().decode()
		respSrc.close()
		sexyEmailParser.feed(sourceRaw)
		sexyEmailParser.close() 

	#Phase-V: Print the email addresses in a file
	oss=open('emailIDDataTrackrAutobot.txt','a')
	for i in range(len(emailID)):
		print(emailID[i],file=oss)
		continue
	oss.close()
	continue 