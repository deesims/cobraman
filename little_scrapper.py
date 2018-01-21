import re
import requests


class Suspect:
    def __init__(self, name, username, city):
        self.name = name
        self.username = username
        self.city = city
    def __str__(self):
        return('Name: ' + self.name)


class Crawler:    
    def __init__(self, name, url, suspect, keywords):
        self.name = name
        self.url = url
        self.suspect = suspect

        if name=='twitter':
            self.suspectUrl = url + suspect.username 
            self.request = requests.get(url + suspect.username)
            self.html = re.sub('<[^>]*>', ' ', self.request.text)

        elif name=='google':
            self.suspectUrl = url + suspect.username 
            self.request = requests.get(url + 'search?q=' + suspect.name)
            self.html = re.sub('<[^>]*>', '', self.request.text)


##        elif name=='facebook':
##
##            self.suspectUrls = list()
##            for x in range(0,100,10):
##                self.suspectUrls.append(url + 'search?q=' + suspect.name + '&start=' + str(x))
##                
##            self.requests = list()
##            for url in self.suspectUrls:
##                print(url)
##                self.requests.append(requests.get(url))
##
##            self.htmls = list()
##            for html in self.requests:
##                formatted = re.sub('<[^>]*>', '', str(html))
##                print(formatted)
##                break
##                self.htmls.append(formatted_text)

    def matchKeywords(self, Keywords):

        if self.name == 'twitter':
            print('scanning... url = ' + self.suspectUrl)
            for key in range(len(Keywords.list)):
                if self.html.find(' ' + Keywords.list[key] + ' ') != -1:
                    print('key: ' + Keywords.list[key] + '  found: ' + str(self.html.count(' ' + Keywords.list[key] + ' ')))

        elif self.name == 'google':
            print('scanning... url = ' + self.suspectUrl)
            for key in range(len(Keywords.list)):
                if self.html.find(Keywords.list[key]) != -1:
                    print('key: ' + Keywords.list[key] + '  found: ' + str(self.html.count(Keywords.list[key])))

        
        elif self.name == 'facebook':
            print('scanning...url = ' + self.url)
            for key in range(len(Keywords.list)):
                print('key:' + Keywords.list[key])
                for urlKey in range(len(self.htmls)):
                    if self.htmls[urlKey].find(' ' + Keywords.list[key] + ' ') != -1:
                        print('found: ' + str(self.htmls[urlKey].count(Keywords.list[key])))
class Keywords:
    def __init__(self, filename):
        filename = 'keywords.txt'
        with open(filename) as file:
            self.list = [line.strip() for line in file]
            
            
        


#setup suspect
suspect =Suspect('Ilona+Hlovyak', 'ilonaah15', 'Ottawa')
suspect2 = Suspect('Donald+Trump', 'realDonaldtrump', 'New York')
suspect3 = Suspect('Norm+Kelly', 'norm', 'Toronto')
suspect4 = Suspect('Kodak+Black', 'kodakblack1k', '1800BLK')
suspect5 = Suspect('Ahmad+Assi', 'ahmad_assi97', 'Ottawa')
suspect6 = Suspect('Kevin+Hart', 'kevinhart4real', 'Ottawa')
suspect7 = Suspect('Neil+rordan', 'neilriordan', 'Panama')

#setup keywords
keywords = Keywords('keywords.txt')

#setup crawler
ilonasCrawler = Crawler('twitter','https://twitter.com/', suspect, keywords)
donaldsCrawler = Crawler('twitter', 'https://twitter.com/', suspect2, keywords)
normsCrawler = Crawler('twitter', 'https://twitter.com/', suspect3, keywords)
kodaksCrawler = Crawler('twitter', 'https://twitter.com/', suspect4, keywords)
ahmadsCrawler = Crawler('twitter', 'https://twitter.com/', suspect5, keywords)
alexsCrawler = Crawler('twitter', 'https://twitter.com/', suspect6, keywords)
neilsCrawler = Crawler('twitter', 'https://twitter.com/', suspect7, keywords)


neilsCrawler.matchKeywords(keywords)
ahmadsCrawler.matchKeywords(keywords)
alexsCrawler.matchKeywords(keywords)
kodaksCrawler.matchKeywords(keywords)
normsCrawler.matchKeywords(keywords)
ilonasCrawler.matchKeywords(keywords)
donaldsCrawler.matchKeywords(keywords)
