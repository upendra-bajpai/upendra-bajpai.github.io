from newspaper import Article
import string
import datetime
import codecs
import csv
import os
import time
import re
import shutil
def news_article(url,category):
	pass
	article=Article(url)
	article.download()
	article.parse()
	title=article.title
	title=[re.sub(r"[^a-zA-Z0-9]+", ' ', k) for k in title.split("\n")]
	title=title[0]
	print(title)
	content=article.text
	top_img=article.top_image
	vids=article.movies
	if(len(content)>0):
		with codecs.open(gen_title(title,category), 'w',encoding='utf8') as the_file:
			write_md_head(the_file,title,category,top_img)
			the_file.write(content)
		the_file.close()

def gen_title(title,category):
	pass
	root='newsData'
	titles=title.replace(" ", "-")
	date = datetime.date.today()
	title=str(date)+'-'+titles+'.md'
	path=os.path.join(root,category,title)
	return path


def write_md_head(the_file,title,category,image):
	pass
	now=datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S') 
	the_file.write('---\n')
	the_file.write(f'layout: post\ntitle: "{title}"\nauthor: jane \ndate: {now} \ncategories: [ {category} ] \nimage: {image}')
	the_file.write('\n---\n')

def articale_entry():
	root='csvs'
	i=0;
	#url='https://news.google.com/__i/rss/rd/articles/CBMic2h0dHBzOi8vd3d3LmdhbWVzcmFkYXIuY29tL3BsYXlzdGF0aW9uLXdlYnNpdGUtcHJlcGFyZXMtcHJlLW9yZGVycy1mb3ItcHM1LWJ1dC1vbmx5LW9uZS12ZXJzaW9uLWNhbi1iZS1wcmUtb3JkZXJlZC_SAXdodHRwczovL3d3dy5nYW1lc3JhZGFyLmNvbS9hbXAvcGxheXN0YXRpb24td2Vic2l0ZS1wcmVwYXJlcy1wcmUtb3JkZXJzLWZvci1wczUtYnV0LW9ubHktb25lLXZlcnNpb24tY2FuLWJlLXByZS1vcmRlcmVkLw?oc=5'
	category_list=['HEALTH','BUSINESS','SCIENCE','TECHNOLOGY']
	for category in category_list:
		try:
			os.mkdir(os.path.join('newsData',category))
		except:
			print("can not create dir for news markdown")
		path=category+".csv"
		print(os.path.join(root,path))
		with open(os.path.join(root,path), mode='r',encoding="utf-8") as csv_file:
			csv_reader = csv.reader(csv_file,delimiter=',')
			#print(csv_reader[0])
			for row in csv_reader:
				url=row[1]
				print( url)
				try:
					news_article(url,category)
				except:
					continue
	archive_files()
					# time.sleep(100)
					# news_article(url,category)
					# print('wrote article {i++}',flush=True)

def archive_files():
	root=os.getcwd()
	date = datetime.datetime.now().strftime('%d-%m-%Y %H-%M') 
	print(date)
	fol_csv='csvs'
	fol_data='newsData'
	old_csv_path=os.path.join(root,fol_csv)
	old_news_path=os.path.join(root,fol_data)
	mv_csv=os.path.join(root,str(date)+'csv')
	mv_files=os.path.join(root,str(date)+'newsData')
	if os.path.exists(old_csv_path):
		pass
		os.rename(old_csv_path,mv_csv)
	if os.path.exists(old_news_path):
		list_dir=os.scandir(old_news_path)
		#os.mkdir(mv_files)
		for sub_dir in list_dir:
			new_path=os.path.join(mv_files,sub_dir.name)
			print(sub_dir.path)
			print(new_path)
			shutil.move(sub_dir.path,new_path)
	try:
		os.mkdir(old_csv_path,0o777)
		# os.mkdir(old_news_path,0o777)
		# os.chmod(old_csv_path, stat.S_IWRITE)
		#os.unlink(old_csv_path)
		pass
	except Exception as e:
		print('can not create ${old_news_path} or {old_csv_path}')
		raise
	#articale_entry()
	pass
articale_entry()