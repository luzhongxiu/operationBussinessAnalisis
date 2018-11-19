#coding=utf-8 
from import_mysql import *
import numpy as np
import pandas as pd
# 获取表头
def get_headers(dataframe):
	# ncols = dataframe.shape[1]
	list_head = [column for column in dataframe]
	# print(list_head)
	return list_head
# 接收前端传过来的数据，生成list_newhead
'''def get_newhead():
	return list_newhead'''

# 筛选表头，返回自己筛选的表头
def type_filter(list_newhead,list_head):
	tmp = [val for val in list_newhead if val in list_head]
	# print(tmp)
	return tmp
# 用新表头生成dataframe
def new_dataframe(dataframe,list_newhead):
	df_new = dataframe[list_newhead]
	# print(df_new)
	return df_new

# ---------------筛选功能----------------#
# 特定年份月份筛选
def date_filter(dataframe,year,month):
	df = dataframe[(dataframe['账期']==int(year + month))]
	# print(df)
	return df
# 一段时间内筛选
def duringdate_filter(data,yearlow,monthlow,yearTop,monthtop):
	print("to be done")
	pass
# 特定用户标识筛选
def userID_filter(dataframe,userID):
	df= dataframe[dataframe['用户标识']==int(userID)]
	# print(df)
	return df 
# 特定号码筛选
def phoneNum_filter(dataframe,phoneNum):
	df= dataframe[dataframe['用户号码']==int(phoneNum)]
	# print(df)
	return df 
# 通话次数筛选
def callNum_filter(dataframe,lowNum,TopNum):
	df = dataframe[(dataframe['通话次数']>=lowNum) & (dataframe['通话次数']<=TopNum) ]
	# print(df)
	return df
