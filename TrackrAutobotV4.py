#Implementation by Rutherblood
#Contact Author: <thecaptcha.314159@gmail.com> <github.com/rutherblood>
#*_T.* denotes code yet to be fully-tested or under the testing phase
#The bot makes a list of ep email ids on myaiesec.net as defined by the tempString.
#The bot is super robust...upon intepreter/connection error, it saves it state continously and re-begins from there later.
#To add: Exception Handling for connection errors for: 1. Connection Errors 2.Unicode decode byte 0xe9 errors
#To add: UI
#To add: Optimize

import http.cookiejar
import urllib.request
from html.parser import HTMLParser

jarCookie=http.cookiejar.CookieJar()
urlOpener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(jarCookie))

#Global Constants
tempCPairs=urllib.parse.urlencode((('userName','twisha.aiesec@gmail.com'),('password','twishaigip'),('login','LOGIN')))
loginString=bytes(tempCPairs,'utf-8')

tempDataPairs=(('operation','backgroundpopupEP'),
	('type','supply'),
	('bgrId','29'),
	('committeeId','2'),
	('xchType','GC'),
	('durFrom','6'),
	('durTo','78'),
	('subbgrname','Microeconomics'),
	('programType','null'),
	('categorybyselected','0'),
	('scope','2'),
	('exchangetype','GC'),
	('categoryby','0'),
	('durationFrom','6'),
	('durationTo','78'),
	('btnAdd','Search'))

tempCPairs=urllib.parse.urlencode(tempDataPairs)
sndString=bytes(tempCPairs,'utf-8')

del(tempCPairs)
del(tempDataPairs)
del(jarCookie)

def stringMatcherCustom(string1,string2):
  str2Count=0
  count=[]
  temp=1-len(string2)
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

def stripCharFromStr(strInQues,char):
	positionValues=stringMatcherCustom(strInQues,char)
	tempStrInCons=''
	loopCounter=0
	while loopCounter<len(strInQues):
		if loopCounter in positionValues:
			loopCounter+=len(char)
			continue
		else:
			tempStrInCons+=strInQues[loopCounter]
			loopCounter+=1
			continue
		continue
	return tempStrInCons

class autoTrackrSndPageParser(HTMLParser):
  def __init__(self):
    HTMLParser.__init__(self)
    self.epNameID=[]    #EP NAME EDIT
    self.epID=[]
    self.sndPage=''

  def handle_starttag(self, tag, attrs):
    if tag=='a':
        if attrs[1][1][0:8]=='viewEP(\'' and attrs[1][1][len(attrs[1][1])-2:len(attrs[1][1])]=='\')':
          self.epID+=[attrs[1][1][8:len(attrs[1][1])-2]]
        
  def handle_data(self,data):									
    if type(self.get_starttag_text())!=type(None):				#EP NAME EDIT
      if len(stringMatcherCustom(self.get_starttag_text(),'onclick="viewEP('))!=0:      
        if len(stringMatcherCustom(data,'EP'))!=0:
        	self.epNameID+=[data]
    localGinger='/exchange/toptendemandsupply.do?page='
    if len(stringMatcherCustom(data,'var len = 51'))!=0: #and len(getMatch)!=0 and len(stringMatcherCustom(data,'Next'))!=0
      getMatch=stringMatcherCustom(data,localGinger)
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
  def __init__(self):
    HTMLParser.__init__(self)
    self.emailID=''
    self.epName=''  #EP NAME EDIT

  def handle_data(self, data):
    if type(self.get_starttag_text())!=type(None) and len(data)!=0:
      if len(stringMatcherCustom(self.get_starttag_text(),'page-mainHeader-class'))!=0:  #EP NAME EDIT
        if len(stringMatcherCustom(data,'\n'))==0 and len(stringMatcherCustom(data,'\t'))==0 and data!=' ':
          self.epName=data

    if self.get_starttag_text()=='<a class="linkclass">':
      if len(stringMatcherCustom(data,'@'))!=0:
        self.emailID=data


def mainBot(sndString):                                  #mainBot: UI Edit
  global loginString,urlOpener

  constGinger='http://www.myaiesec.net/exchange/viewep.do?operation=executeAction&epId='
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
    sourceSndPage=Pager.read().decode('latin-1').encode('utf-8').decode() #FIX
    Pager.close()

    sndPageParse=autoTrackrSndPageParser()
    sndPageParse.feed(sourceSndPage)
    sndPageParse.close()

    epIDloc=0
    if len(epPage)==0:   #FIX
      epIDloc=0
    elif stripCharFromStr(epPage[len(constGinger):len(epPage)],'\n') in sndPageParse.epID:
      for i in sndPageParse.epID:
        if epPage[len(constGinger):len(epPage)]==i+'\n':    #STATE BUG FIX: stripCharFromStr(epPage[len(constGinger):len(epPage)],'\n')
          epIDloc+=1
          break
        epIDloc+=1
        continue
      if epIDloc==len(sndPageParse.epID):   #FIX
        sndPage=sndPageParse.sndPage
        continue

    for i in range(epIDloc,len(sndPageParse.epID)):
      epPage=constGinger+sndPageParse.epID[i]
      Pager=urlOpener.open(epPage)
      sourceEPPage=Pager.read().decode('latin-1').encode('utf-8').decode() #FIX
      Pager.close()
      epPageParse=autoTrackrEPPageParser()
      epPageParse.feed(sourceEPPage)
      epPageParse.close()
      emailFile=open('emailIDDataTrackrAutobot.txt','a')
      print(epPageParse.epName+'\t'+sndPageParse.epNameID[i]+'\t'+epPageParse.emailID,file=emailFile)   #epPageParse.epName+' '+
      emailFile.close()
      epIDFile=open('StateFile.txt','w')
      print(sndPage+' '+sndPageParse.epID[i],file=epIDFile)
      epIDFile.close()
      continue

    sndPage=sndPageParse.sndPage
    print(sndPage)    #TEST STATEMENT
    continue

if __name__ == '__main__':
    mainBot(sndString)                           #mainBot: UI Edit
