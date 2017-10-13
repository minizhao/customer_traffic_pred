# -*- coding: utf-8 -*-
import data_helper
from sklearn.externals import joblib


def run():
	args=dict()
	args['storeId']=5
	args['starttime']=11
	args['preds']='customer' #人流客流特征参数 'traffic'/'customer'
	args['day']='2017-08-08'
	args_pref_features=data_helper.data_loader(train=False,args=args)
	model= joblib.load('train_model.m')
	print model.predict([args_pref_features])




if __name__ == '__main__':
	run()