# 不同套餐类型筛选
def plantype_filter(dataframe,list_newType):
	list_Type=['1元日租卡国际版', '36元套餐', '3元不限量卡', '56元套餐', '96元套餐', 'JJ春天卡', 'JJ地主卡', 'JJ王炸卡', 'MINI橙卡', 'O粉卡', 'O粉卡畅聊版', 'RIO任性卡19元套餐', 'RIO任性卡59元套餐', 'V粉卡（9元版）', 'V粉卡（升级版）', '阿里YunOS云游-46元卡', '阿里YunOS云游-9元卡', '阿里宝卡亲情卡', '阿里大宝卡', '阿里钉钉商务金卡', '阿里钉钉商务银卡', '阿里钉钉商务钻石卡', '阿里小宝卡', '百度超圣卡', '百度大神卡', '百度大圣卡', '百度女神卡', '百度天圣卡', '百度天圣卡 plus', '百度小神卡', '百度小圣卡', '帮帮卡', '菜鸟大宝卡（新）', '菜鸟小宝卡（新）', '畅爽卡', '畅淘卡', '超白金卡', '大e卡', '大白金卡', '大橙卡', '大程卡', '大地1元日租卡', '大帝卡', '大丰卡', '大怪卡', '大花椒卡', '大黄卡', '大酷卡', '大满卡', '大民卡', '大摩王卡', '大糯卡', '大神盾卡', '大顺卡', '大铁卡', '大歪卡', '大蜗牛卡', '大夏卡', '大逸听卡', '大映卡', '大猪卡', '导学易学卡29元套餐', '导学易学卡69元套餐', '导学易学卡99元套餐', '滴滴大王卡', '滴滴王卡MINI版', '滴滴小王卡', '地王卡', '钉钉大宝卡', '钉钉卡-商务银卡个性化套餐（线下）', '钉钉小宝卡', '懂我卡', '懂我卡mini', '懂我卡plus', '饿了么大饿卡', '饿了么小饿卡', '蜂鸟卡', '蜂王卡', '副卡', '国民卡19元套餐', '国民卡19元套餐-伊利', '国民卡59元套餐', '国民卡59元套餐-伊利', '国民卡89元套餐', '国寿精英卡19元套餐', '国寿精英卡39元套餐', '国寿精英卡98元套餐', '国寿专享卡19元档', '国寿专享卡39元档', '国王卡', '花粉卡', '惠民卡', '金粉卡', '金享卡19元套餐', '京东大强卡', '京东小强卡', '凯旋将士卡', '凯旋卫士卡', '口粮零食卡', '联通国民卡19元套餐', '联通国民卡89元套餐', '连尚万能白金卡', '连尚万能金卡', '流邦卡29元套餐', '流邦卡69元套餐', '流邦卡99元套餐', '蚂蚁宝卡亲情卡', '蚂蚁大宝卡', '蚂蚁国宝卡', '蚂蚁小宝+卡', '蚂蚁小宝卡', '芒果大芒卡', '芒果小芒卡', '美团大美卡', '美团小美卡', '梦想e卡', '米粉卡29元套餐', '米粉卡59元套餐', '米粉卡Plus（35元卡）', '米粉卡（5元卡）', '女王加冕卡', '普惠e卡', '普惠e卡和合版', '亲情卡', '青啤无限畅爽卡（35元卡）', '青啤无限畅爽卡（5元卡）', '软易金钻卡', '软易小钻卡', '顺丰速运巴枪卡49元套餐', '丝芭畅享卡', '丝芭乐享卡', '腾讯大王卡', '腾讯视频小王卡', '腾讯天王卡', '腾讯音乐小王卡', '天顺卡', '微博V+卡', '微博V卡', '微博大V卡', '微博金V卡', '小白金卡', '小贝壳卡', '小橙卡', '小程卡', '小怪卡', '小花椒卡', '小黄卡', '小酷卡', '小满卡', '小满卡（i-Fi专属）', '小民卡', '小摩王卡', '小糯卡', '小神盾卡', '小顺卡', '小歪卡', '小蜗牛卡', '小沃PLUS卡19元套餐', '小夏卡', '小逸听卡', '小映卡', '小圆卡', '小猪卡', '携程冰激凌卡', '星粉卡', '星粉卡(5元卡)', '星粉卡Plus（35元卡）', '星芒卡', '用友王卡', '圆卡', '约创卡19元档', '招联牛卡', '招行大招卡', '招行小招卡', '知卡', '知卡 Plus', '中铁e卡', '中铁e卡plus', '中通快递大卡', '中通快递王卡', '中通快递小卡', '哔哩哔哩22卡', '哔哩哔哩33卡', '哔哩哔哩小电视卡', '魅友1元日租卡', '魅友3元不限量卡']
	list_newType = [val for val in list_Type if val in list_newType]
	typeNumber = len(list_newType)
	for i in range(0,typeNumber):
			df_new = df_new.append(dataframe[dataframe['套餐类型']==list_newType[i]],ignore_index=False)
	# df = dataframe[dataframe['套餐类型'==str(planType)]]
	# print(df_new)
	return df_new
#计费时长筛选
def callNum_filter(dataframe,lowNum,TopNum):
	df = dataframe[(dataframe['计费时长']>=lowNum) & (dataframe['计费时长']<=TopNum) ]
	# print(df)):
	if i==0:
		df_new = dataframe[dataframe['套餐类型']==list_newType[i]]
	return df
#流量筛选
def dataflow_filter(dataframe,lowNum,TopNum):
	df = dataframe[(dataframe['流量']>=lowNum) & (dataframe['流量']<=TopNum) ]
	print(df)
	return df
# 生成list table需要的
def np2list(dataframe):
	nparray = np.array(dataframe)
	list1 = nparray.tolist()
	list0 = get_headers(dataframe)
	list1.insert(0,list0)
	return list1
# def insert_tolist(dataframe):
# 	np2list(dataframe)
# 筛选类型数 生成list
# def list2df(list,string)
	
def coltype_filter(dataframe,colName):
	nrows = dataframe.shape[0]
	ncols = dataframe.shape[1]
	# list = []
	# for i in range(0,nrows):
	df_new = dataframe[colName]
	df_new = df_new.drop_duplicates(keep='first')
	# print(df_new)
	nparray = np.array(df_new)
	list1 = nparray.tolist()
	return list1
