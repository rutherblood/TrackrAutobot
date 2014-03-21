#Implementation by Rutherblood
#Contact Author: <thecaptcha.314159@gmail.com> <github.com/rutherblood>
#*_T.* denotes code yet to be fully-tested or under the testing phase
#The bot makes a list of ep email ids on myaiesec.net as defined by the tempString.
#The bot is robust...upon intepreter/connection error, it saves it state continously and re-begins from there later.

import http.cookiejar
import urllib.request
from html.parser import HTMLParser

jarCookie=http.cookiejar.CookieJar()
urlOpener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(jarCookie))

#Global Constants
constGinger='http://www.myaiesec.net/exchange/viewep.do?operation=executeAction&epId='

tempCPairs=urllib.parse.urlencode((('userName','twisha.aiesec@gmail.com'),('password','twishaigip'),('login','LOGIN')))
loginString=bytes(tempCPairs,'utf-8')

tempDataPairs=(('operation','backgroundpopupEP'),('type','supply'),('bgrId','14'),('committeeId','2'),('xchType','GI'),('durFrom','6'),('durTo','78'),('subbgrname','Project Management'),('programType','null'),('categorybyselected','0'),('scope','2'),('exchangetype','GI'),('categoryby','0'),('durationFrom','6'),('durationTo','78'),('btnAdd','Search'))

tempCPairs=urllib.parse.urlencode(tempDataPairs)
sndString=bytes(tempCPairs,'utf-8')

del(tempDataString)
del(tempString)
del(jarCookie)

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


class autoTrackrSndPageParser(HTMLParser):
	def __init__(self):
		self.epID=[]
		self.sndPage=''

	def handle_starttag(self, tag, attrs):
		if tag=='a':
				if attrs[1][1][0:8]=='viewEP(\'' and attrs[1][1][len(attrs[1][1])-2:len(attrs[1][1])]=='\')':
					self.epID+=[attrs[1][1][8:len(attrs[1][1])-2]]
				
	def handle_data(self,data):
		localGinger='/exchange/toptendemandsupply.do?page='
		getMatch=stringMatcherCustom(data,localGinger)
		if len(stringMatcherCustom(data,'var len = 51'))!=0: #and len(getMatch)!=0 and len(stringMatcherCustom(data,'Next'))!=0
			self.sndPage='http://www.myaiesec.net/exchange/toptendemandsupply.do?page='
			count=0
			while 1==1:
				if data[getMatch[len(getMatch)-1]+len(localGinger)+count]=='\'':
					break
				else:
					self.sndPage+=data[getMatch[len(getMatch)-1]+len(localGinger)+count]     #CHNGED
					count+=1
					continue
				continue
		else:
			sndPage=''
	
class autoTrackrEPPageParser(HTMLParser):
	def __init__():
		self.emailID=[]

	def handle_data(self, data):
		if self.get_starttag_text()=='<a class="linkclass">':
			if len(stringMatcherCustom(data,'@'))!=0:
				self.emailID+=[data]



def main():
	global constGinger,loginString,sndString

	sndPage=''
	epPage=''

	stateFile=open('StateFile.txt','r')
	stateFileRead=stateFile.read()
	match=stringMatcherCustom(stateFileRead,' ')
	if len(match)!=0:
		sndPage=stateFileRead[0:match[0]]
		epPage=constGinger+stateFileRead[match[0]+1:len(stateFileRead)]
	else:
		sndPage='http://www.myaiesec.net/exchange/toptendemandsupply.do'
		epPage=''

	del(match)
	del(stateFileRead)	
	stateFile.close()
	del(stateFile)

	urlOpener.open('http://www.myaiesec.net/login.do',loginString)

	while len(sndPage)!=0:
		Pager=urlOpener.open(sndPage,sndString)
		sourceSndPage=Pager.read().decode()
		Pager.close()

		sndPageParse=autoTrackrSndPageParser()
		sndPageParse.feed(sourceSndPage)
		sndPageParse.close()

		epIDloc=0
		if len(epPage)!=0:
			epIDloc=0
		else:
			for i in sndPageParse.epID:
				if epPage[len(constGinger):len(epPage)]==i:
					epIDloc+=1
				else:
					break

		for i in range(epIDloc,len(sndParse.epID)):
			epPage=constGinger+sndParse.epID[i]
			Pager=urlOpener.open(epPage)
			sourceEPPage=Pager.read().decode()
			Pager.close()
			epPageParse=autoTrackrEPPageParser()
			epPageParse.feed(sourceEPPage)
			epPageParse.close()
			emailFile=open('emailIDDataTrackrAutobot.txt','a')
			print(epPageParse.emailID[i],file=emailFile)
			emailFile.close()
			epIDFile=open('StateFile.txt','w')
			print(sndPage+' '+sndParse.epID[i])   #TEST STATEMENT
			print(sndPage+' '+sndParse.epID[i],file=epIDFile)
			epIDFile.close()
			continue

		sndPage=sndPageParse.sndPage
		continue


if __name__ == '__main__':
    main()
