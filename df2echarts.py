#coding=utf-8
import random
from pyecharts import Bar, Page,Line
# from app.charts.constants import WIDTH, HEIGHT

from imprv2 import APRU_Chuzhang,month_Chuzhang,yearincome_filter,MOU,DOU
import math
from import_mysql import excelRead
from import_mysql import get_df_fromSQL
from headerAndtypes import *
from import_mysql import *
from imprv2 import *
def create_total_charts(df):
	page = Page()
	df_new = pd.DataFrame()
	list1 = coltype_filter(df,'套餐类型')
	num = len(list1)
	v1=[x for x in range(0,num)]
	for i in range(0,num):
		df_new = df[df['套餐类型']==list1[i]]
		v1[i]=month_Chuzhang(df_new)
	# v2 = [10, 25, 8, 60, 20, 80]
	v2=[x for x in range(0,num)]
	for i in range(0,num):
		df_new= df[df['套餐类型']==list1[i]]
		v2[i]=APRU_Chuzhang(df_new)
	v3 = [x for x in range(0,num)]
	for i in range(0,num):
		df_new=df[df['套餐类型']==list1[i]]
		v3[i]=MOU(df_new)
	v4 = [x for x in range(0,num)]
	for i in range(0,num):
		df_new=df[df['套餐类型']==list1[i]]
		v4[i]=DOU(df_new)
	chart = Bar("数据分析", "月总收入/平均收入/MOU/DOU")
	chart.add("月总收入", list1, v1)
	chart.add("各套餐平均收入", list1, v2)
	chart.add("MOU", list1, v3)
	chart.add("DOU", list1, v4)
	# chart.add("月平均收入", attr, v2, is_stack=True, is_more_utils=True)
	page.add(chart)
	return page
# def create_com_charts(dataframe):
# 	page=Page()

def create_avg_charts(dataframe):
	page=Page()
	# df= get_df_fromSQL('ori_data')
	df_new = pd.DataFrame()
	list1 = coltype_filter(dataframe,'套餐类型')
	num = len(list1)
	v2= [x for x in range(0,num)]
	for i in range(0,num):
		df_new = detailed_info_filter(dataframe,'套餐类型',[list1[i]])
		v2[i]=APRU_Chuzhang(df_new)
	chart = Bar("月平均收入",'各种套餐类型')
	# chart.add('平均收入',list,v1,is_stack=True)
	chart.add("月平均收入", list, v2, is_stack=True, is_more_utils=True)
	page.add(chart)
	return page	
def create_combine_charts(dataframe):
	page=Page()
	# df= get_df_fromSQL('ori_data')
	df_new = pd.DataFrame()
	list1 = coltype_filter(dataframe,'套餐类型')
	num = len(list1)
	v1= [x for x in range(0,num)]
	v2= [x for x in range(0,num)]
	v3 = [x for x in range(0,num)]
	v4 = [x for x in range(0,num)]
	for i in range(0,num):
		df_new = detailed_info_filter(dataframe,'套餐类型',[list1[i]])
		v1[i]=month_Chuzhang(df_new)
	for i in range(0,num):
		df_new = detailed_info_filter(dataframe,'套餐类型',[list1[i]])
		v2[i]=APRU_Chuzhang(df_new)
	# for i in range(0,num):
	# 	df=dataframe[dataframe['套餐类型']==list1[i]]
	# 	v3[i]=MOU(df)
	# for i in range(0,num):
	# 	df = dataframe[dataframe['套餐类型']==list1[i]]
	# 	v4[i]=DOU(df)
	chart = Bar("数据分析",'总收入/平均出帐收入/MOU/DOU')
	chart.add('总收入',list,v1)
	chart.add("月平均收入", list, v2)
	# chart.add('MOU',list,v3)
	# chart.add('DOU',list,v4)
	page.add(chart)
	return page
