import os
import stat
import datetime
import shutil
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
	#os.rename(old_csv_path,mv_csv)
if os.path.exists(old_news_path):
	list_dir=os.scandir(old_news_path)
	print(str(list_dir))
	for sub_dir in list_dir:
		#old_path=os.path.join(old_news_path,sub_dir.path)
		new_path=os.path.join(mv_files,sub_dir.name)
		print(sub_dir.path)
		print(new_path)
		shutil.move(old_path,new_path)
