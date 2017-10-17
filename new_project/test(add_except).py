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
	
	error='ok'
	print request.args.get('hour')
	try:
		time_point = [int(x) for x in str(request.args.get('hour')).split(',') ] #预测几点
	except ValueError as e:
	 	error = "Incorrect input data <hour>: "
	 	error+=( ': '+str(e)  )
		resp = { "msg":error,"code":1,"data": None}
		return jsonify(resp)

	try:
		dates = str(request.args.get('daySpan')).split(',')  #预测几月到几月
	except ValueError as e:
	 	error = "Incorrect input data <dates>: "
	 	error+=( ': '+str(e)  )
		resp = { "msg":error,"code":1,"data": None}
		return jsonify(resp)

	try:
		function = str(request.args.get('function'))

	except ValueError as e:
	 	error = "Incorrect input data <function>: "
	 	error+=( ': '+str(e)  )
		resp = { "msg":error,"code":1,"data": None}
		return jsonify(resp)

	try:
		storeId = int(str(request.args.get('storeId')))

	except ValueError as e:
	 	error = "Incorrect input data <storeId>: "
	 	error+=( ': '+str(e)  )
		resp = { "msg":error,"code":1,"data": None}
		return jsonify(resp)

	if time_point == None or dates == None or function== None or storeId== None:
		error = "Missing input data: "
		resp = { "msg":error,"code":1,"data": None}
		return jsonify(resp)

	if function not in ['traffic','customer']:
		error = "Incorrect parameter input <function>: "
		resp = { "msg":error,"code":1,"data": None}
		return jsonify(resp)

	if function not in ['traffic','customer']:
		error = "Incorrect parameter input <function>: "
		resp = { "msg":error,"code":1,"data": None}
		return jsonify(resp)

	
	# method=1  #method 0 or 1 ,method 0:精确预测，耗时多; method 1:历史数据预测，耗时少;
	try:
		d_start = datetime.date(*[int(x) for x in str(dates[0]).split('-')])
		d_end= datetime.date(*[int(x) for x in str(dates[-1]).split('-')])
	except ValueError as e:
	 	error = "Incorrect input data : "
	 	error+=( ': '+str(e)  )
		resp = { "msg":error,"code":1,"data": None}
		return jsonify(resp)

	if d_start>d_end:
		error = "Incorrect parameter input <dates> :The start date must be before the end date: "
		resp = { "msg":error,"code":1,"data": None}
		return jsonify(resp)

	days_span=(d_end-d_start).days #差了几天
	
	# df=pd.DataFrame()

	result_dic=dict()
	for i in range(days_span+1):
		d=d_start+datetime.timedelta(days=i)
		d_to_str=d.strftime('%Y-%m-%d')
		# print d_to_str
		for time in range(time_point[0],time_point[-1]+1):

			result=get_reslut(d_to_str,time,storeId,function)
		
			radm=random.randint(0, 50)
			output=(result+radm)

			result_dic[str(d_to_str)+','+str(time)]=str(int(output))

	resp = { "msg":error,"code":0,"data": result_dic}
	return jsonify(resp)


def get_reslut(d_to_str,time,storeId,pred):

	args=dict()
	args['storeId']=storeId
	args['starttime']=time
	args['preds']=pred #人流客流特征参数 'traffic'/'customer'
	args['day']=d_to_str

	args_pref_features=data_helper.data_loader(train=False,args=args)
	model= joblib.load('train_model.m')
	return model.predict([args_pref_features])
	




if __name__ == '__main__':

	app.run(host='0.0.0.0')
