# -*- coding: utf-8 -*-
import data_helper
from sklearn.externals import joblib
import time,datetime

def get_reslut(d_to_str,time,storeId,pred):

	args=dict()
	args['storeId']=storeId
	args['starttime']=time
	args['preds']=pred #人流客流特征参数 'traffic'/'customer'
	args['day']=d_to_str


	args_pref_features=data_helper.data_loader(train=False,args=args)
	model= joblib.load('train_model.m')
	return model.predict([args_pref_features])



def run():

	date=['2017-08-10']
	time_point=[5,9]
	storeId=3

	d_start = datetime.date(*[int(x) for x in date[0].split('-')])
	d_end= datetime.date(*[int(x) for x in date[1].split('-')])

	days_span=(d_end-d_start).days #差了几天

	for i in range(days_span+1):
		d=d_start+datetime.timedelta(days=i)
		d_to_str=d.strftime('%Y-%m-%d')
		# print d_to_str
		for time in range(time_point[0],time_point[-1]+1):
			output=[]
			for pred in ['traffic','customer']:
				result=get_reslut(d_to_str,time,storeId,pred)
				output.append(result)
			print d_to_str,time,[int(x) for x in output]


		

		# for time in time_point:



	


if __name__ == '__main__':
	run()
