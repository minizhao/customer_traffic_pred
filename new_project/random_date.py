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
	
	pred=[]

	x=np.linspace(0,4*np.pi,len(days_points)*24)
	y=np.sin(x)

	for x in range(1,len(days_points)+1):
		temp=[]
		for _ in range(0,24):

			radm1=random.randint(0, 10)
			radm2=random.randint(0, 10)
			temp.append('['+str(int(abs(math.cos(radm1*x)*5000)))+','+str(int(abs(math.cos(radm2*x)*400)))+']')
		
		pred.append(temp)
	# result=zip(days_points,pred1,pred2)
	df=pd.DataFrame()
	df['days_points']=days_points
	df["preds"]=pred
	return df

def insert_data(day):
	
	conn = mysql.connector.connect(user='root',password='123456',host='127.0.0.1',port='3306',\
		database='zdb_udc')
	cursor = conn.cursor()

	# days=['2017-08-04','2017-08-05','2017-08-06','2017-08-07','2017-08-08','2017-08-09']
	storeid=['0001','0002','0003','0004','0005','0006','0007']
	i=0
	for sid in storeid:
		df=get_random_value(days)
		for index, row in df.iterrows():
			cursor.execute("insert into zt_traffic_prediction values('"+str(i)+"','"+sid+"','"+str(row['days_points'])+"','"+','.join(row['preds'])+"')")
			i+=1
	conn.commit()
	cursor.close()
   	# conn.close()


if __name__ == '__main__':
		
	# d_start = datetime.date(2017,9,5)
	# d_end= datetime.date(2017,9,20)
	# days_span=(d_end-d_start).days
	# days=[]
	# for i in range(days_span+1):
	# 	d=d_start+datetime.timedelta(days=i)
	# 	d_to_str=d.strftime('%Y-%m-%d')	
	# 	days.append(d_to_str)

	# # df=get_random_value(days)
	# insert_data(days)
	# for i in np.linspace(0,4*np.pi,100):
	# 	print math.cos(i)
	x=np.linspace(0,4*np.pi,100)
	y=np.sin(x)
	# plt.plot(x,math.sin(x))
	plt.plot(x,y,label="$sin(x)$",color="red",linewidth=2)

	plt.show()

	# print df 
	# for index, row in df.iterrows():
	# 	print len(row['preds'])
	# 	print ','.join(row['preds'])
	
	
	# # storeid=['0001','0002','0003','0004','0005','0006','0007']
	# # for id in storeid:
	# insert_data(days_points)
