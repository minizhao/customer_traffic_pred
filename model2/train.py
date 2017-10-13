# -*- coding: utf-8 -*-
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.cross_validation import train_test_split
from sklearn.externals import joblib
import data_helper
# update mysql.user set authentication_string=password("123456") where user="root";
# UPDATE mysql.user SET Password=PASSWORD("123456")  WHERE User='root' and Host='localhost';


if __name__ == '__main__':
	#load train data
	# df=data_helper.data_loader()
	# print df
	train_X_data,train_y_data=data_helper.data_loader()
	
	#split the train data and test data
	X_train, X_test, y_train, y_test = train_test_split(train_X_data, train_y_data, \
	test_size=0.25, random_state=33)

	# new model and train model
	GBR=GradientBoostingRegressor()
	GBR=GBR.fit(X_train, y_train)

	#save model
	joblib.dump(GBR, "train_model.m")

	pred=GBR.predict(X_test) 

	#test the model score
	result=zip(y_test,pred)
	print "real_value\tpred_value"
	for real_value,pred_value in result:
		print real_value,'\t',pred_value

	print ("GBR train score is {}".format(GBR.score(X_test, y_test)))
	
