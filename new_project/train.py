# -*- coding: utf-8 -*-
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.cross_validation import train_test_split
from sklearn.externals import joblib
import data_helper
import time,datetime


def train_task():
	#load train data
	train_X_data,train_y_data=data_helper.data_loader()
	
	#split the train data and test data
	X_train, X_test, y_train, y_test = train_test_split(train_X_data, train_y_data, \
	test_size=0.25, random_state=33)

	# new model and train model
	GBR=GradientBoostingRegressor()
	GBR=GBR.fit(X_train, y_train)

	#save model
	joblib.dump(GBR, "train_model.m")

if __name__ == '__main__':
	flag=0
	now=datetime.datetime.now()
	target_time=datetime.datetime(2017,10,14,03,54,0)
	while True:
		now=datetime.datetime.now()
		if now==target_time:
			train_task()
			flag=1
		else:
			if flag==1:
				target_time=target_time+datetime.timedelta(days=1)
				flag=0
	
		
	
	
