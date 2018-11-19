#coding=utf-8
from import_mysql import excelRead
from import_mysql import get_df_fromSQL
from headerAndtypes import *
import math
 # 月出账费用 空
def month_Chuzhang(dataframe):
	df = dataframe[['出帐费用']]
	df3 = df.copy()
	df3.loc['Row_sum'] = df3.apply(lambda x: x.sum())
	a=int(df3.loc['Row_sum'])
	# print(sum)
	return a
# 年累计收入
def yearincome_filter(dataframe):
	df = dataframe[['年累计收入']]
	df3 = df.copy()
	df3.loc['Row_sum'] = df3.apply(lambda x: x.sum())
	a=int(df3.loc['Row_sum'])
	# print(sum)
	return a
# APRU 平均
def APRU_Chuzhang(dataframe):
	nrows = dataframe.shape[0]
	sum = month_Chuzhang(dataframe)
	sum = sum/nrows
	# print(sum)
	return sum
def all_APRU(dataframe):
	list1=coltype_filter(dataframe,'账期')
	# print(list1)
	list1.sort()
	list2 =[]
	for i in range(0,len(list1)):
		df_new = dataframe.loc[dataframe['账期']==list1[i]]
		nrows = dataframe.shape[0]
		sum = 0
		df = df_new[['出帐费用']]
		df3 = df.copy()
		df3.loc['Row_sum'] = df3.apply(lambda x: x.sum())
		a=float(df3.loc['Row_sum'])
		a=float(a/nrows)
		list2.append(a)
	return list2
# 平均每月通话时间
def MOU(dataframe):
	nrows = dataframe.shape[0]
	sum = 0
	df = dataframe[['计费时长']]
	df3 = df.copy()
	df3.loc['Row_sum'] = df3.apply(lambda x: x.sum())
	a=int(df3.loc['Row_sum'])
	a=int(a/nrows)
	# print(df)
	# print(sum)
	return a
def all_MOU(dataframe):
	list1=coltype_filter(dataframe,'账期')
	# print(list1)
	list1.sort()
	list2 =[]
	for i in range(0,len(list1)):
		df_new = dataframe.loc[dataframe['账期']==list1[i]]
		nrows = dataframe.shape[0]
		sum = 0
		df = df_new[['计费时长']]
		df3 = df.copy()
		df3.loc['Row_sum'] = df3.apply(lambda x: x.sum())
		a=int(df3.loc['Row_sum'])
		a=int(a/nrows)
		list2.append(a)
	return list2
# 每月平均使用流量
def DOU(dataframe):
	nrows = dataframe.shape[0]
	sum = 0
	df = dataframe[['流量']]
	df3 = df.copy()
	df3.loc['Row_sum'] = df3.apply(lambda x: x.sum())
	a=float(df3.loc['Row_sum'])
	a=float(a/nrows)
	# print(sum)
	return a
def All_DOU(dataframe):
	list1=coltype_filter(dataframe,'账期')
	# print(list1)
	list1.sort()
	list2 =[]
	for i in range(0,len(list1)):
		df_new = dataframe.loc[dataframe['账期']==list1[i]]
		nrows = dataframe.shape[0]
		sum = 0
		df = df_new[['流量']]
		df3 = df.copy()
		df3.loc['Row_sum'] = df3.apply(lambda x: x.sum())
		a=int(df3.loc['Row_sum'])
		a=int(a/nrows)
		list2.append(a)
	return list2

df = get_df_fromSQL('new1_data')
a = All_DOU(df)
print(a)


# df=get_df_fromSQL('new1_data')
# print(All_DOU(df))
# print(MOU(df))
# df_new = df[df['账期'] == 201809]
# print(df_new)
# APRU_Chuzhang(df)
# DOU(df)

	# print(sum)
# for i in range(0,len(list))
# df_new=detailed_info_filter(df,'套餐类型',[Typelist[1]])
# list = get_headers(df_new)
# sum = month_Chuzhang(df_new)
# print(sum)
# df = get_df_fromSQL('ori_data')

# Typelist = coltype_filter(df,'套餐类型')
# # print(Typelist)
# sum = 0
# for i in range(0,len(Typelist)):
# 	df_new = detailed_info_filter(df,'套餐类型',[Typelist[i]])
# 	sum = month_Chuzhang(df_new)
	
