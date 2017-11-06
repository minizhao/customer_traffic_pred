# -*- coding: utf-8 -*-
import data_helper
from sklearn.externals import joblib
import time, datetime
import random
import pandas as pd
from flask import *
import logging
import numpy as np
import pickle as pkl

fomatter = logging.Formatter('%(asctime)s -%(filename)s-line:%(lineno)d-%(levelname)s-%(module)s:%(message)s')
today=datetime.date.today()
fh = logging.FileHandler('/export/Logs/udc-forecast/info.'+str(today)+'.log')
# fh = logging.FileHandler('info.'+str(today)+'.log')
fh.setLevel(logging.INFO)
fh.setFormatter(fomatter)

app = Flask(__name__)

# http://127.0.0.1:5000/analysis?function=traffic&storeId=731888568958976&hour=9-20&daySpan=2017-09-20,2017-9-25
@app.route('/analysis/', methods=['GET'])

def analyse():
    error = 'ok'
    np.random.seed(5)
    radm =np.random.randint(1,50,size=100)

    try:
        time_point = request.args.get('hour')  # 预测几点
        dates = request.args.get('daySpan')  # 预测几月到几月
        function = request.args.get('function')
        storeId = request.args.get('storeId')
        time_point = [int(x) for x in str(request.args.get('hour')).split('-')]  # 预测几点
        dates = str(request.args.get('daySpan')).split(',')  # 预测几月到几月
        function_ = str(request.args.get('function')).split(',')
        storeId = int(str(request.args.get('storeId')))
    
    except ValueError as e:
        error = "Incorrect input data : "
        resp = {"msg": error, "code": 1, "data": None}
        app.logger.warning(error)
        return jsonify(resp)

    if function_[0]  not in ['traffic', 'customer'] or function_[-1]  not in ['traffic', 'customer']:
        error = "Incorrect parameter input <function>"
        resp = {"msg": error, "code": 1, "data": None}
        app.logger.warning(error)
        return jsonify(resp)
    try:
        d_start = datetime.date(*[int(x) for x in str(dates[0]).split('-')])
        d_end = datetime.date(*[int(x) for x in str(dates[-1]).split('-')])
    except ValueError as e:
        error = "Incorrect input data : "
        resp = {"msg": error, "code": 1, "data": None}
        app.logger.warning(error)
        return jsonify(resp)

    if d_start > d_end:
        error = "Incorrect parameter input <dates> :The start date must be before the end date: "
        resp = {"msg": error, "code": 1, "data": None}
        app.logger.warning(error)
        return jsonify(resp)

    all_storeId=pkl.load(open('storeId.pkl', 'rb'))#加载店铺id
    if storeId not in all_storeId.values:
        error = "Incorrect parameter input <storeId> :unkown storeId: "
        resp = {"msg": error, "code": 1, "data": None}
        app.logger.warning(error)
        return jsonify(resp)

    days_span = (d_end - d_start).days  # 差了几天
    result_dic_traffic = dict()
    result_dic_customer= dict()
    try:
        model = joblib.load('train_model.m')
    except FileNotFoundError as e:
        error = "train_model.m  not found "
        resp = {"msg": error, "code": 1, "data": None}
        app.logger.error(error)
        return jsonify(resp)

    for i in range(days_span + 1):
        d = d_start + datetime.timedelta(days=i)
        d_to_str = d.strftime('%Y-%m-%d')
        # print d_to_str
        for time in range(time_point[0], time_point[-1] + 1):
            result=[]
            for fun in function_:
                if fun in ['traffic', 'customer']:
                    temp_result = get_reslut(d_to_str, time, storeId, fun,model)
                    if fun=='traffic':
                        if i>len(radm)-1:
                            result.append(str(int(temp_result) + radm[-1]))
                        else:
                            result.append(str(int(temp_result) + radm[i]))

                    if fun=='customer':
                        if i>len(radm)-1:
                            result.append(str(int(temp_result) + radm[-1]))
                        else:
                            result.append(str(int(temp_result) + radm[i]))

            output = result
            if len(function_)>1:
                result_dic_traffic[str(d_to_str) + '-' + str(time)] = str((output[0]))
                result_dic_customer[str(d_to_str) + '-' + str(time)] = str((output[-1]))
            elif function_[0]=='traffic':
                result_dic_traffic[str(d_to_str) + '-' + str(time)] = str((output[0]))
            elif function_[0]=='customer':
                result_dic_customer[str(d_to_str) + '-' + str(time)] = str((output[0]))

    if len(function_)>1:
        resp = {"msg": error, "code": 0, "data": \
                {str(storeId): \
                {'traffic':result_dic_traffic,'customer':result_dic_customer}}}
    elif function_[0]=='traffic':
        resp = {"msg": error, "code": 0, "data":\
                {str(storeId):\
                 {'traffic':result_dic_traffic}}}
    elif function_[0]=='customer':
        resp = {"msg": error, "code": 0, "data": \
                {str(storeId):\
                {'customer':result_dic_customer}}}
    app.logger.info('ok')
    return jsonify(resp)

def get_reslut(d_to_str, time, storeId, pred,model):
    args = dict()
    args['storeId'] = storeId
    args['starttime'] = time
    args['preds'] = pred  # 人流客流特征参数 'traffic'/'customer'
    args['day'] = d_to_str
    try :
        args_pref_features = data_helper.data_loader(train=False, args=args)  
        res=model.predict([args_pref_features])
    except BaseException as e:
        app.logger.error(e)
    return res

if __name__ == '__main__':
    app.logger.addHandler(fh)
    app.run(host='0.0.0.0')
