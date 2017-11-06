# -*- coding: utf-8 -*-
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.cross_validation import train_test_split
from sklearn.externals import joblib
import data_helper
import logging
import time,datetime
import pickle as pkl


logger = logging.getLogger("train")
logger.setLevel(logging.DEBUG)
fomatter = logging.Formatter('%(asctime)s -%(filename)s-line:%(lineno)d-%(levelname)s-%(module)s:%(message)s')
today=datetime.date.today()
fh = logging.FileHandler('/export/Logs/udc-forecast/info.'+str(today)+'.log')
fh = logging.FileHandler('info.'+str(today)+'.log')
fh.setLevel(logging.INFO)
fh.setFormatter(fomatter)
logger.addHandler(fh)


def train_task():
	#load train data
	try :
		train_X_data,train_y_data,storeId=data_helper.data_loader()
	except BaseException as e:
		logger.error(e)

	#保存下来所有店铺id
	pkl.dump(storeId, open('storeId.pkl','wb'))

	#train model
	try :
		GBR=GradientBoostingRegressor()
		GBR=GBR.fit(train_X_data, train_y_data)
	except BaseException as e:
		logger.error(e)

	#save model
	joblib.dump(GBR, "train_model.m")

if __name__ == '__main__':

	flag=0
	target_time = datetime.datetime(2017, 11, 6, 18, 10, 0)

	while True:
		now=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		tar_time_str=target_time.strftime('%Y-%m-%d %H:%M:%S')
		if now==tar_time_str:
			train_task()
			logger.info('train done')
			flag=1
		else:
			if flag==1:
				target_time=target_time+datetime.timedelta(days=1)
				logger.info('reset train time')
				flag=0
	
