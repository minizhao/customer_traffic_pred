# -*- coding: utf-8 -*-
import mysql.connector
import pandas as pd
import numpy as np
import re
import datetime
import time
import time,datetime
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.cross_validation import train_test_split

def str_to_list(str_=''):
		rr = re.compile(r'[\d]+,[\d]+')
		match_list=rr.findall(str_)
		result=list(map(lambda x : x.split(','),match_list))
		return result

def data_sql_helper():
	conn = mysql.connector.connect(user='root',password=' ',host='127.0.0.1',port='3306',\
		database='zdb_udc')
	cursor = conn.cursor()
	count = cursor.execute('select * from zt_traffic_prediction')

	results = cursor.fetchall()
	df_dataset=pd.DataFrame(columns=['storeId','day','preds1','preds2','starttime']) #总数据表

	preds_data=[]
	storeid_data=[]
	days_data=[]
	starttime_data=[]

	for record in results:
		index,storeid,day,preds=record

		preds=preds.decode('utf-8')
		preds_list=(str_to_list(preds))

		row_num=len(preds_list)

		preds_data.extend(preds_list)
		storeid_data.extend([storeid]*row_num)
		day=day.strftime('%Y-%m-%d')
		days_data.extend([day]*row_num)
		starttime_data.extend(range(0,24))
		
	preds_data=np.array(preds_data)

	df_dataset['storeId']=storeid_data
	df_dataset['day']=days_data

	df_dataset['preds1']=preds_data[:,0]
	df_dataset['preds2']=preds_data[:,1]
	df_dataset['starttime']=starttime_data
	conn.close()

	return df_dataset


def data_loader(df=''):

	train_x=[]
	train_y=[]


	# df=pd.read_csv('1.txt',sep=',')
	days=df['day'].drop_duplicates() # all day date in the dataset
	storeId=df['storeId'].drop_duplicates() # all day date in the dataset
	predict_values=['traffic','customer']

	target_times=range(9,23)# predict target hours value 

	for store in storeId:
		for it in predict_values:
			for da in days:
				# da: one day ,2017-08-05,...
				sub_df=df[np.logical_and(df['day']==da,df['storeId']==store)]

				all_time=sub_df['starttime'] # this day and store all hour value

				time_available=list(map(lambda x:judge(x,all_time) ,target_times))
				time_available=[x for x in time_available if x !=None]	

				for t in time_available:	
					# t is one hours value 
					time_f=time_feature(df,da,t,store,it)	# hours feature
					three_hours_f,pred_target=three_hours_feature(sub_df,t,store,it) # three hours before feature
					week_f=week_feature(da)	# week feature
					store_f=store_feature(storeId,store)
					traffic_customer_f=traffic_customer_feature(it)
					# all feature dims 16:x1,x2....x16
					result_f=np.concatenate((time_f, three_hours_f,week_f,store_f,traffic_customer_f)).astype(float)
					# pred_target  :y
					train_x.append(result_f)
					train_y.append(pred_target)

	assert len(train_x)==len(train_y)
	return train_x,train_y




def judge(tar_time,all_time):
	tar_list=[tar_time,tar_time-1,tar_time-2,tar_time-3]
	if len(set(tar_list).difference(set(all_time)))==0:
		return tar_time




def time_feature(df,da,t,store,it):
	sub_df_befor=df[np.logical_and(df['day']<=da,df['starttime']==t)]
	sub_df_befor=sub_df_befor[df['storeId']==store]
	if it=='traffic':
		bumber_list=np.array(sub_df_befor['preds1'].tolist()).astype(float)
	elif it=='customer':
		bumber_list=np.array(sub_df_befor['preds2'].tolist()).astype(float)
	mean_=np.mean(bumber_list)
	var_=np.var(bumber_list)
	mediam_=np.median(bumber_list)
	percentile_25=np.percentile(bumber_list,25)
	percentile_75=np.percentile(bumber_list,75)

	return [mean_,var_,mediam_,percentile_25,percentile_75]


def three_hours_feature(sub_df,tar_time,store,it):
	tar_list=[tar_time,tar_time-1,tar_time-2,tar_time-3]
	num_list=[]
	for h in tar_list:
		sub_data=sub_df[np.logical_and(sub_df['starttime']==h,sub_df['storeId']==store)]
		assert sub_data.shape[0]==1
		if it=='traffic':
			num_list.append(sub_data['preds1'].tolist()[0])
		elif it=='customer':
			num_list.append(sub_data['preds2'].tolist()[0])


	num_list=np.array(num_list).astype(float)
	result=[np.mean(num_list[1:]),float((num_list[2]-num_list[1]))/(num_list[1]+1),\
			float((num_list[3]-num_list[2]))/(num_list[2]+1)]
	return result,num_list[0]




def week_feature(da):
	da_int_list=[int(x) for x in da.split('-')]
	day = datetime.datetime(*da_int_list).weekday()
	one_hot=np.zeros(7)
	one_hot[day]=1.0
	return one_hot
	

def store_feature(storeId,store):
	zero_enc=np.zeros(len(storeId)).tolist()
	zero_enc[storeId.tolist().index(store)]=1
	return zero_enc

def traffic_customer_feature(it):
	if it=='traffic' :
		return [1,0]
	elif it=='customer':
		return [0,1]


if __name__ == '__main__':
	#load train data
	df=data_sql_helper()
	# print df
	train_X_data,train_y_data=data_loader(df)
	

	X_train, X_test, y_train, y_test = train_test_split(train_X_data, train_y_data, \
	test_size=0.25, random_state=33)

	# load model and train model
	GBR=GradientBoostingRegressor()
	GBR=GBR.fit(X_train, y_train)
	pred=GBR.predict(X_test) 

	#test the model score
	result=zip(y_test,pred)
	print "real_value\tpred_value"
	for real_value,pred_value in result:
		print real_value,'\t',pred_value

	print ("GBR train score is {}".format(GBR.score(X_test, y_test)))
	
