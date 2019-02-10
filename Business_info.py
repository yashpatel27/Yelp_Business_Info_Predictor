import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup, SoupStrainer
import requests
import re
from selenium.webdriver.common.by import By
import subprocess




html=None
link_list = []
for i in range(3):
	print("Page", i)
	url = "https://www.yelp.com/search?find_desc=american&find_loc=San+Francisco,+CA&start=" + str((i * 10))
	print(url)
	for i in range(5):
		try:
			response=requests.get(url, headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', })
			html=response.content
			break
		except Exception as e:
			print ('failed attempt',i)

	#time.sleep(5)
	soup = BeautifulSoup(html.decode('ascii', 'ignore'),'lxml') #decode html
	#print(soup.encode("utf-8"))

	data = soup.findAll('a', attrs = {'data-analytics-label': 'biz-name'})
	for dataa in data:
		if '/biz/' in dataa['href']:
			link_list.append(dataa['href'])
			print(dataa['href'])


fopen = open('links.txt', 'w')
for link in link_list:
	fopen.write(link + "\n")
fopen.close()

result = open('result.txt', 'w')


browser = webdriver.Chrome('./chromedriver')




for page in link_list:
	try:
		page_url = 'https://www.yelp.com' + page
		browser.get(page_url)
		#name = browser.find_element_by_xpath('//*[@id="wrap"]/div[2]/div/div[1]/div/div[3]/div[1]/div[1]/h1')
		#print(name.text.encode('utf-8'))
		#result.write(name.text + '\n')
		words = page.lower().strip()    
		print (words)
		if "-san-franc" in words:       
			start = words.index( "/biz/" ) + len( "/biz/" )
			end = words.index( "-san-franc", start )
		else: 
			if "-brisbane" in words:
				start = words.index( "/biz/" ) + len( "/biz/" )
				end = words.index( "-brisbane", start )
    
		names = str(words[start:end])
		names = names.replace('-',' ')
        #f=open('Yelp\San_Fransisco\American\Reviews''\\'+names+'.txt','w')      #New file Created by Restaurant name to store the reviews
        #f=open('Yelp_reviews_new''\\'+names+'.txt','w')      #New file Created by Restaurant name to store the reviews

		result.write(names + '\n')
      
		print(10 * '--')
		result.write('---------------' + '\n')	
		lists = browser.find_elements_by_class_name('ywidget')
		for listing in lists:
			if "More business info" in listing.text:
				if "Reservations Yes" in listing.text:  				
					result.write('reservations yes'+ '\n')
				elif "Reservations No" in listing.text:  
					result.write('reservations no'+ '\n')                        
				else:
					result.write('reservations no'+ '\n')                       
				if "Delivery Yes" in listing.text:  				
					result.write('delivery yes'+ '\n')
				elif "Delivery No" in listing.text:  
					result.write('delivery no'+ '\n')                        
				else:  
					result.write('delivery no'+ '\n')                        
				if "Parking No" in listing.text:  				
					result.write('parking no'+ '\n')
				elif "Parking No" not in listing.text and "Parking" in listing.text:
					result.write('parking yes'+ '\n')     
				else:  
					result.write('parking no'+ '\n')                    
				if "Alcohol No" in listing.text:  				
					result.write('alcohol no'+ '\n')
				elif "Alcohol No" not in listing.text and "Alcohol" in listing.text:
					result.write('alcohol yes'+ '\n')                        
				else:  
					result.write('alcohol no'+ '\n')                    
					#result.write(listing.text + '\n')'''
		result.write('\n')
	except Exception as e:
		print(e)

result.close()