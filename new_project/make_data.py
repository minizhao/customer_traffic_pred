# -*- coding: utf-8 -*-
import time,datetime
import math
import random
import pandas as pd
import mysql.connector
import numpy as np
# import pylab as pl
import matplotlib.pyplot as plt

def get_random_value(days_points):
	num_list=get_timepoint_value()
	pred=[]

	for x in range(1,len(days_points)+1):
		temp=[]
		#下面的num只是客流
		for day,num in num_list:

			radm1=np.random.randint(0, 50)
			num=num+radm1
			radm2=np.random.uniform(4.8,5.3) 
			temp.append('['+str(int(num*radm2))+','+str(num)+']')
		
		pred.append(temp)
	# result=zip(days_points,pred1,pred2)
	df=pd.DataFrame()
	df['days_points']=days_points
	df["preds"]=pred
	return  df


def get_timepoint_value():
	df=pd.read_csv('1.txt')
	time=sorted(df['start'].drop_duplicates())	
	time_point=[]
	time_point_num=[] #这里仅仅是客流
	for t in time:
		time_point.append(t)
		time_point_num.append(int(np.mean(df[df['start']==t]['number'])))
	return zip(time_point,time_point_num)


def insert_data(days):
	
	conn = mysql.connector.connect(user='root',password='123456',host='127.0.0.1',port='3306',\
		database='zdb_udc')
	cursor = conn.cursor()

	# days=['2017-08-04','2017-08-05','2017-08-06','2017-08-07','2017-08-08','2017-08-09']
	storeid=['731888568958976','760356912054273','730065587716096','760258552217601','755999991742465',\
			'730384208216065','728673949859840']
	i=0
	for sid in storeid:
		df=get_random_value(days)
		for index, row in df.iterrows():
			cursor.execute("insert into zt_traffic_prediction values('"+str(i)+"','"+sid+"','"+str(row['days_points'])+"','"+','.join(row['preds'])+"')")
			i+=1
	conn.commit()
	cursor.close()



if __name__ == '__main__':
		
	d_start = datetime.date(2017,9,5)
	d_end= datetime.date(2017,9,20)
	days_span=(d_end-d_start).days
	days=[]
	for i in range(days_span+1):
		d=d_start+datetime.timedelta(days=i)
		d_to_str=d.strftime('%Y-%m-%d')	
		days.append(d_to_str)
	insert_data(days)