def typecol_tolist(dataframe,colName):
	nrows = dataframe.shape[0]
	list1=[]
	for i in range(0,nrows):
		list1.append(str(dataframe.loc[i,colName]))
		print(list1)
	return list1
def info_filter(df,colName_list):
	df_new1 = df[colName_list]
	return df_new1

def detailed_info_filter(dataframe,colName,listtypeNeed):
	list = coltype_filter(dataframe,colName)
	typeNum = len(list)
	# typeneedNum = len(listtypeNeed)
	# df_new = pd.DataFrame(columns=get_headers(dataframe))
	df_new = dataframe.drop(dataframe.index)
	for i in range(0,len(listtypeNeed)):
		# if listtypeNeed[i] in list:
		df_new = df_new.append(dataframe[dataframe[colName]==listtypeNeed[i]],ignore_index=True)
		# else:df_new1 = df_new1.append(dataframe[dataframe[listtypeNeed[i]]],ignore_index=True)
	# df = dataframe[dataframe['套餐类型'==str(planType)]]
	# print(df_new)
	return df_new

# df = get_df_fromSQL("new_data")
# df_new = info_filter(df,['账期','用户号码'])
# print(df_new)
# a=df[['流量','用户号码']]
# print(a)
# nparray = np.array(df)
# list1= nparray.tolist()
# print(list1)
# list0 = get_headers(df)
# list1.insert(0,list0)
# print(list1)

# # print(nparray.tolist())
# list0.append(nparray.tolist)
# # a = detailed_info_filter(df,'套餐类型',['地王卡','亲情卡'])
# # print(a)
# list1 = np2list(df)
# print(list1)

# list1 = typecol_tolist(df,)
# list_newhead=['流量','账期','用户号码','归属部门名称']
# list_head = get_headers(df)
# temp = type_filter(list_head,list_newhead)
# print(temp)
# head = get_headers(df)
# print(head)
# list=coltype_filter(df,'套餐类型')

# v1=[x for x in range(0,10)]
# print(v1)
# print(df)
# list1= typecol_tolist(df,'流量')
# print(list1)
# print(df)
# list =['121','100']
# df1=detailed_info_filter(df,'addr',list)


#合并同样客户, 
# def user_combine(dataframe)
# 	df = dataframe.groupby

# df=excelRead('D:/code/finalexam/data/ori_data.xlsx')

# list_head = get_headers(df)
# list_newhead = ['账期','用户标识','用户号码']
# list_newhead = type_filter(list_newhead,list_head)
# print(new_dataframe(df,list_newhead))

# userID_filter(df,1117070697142278)
# callNum_filter(df,40,100)
# list_newType=['普惠e卡','亲情卡']
# plantype_filter(df,list_newType)
# dataflow_filter(df,10240,15360)
# yearincome_filter(df)


# print(len(list))
# list = get_headers(df)
# print(list)

# list1=type_filter(df,'套餐类型')
# print(list1)
# list = [[1,'2','3'],'string',3]
# print(list)

# def list2table(dataframe,ori_list):
# 	nrows = dataframe.shape[0]
# 	ncols = dataframe.shape[1]
# 	list = []
# 	list_new = [0]
# 	for i in range(0,nrows):
# 		for j in range(0,ncols):
# 			# print((i*n=ncols)+j)
# 			n=i*ncols+j
# 			print(n)
# 			ori_list
# 			# items = ori_list[]
# 			# # list.append(items)
# 			# print(items)
# 		# list_new[i]= list
# 		# list=[]

# 	return list_new


# print(df)
# list = np2list(df)
# # print(list)
# # def fill_table():
# # 	list = np2list(dataframe)
# # 	for i in range(0,talbe_row):
# # 		for j in range(0,table_column):
# # 			list_new = list[i]
# # 			table[i][j]=list_new[j]
# # 	return 0

# # list=[[1,2,3],22,33]
# # print(list[0][2])

# for i in range(0,len(list)):
# 	for j in range(0,len(list[i])):
# 		items = list[i][j]



# df = get_df_fromSQL()



