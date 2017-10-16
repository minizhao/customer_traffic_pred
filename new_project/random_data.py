# -*- coding: utf-8 -*-
import time,datetime
import math
import random
import pandas as pd

def get_random_value(days_points):
	radm1=random.randint(0, 10)
	radm2=random.randint(0, 10)
	pred1=[]
	pred2=[]
	for x in range(1,len(days_points)+1):
		# print 
		pred1.append(int(abs(math.cos(radm1*x)*1000)))
		pred2.append(int(abs(math.cos(radm2*x)*1000)))

	# result=zip(days_points,pred1,pred2)
	df=pd.DataFrame()
	df['days_points']=days_points
	df['pred1']=pred1
	df['pred2']=pred2
	print df

if __name__ == '__main__':
		
	d_start = datetime.date(2017,9,5)
	d_end= datetime.date(2017,9,20)
	days_span=(d_end-d_start).days #差了几天
	days_points=[]
	for i in range(days_span+1):
		d=d_start+datetime.timedelta(days=i)
		d_to_str=d.strftime('%Y-%m-%d')	
		for time in range(0,24):
			days_points.append(d_to_str+','+str(time))
	simulation_data=get_random_value(days_points)