def total_everymonth_charts(dataframe):
	page = Page()
	list1 = coltype_filter(dataframe,'账期')
	df_new = pd.DataFrame()
	num = len(list1)
	v1 = [x for x in range(0,num)]
	v2 = [x for x in range(0,num)]
	for i in range(0,num):
		df_new =detailed_info_filter(dataframe,'账期',[list1[i]])
		v1[i]=month_Chuzhang(df_new)
	chart = Line("折线图",'一年的降水量')
	chart.add("降水量",list1,v1,is_label_show=True)
	page.add(chart)
	return page
# def person_everymonth_charts(dataframe):
def person_MOU_charts(dataframe):
	page =Page()
	list1=coltype_filter(dataframe,'账期')
	# print(list1)
	list1.sort()
	list2 =all_MOU(dataframe)
	charts = Line("MOU")
	charts.add("每人每月平均通话次数",list1,list2,
    mark_point=[ "max", "min"],
    is_label_show=True,
    mark_point_textcolor="#40ff27")

	# v1=[x fo in range(0,num)]
	# for i in range(0,num):
	# 	df_new = detailed_info_filter(dataframe,'套餐类型',[list1[i]])
	# 	v1[i]=month_Chuzhang(df_new)
	# # v2 = [10, 25, 8, 60, 20, 80]
	# chart = Bar("月总收入", "各套餐类型")
	# chart.add("月总收入", list, v1, is_stack=True)
	# # chart.add("月平均收入", attr, v2, is_stack=True, is_more_utils=True)
	page.add(charts)
	return page
def create_DOU_charts(dataframe):
	page =Page()
	list3=coltype_filter(dataframe,'账期')
	# print(list1)
	list3.sort()
	list4 =All_DOU(dataframe)
	charts = Line("DOU")
	charts.add("每人每月平均使用流量",list3,list4)

	page.add(charts)
	return page
# df=get_df_fromSQL("new_data")
# create_DOU_charts(df).render()
def sameUserDataframe(df,numlist):
	df_new = df[df['用户标识']==numlist]

	
	list3 = coltype_filter(df,'账期')
	list3.sort()
	n=len(list3)
	yearIncome=month_Chuzhang(df_new)
	# monthIncome = yearIncome/n
	list5 = All_DOU(df)
	list6 = all_MOU(df)
	list7 = all_APRU(df)
	page =Page()
	charts1 = Line("DOU")
	charts1.add(str(numlist)+"的DOU",list3,list5)
	# charts2 = Line("MOU")
	charts1.add(str(numlist)+"的MOU",list3,list6)
	# charts3  =Line('APRU')
	charts1.add(str(numlist)+"的APRU",list3,list7)
	page.add(charts1)
	# page.add(charts2)
	# page.add(charts3)
	return page
# def improve3(df):
def create_iprv3_charts(df):
	page=Page()
	list3 = coltype_filter(df,'账期')
	list3.sort()
	n=len(list3)
	v1 = [x for x in range(0,n)]
	for i in range(0,n):
		df_new = df[df['账期']==list3[i]]
		yearIncome=month_Chuzhang(df_new)
		v1[i]=yearIncome
	# monthIncome = yearIncome/n
	list5 = All_DOU(df)
	list6 = all_MOU(df)
	list7 = all_APRU(df)
	page =Page()
	v2=[x for x in range(0,n)]
	charts1 = Line("各月份比较")
	charts1.add('income',list3,v1)
	charts1.add("DOU",list3,list5)
	charts1.add("MOU",list3,list6)
	# charts3  =Line('APRU')
	charts1.add("APRU",list3,list7)
	page.add(charts1)
	# page.add(charts2)
	# page.add(charts3)
	return page
df = get_df_fromSQL('new1_data')
create_total_charts(df).render()
# a=1117090152471145
# print(type(a))
# sameUserDataframe(df,1117090152471145).render()
# create_iprv3_charts(df).render()
