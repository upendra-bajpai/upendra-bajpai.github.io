from pygooglenews import GoogleNews
import os
from bs4 import BeautifulSoup
import csv
import os
# default GoogleNews instance
category_list=['TECHNOLOGY','SCIENCE','HEALTH','BUSINESS']
for category in category_list:
	pass
	file_path=category+'.csv'
	file=os.path.join('csvs',file_path)
	gn = GoogleNews(lang = 'en', country = 'IN')
	tech = gn.topic_headlines(category, proxies=None, scraping_bee = None)
	with open(file, 'w', newline='',encoding="utf-8") as the_file:
		writer = csv.writer(the_file)
		#writer.writerow(['title','link'])
		for x in tech['entries']:
			sumry=x['summary']
			#print(sumry)
			parsedContent = BeautifulSoup(sumry, 'html.parser')
			atg=parsedContent.find('a')
			#print(atg.text)
			writer.writerow([atg.text, x['link']])
			for urls in x['sub_articles']:
				pass
				#print(urls['url'])
				titlr=urls['title'].replace(",", " ")
				writer.writerow([urls['title'],urls['url']])
	print('created csv of "{category}"')
	the_file.close()