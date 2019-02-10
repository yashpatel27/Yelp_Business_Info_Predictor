from bs4 import BeautifulSoup
import re
#import urllib2
#from operator import itemgetter
import time
#import sys
import requests
import os

def run(url):
    for p in range(0,2):  
        if p==0:                                                                                         #For page num=1
 
            pageLink=url 
        else:                                                                                           #For pages after
            pageLink=url+'?start='+str(p*20)
            
        for i in range(5): # try 5 times
            try:
                response=requests.get(pageLink,headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', })
                html=response.content 
                break 
            except Exception as e:
                print ('failed attempt',i)
                time.sleep(2)
                #ss=input("No internet, Enter Anything")		
                
        if not html:continue # couldnt get the page, ignore
        
        revsoup = BeautifulSoup(html)# parse the html
        review_content=revsoup.findAll('div',{'class': 'review-content'})        #Find review content with rating and date
        for div in review_content:
            """review_date=revsoup.findAll('span',{'class':re.compile('rating-qualifier')})
            date=str(review_date[0])
            d1=re.findall(r'class="rating-qualifier"> (.*)',str(date))
            print d1"""
            elem=div.find('p')                                              #Scrappng review text from review content
            if elem:
                try:
                    f.write(elem.text)                                #Writting review Text to the file  
                                   
                except UnicodeEncodeError:
                    f.write('\n')
            
    f.close()                                                                 #Closing file 

if __name__=='__main__':
    #newpath = r'Yelp_reviews'                                   #Creating folder for Yelp to store the restaurant reviews
    #if not os.path.exists(newpath):
        #os.makedirs(newpath)
    
    #Reading the file from which the restaurants names are taken to search in Yelp and Scrape the reviews
    path=r'links.txt'    
    
    fin=open(path)
    for line in fin:                                        #For each name of restaurant in the List
        words = line.lower().strip()                     
        #restaurant_name=words
        
        #words = re.findall(r'/biz/(.*?)-san-francisco',words)
        print (words)
        if "-san-franc" in words:       
            start = words.index( "/biz/" ) + len( "/biz/" )
            end = words.index( "-san-franc", start )
        
        elif "-brisbane" in words:
                start = words.index( "/biz/" ) + len( "/biz/" )
                end = words.index( "-brisbane", start )
        else:
            if "-alameda" in words:
                start = words.index( "/biz/" ) + len( "/biz/" )
                end = words.index( "-alameda", start )
            
    
        names = str(words[start:end])
        names = names.replace('-',' ')
        #f=open('Yelp\San_Fransisco\American\Reviews''\\'+names+'.txt','w')      #New file Created by Restaurant name to store the reviews
        #f=open('Yelp_reviews_new''\\'+names+'.txt','w')      #New file Created by Restaurant name to store the reviews
        f=open(names+'.txt','w')      #New file Created by Restaurant name to store the reviews   
        url='https://www.yelp.com'+str(words)         #Creating URL for restaurant
        run(url)                                                            #Passing URL to the function
	
