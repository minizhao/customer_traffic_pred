# -*- coding: utf-8 -*-
import data_helper
from sklearn.externals import joblib
import time,datetime
import random
import pandas as pd
from flask import *

app = Flask(__name__)
# http://127.0.0.1:5000/analysis?function=traffic&storeId=5&hour=9,20&daySpan=2017-09-20,2017-9-25
@app.route('/analysis/', methods=['GET'])


def analyse():

	time_point = [int(x) for x in str(request.args.get('hour')).split(',') ] #预测几点
	dates = str(request.args.get('daySpan')).split(',')  #预测几月到几月
	function = str(request.args.get('function'))
	storeId = int(str(request.args.get('storeId')))
	method=1  #method 0 or 1 ,method 0:精确预测，耗时多; method 1:历史数据预测，耗时少;

	d_start = datetime.date(*[int(x) for x in str(dates[0]).split('-')])
	d_end= datetime.date(*[int(x) for x in str(dates[-1]).split('-')])
	days_span=(d_end-d_start).days #差了几天
	
	df=pd.DataFrame()

	result_dic=dict()
	for i in range(days_span+1):
		d=d_start+datetime.timedelta(days=i)
		d_to_str=d.strftime('%Y-%m-%d')
		# print d_to_str
		for time in range(time_point[0],time_point[-1]+1):

			result,df=get_reslut(d_to_str,time,storeId,function,method,df)
			if method==1:
				radm=random.randint(0, 50)
				output=(result+radm)
			else:
				output=(result)
			result_dic[str(d_to_str)+','+str(time)]=str(int(output))

	resp = { "msg":"OK","code":0,"data": result_dic}
	return jsonify(resp)


def get_reslut(d_to_str,time,storeId,pred,method,df):

	args=dict()
	args['storeId']=storeId
	args['starttime']=time
	args['preds']=pred #人流客流特征参数 'traffic'/'customer'
	args['day']=d_to_str

	args_pref_features,df=data_helper.data_loader(train=False,args=args,method=method,df=df)
	model= joblib.load('train_model.m')
	return model.predict([args_pref_features]),df
	
'''
def run():

	date=['2017-08-10','2017-08-13']
	time_point=[9,22]
	storeId=3
	method=0  #method 0 or 1 ,method 0:精确预测，耗时多; method 1:历史数据预测，耗时少;

	d_start = datetime.date(*[int(x) for x in date[0].split('-')])
	d_end= datetime.date(*[int(x) for x in date[-1].split('-')])

	days_span=(d_end-d_start).days #差了几天

	df=pd.DataFrame()
	for i in range(days_span+1):
		d=d_start+datetime.timedelta(days=i)
		d_to_str=d.strftime('%Y-%m-%d')
		# print d_to_str
		for time in range(time_point[0],time_point[-1]+1):
			output=[]
			for pred in ['traffic','customer']:
				result,df=get_reslut(d_to_str,time,storeId,pred,method,df)
				if method==1:
					radm=random.randint(0, 50)
					output.append(result+radm)
				else:
					output.append(result)
			print d_to_str,time,[int(x) for x in output]
'''




if __name__ == '__main__':

	app.run(debug=True)

