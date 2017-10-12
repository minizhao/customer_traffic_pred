import pandas as pd
import numpy as np
import time,datetime

from sklearn.ensemble import GradientBoostingRegressor
from sklearn.cross_validation import train_test_split

def data_loader():

	train_x=[]
	train_y=[]


	df=pd.read_csv('1.txt',sep=',')
	date=df['date'].drop_duplicates() # all day date in the dataset

	target_times=range(9,23)# predict target hours value 

	for da in date:
		# da: one day ,2017-08-05,...
		sub_df=df[df['date']==da]
		all_time=sub_df['start'] # this day all hour value

		time_available=list(map(lambda x:judge(x,all_time) ,target_times))
		time_available=[x for x in time_available if x !=None]	

		


		for t in time_available:	
			# t is one hours value 
			time_f=time_feature(df,da,t)	# hours feature
			three_hours_f,pred_target=three_hours_feature(sub_df,t) # three hours before feature
			week_f=week_feature(da)	# week feature
			
			# all feature dims 16:x1,x2....x16
			result_f=np.concatenate((time_f, three_hours_f,week_f)).astype(float)
			# pred_target  :y
			train_x.append(result_f)
			train_y.append(pred_target)

	assert len(train_x)==len(train_y)
	return train_x,train_y




def judge(tar_time,all_time):
	tar_list=[tar_time,tar_time-1,tar_time-2,tar_time-3]
	if len(set(tar_list).difference(set(all_time)))==0:
		return tar_time




def time_feature(df,da,t):
	sub_df_befor=df[np.logical_and(df['date']<=da,df['start']==t)]
	bumber_list=sub_df_befor['number']

	mean_=np.mean(bumber_list)
	var_=np.var(bumber_list)
	mediam_=np.median(bumber_list)
	percentile_25=np.percentile(bumber_list,25)
	percentile_75=np.percentile(bumber_list,75)

	return [mean_,var_,mediam_,percentile_25,percentile_75]


def three_hours_feature(sub_df,tar_time):
	tar_list=[tar_time,tar_time-1,tar_time-2,tar_time-3]
	num_list=[]
	for h in tar_list:
		sub_data=sub_df[sub_df['start']==h]
		assert sub_data.shape[0]==1
		num_list.append(sub_data['number'].tolist()[0])
	
	result=[np.mean(num_list[1:]),float((num_list[2]-num_list[1]))/num_list[1],\
			float((num_list[3]-num_list[2]))/num_list[2]]
	return result,num_list[0]




def week_feature(da):
	da_int_list=[int(x) for x in da.split('-')]
	day = datetime.datetime(*da_int_list).weekday()
	one_hot=np.zeros(7)
	one_hot[day]=1.0
	return one_hot
	

	
	


if __name__ == '__main__':
	#load train data
	train_X_data,train_y_data=data_loader()
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
