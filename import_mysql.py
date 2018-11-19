# coding=utf-8
import xlrd  
import xlwt  
from datetime import date,datetime 
import pymysql
import pandas as pd
from sqlalchemy import create_engine
import os
import re
# 把excel通过pandas读取成dataframe
def allexcelRead():
	rootdir = "./data1"
	filelist=[]
	for parent,dirnames,filenames in os.walk(rootdir):
		for filename in filenames:
			filelist.append(filename)
	print(filelist)
	dataframe=excelRead('ori_data.xlsx')
	for i in range(0,len(filelist)):
		df2=pd.read_excel("./data1"+r"/"+filelist[i],ignore_index=True)		
		dataframe = dataframe.append(df2,ignore_index=True)
	return dataframe
def excelRead(filename):
	dataframe= pd.read_excel(filename,skiprows=[0])
	return dataframe
# 创建数据库engine
class mysql_engine():
	user='root'
	passwd='tk553977388'
	host='localhost'
	port = '3306'
	db_name='test'
	engine = create_engine('mysql+mysqldb://{0}:{1}@{2}:{3}/{4}?charset=utf8'.format(user,passwd,host,port,db_name))
# 把dataframe写入ori_data table
def write2oridata(dataframe):
	pg_enine=mysql_engine()
	# print("success")
	try:
		with pg_enine.engine.connect() as con, con.begin():
			pd.io.sql.to_sql(dataframe,'ori_data', con, schema='test', if_exists='replace')  
		con.close()
	except Exception as e:
		raise e
# 把dataframe写入new_data table
def write2newdata(dataframe):
	passpg_engine=mysql_engine()
	# print("success")
	try:
		with pg_engine.engine.connect() as con, con.begin():
			pd.io.sql.to_sql(dataframe,'new_data', con, schema='test', if_exists='replace')  
		con.close()
	except Exception as e:
		raise 
# dataframe存在一个新生成的table中
def write2mySQL(dataframe,tablename):
	pg_engine=mysql_engine()
	# print("success")
	try:
		with pg_engine.engine.connect() as con, con.begin():
			pd.io.sql.to_sql(dataframe,tablename, con, schema='test', if_exists='replace')  
		con.close()
	except Exception as e:
		raise 
# 从数据库获取dataframe
def get_df_fromSQL(tablename):
	pg_engine=mysql_engine()
	try:
		with pg_engine.engine.connect() as con, con.begin():
			dataframe = pd.read_sql_query('select * from '+ tablename,con)
			con.close()
			# print(dataframe)
			return dataframe
	except Exception as e:
		raise e
def import_df_toexcel(dataframe,filename):
	writer = pd.ExcelWriter(filename)
	dataframe.to_excel(writer,'sheet1')
	writer.save()
def test():
	df= excelRead('new_data')
	write2mySQL(df,'test002')
	list= get_headers(df)

# df= excelRead('ori_data.xlsx')
# write2mySQL(df,'new1_data')

# df = get_df_fromSQL('new_data')
# import_df_toexcel(df,'d:/1.xlsx')

# if __name__ == '__main__':  
#     printPath(1, '/home/lizheng')  
#     print '总文件数 =', allFileNum  


# df = excelRead('d:/code/finalexam/finalversion/data/ori_data.xlsx')
# print(df[0:2])

# total_everymonth_charts(df).render()

# write2mySQL(df,'stud1_info')
