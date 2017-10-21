# -*- coding: utf-8 -*-
import data_helper
from sklearn.externals import joblib
import time, datetime
import random
import pandas as pd
from flask import *

import logging

logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='myapp.log',
                filemode='w')


app = Flask(__name__)

# http://127.0.0.1:5000/analysis?function=traffic&storeId=731888568958976&hour=9-20&daySpan=2017-09-20,2017-9-25
@app.route('/analysis/', methods=['GET'])
def analyse():
    error = 'ok'
    # print(request.args.get('hour'))

    time_point = request.args.get('hour')  # 预测几点

    dates = request.args.get('daySpan')  # 预测几月到几月
    function = request.args.get('function')
    storeId = request.args.get('storeId')

    # 判断什么也没有输入
    # http://127.0.0.1:5000/analysis/
    if time_point == None and dates == None and function == None and storeId == None:


        storeId = 731888568958976  # 默认店铺

        function = ['traffic','customer']  # 默认计算客流量

        now = datetime.datetime.now()

        str_now = now.strftime('%Y-%m-%d %H:%M:%S')
        date_now = str_now.split(' ')[0]
        hour_point_now = int(str(str_now.split(' ')[1]).split(':')[0])
        if ((hour_point_now + 1) < 9 or (hour_point_now + 1) > 22):

            now_day = datetime.date(*[int(x) for x in str(date_now).split('-')])
            tomorrow = now_day + datetime.timedelta(days=1)
            dates = [tomorrow.strftime('%Y-%m-%d')]
            time = int(9)

        else:
            dates = [date_now]
            time = int(hour_point_now + 1)

        d_start = datetime.date(*[int(x) for x in str(dates[0]).split('-')])

        d_to_str = d_start.strftime('%Y-%m-%d')
        result1 = get_reslut(d_to_str, time, storeId, function[0])
        result2 = get_reslut(d_to_str, time, storeId, function[-1])
        radm = random.randint(0, 50)
        output=function[0]+':'+str(int(result1+radm))+','+function[-1]+':'+str(int(result2+radm))
        result_dic = dict()
        result_dic[str(d_to_str) + ',' + str(time)] = str(output)
        # df=pd.DataFrame()
        time_p=str(d_to_str) + ',' + str(time)

        resp = {"msg": error, "code": 0, "data": \
            {'traffic':{time_p:str(int(result1+radm))},'custmoer':{time_p:str(int(result2+radm))}}}
        logging.info('ok')
        return jsonify(resp)

    try:
        time_point = [int(x) for x in str(request.args.get('hour')).split(',')]  # 预测几点
    except ValueError as e:
        error = "Incorrect input data <hour>: "
        error += (': ' + str(e))
        resp = {"msg": error, "code": 1, "data": None}
        logging.debug(error)
        return jsonify(resp)




    try:
        time_point = [int(x) for x in str(request.args.get('hour')).split('-')]  # 预测几点
    except ValueError as e:
        error = "Incorrect input data <hour>: "
        error += (': ' + str(e))
        resp = {"msg": error, "code": 1, "data": None}
        logging.debug(error)
        return jsonify(resp)

    try:
        dates = str(request.args.get('daySpan')).split(',')  # 预测几月到几月
    except ValueError as e:
        error = "Incorrect input data <dates>: "
        error += (': ' + str(e))
        logging.debug(error)
        resp = {"msg": error, "code": 1, "data": None}
        return jsonify(resp)

    try:
        function_ = str(request.args.get('function')).split(',')

    except ValueError as e:
        error = "Incorrect input data <function>: "
        error += (': ' + str(e))
        logging.debug(error)
        resp = {"msg": error, "code": 1, "data": None}
        return jsonify(resp)

    try:
        storeId = int(str(request.args.get('storeId')))

    except ValueError as e:
        error = "Incorrect input data <storeId>: "
        error += (': ' + str(e))
        resp = {"msg": error, "code": 1, "data": None}
        logging.debug(error)
        return jsonify(resp)

    if time_point == None or dates == None or function_ == None or storeId == None:
        error = "Missing input data: "
        resp = {"msg": error, "code": 1, "data": None}
        logging.debug(error)
        return jsonify(resp)


    if function_[0]  not in ['traffic', 'customer'] or function_[-1]  not in ['traffic', 'customer']:
        error = "Incorrect parameter input <function>"+function_[0]+','+function_[-1]+": "
        resp = {"msg": error, "code": 1, "data": None}
        logging.debug(error)
        return jsonify(resp)



    # method=1  #method 0 or 1 ,method 0:精确预测，耗时多; method 1:历史数据预测，耗时少;
    try:
        d_start = datetime.date(*[int(x) for x in str(dates[0]).split('-')])
        d_end = datetime.date(*[int(x) for x in str(dates[-1]).split('-')])
    except ValueError as e:
        error = "Incorrect input data : "
        error += (': ' + str(e))
        resp = {"msg": error, "code": 1, "data": None}
        logging.debug(error)
        return jsonify(resp)

    if d_start > d_end:
        error = "Incorrect parameter input <dates> :The start date must be before the end date: "
        resp = {"msg": error, "code": 1, "data": None}
        logging.debug(error)
        return jsonify(resp)

    days_span = (d_end - d_start).days  # 差了几天

    # df=pd.DataFrame()

    result_dic_traffic = dict()
    result_dic_customer= dict()

    for i in range(days_span + 1):
        d = d_start + datetime.timedelta(days=i)
        d_to_str = d.strftime('%Y-%m-%d')
        # print d_to_str
        for time in range(time_point[0], time_point[-1] + 1):
            result=[]
            for fun in function_:
                if fun in ['traffic', 'customer']:
                    temp_result = get_reslut(d_to_str, time, storeId, fun)
                    radm = random.randint(0, 50)
                    if fun=='traffic':
                        result.append(str(int(temp_result)+radm))
                    if fun=='customer':
                        result.append(str(int(temp_result)+radm))

            output = result
            if len(function_)>1:
                result_dic_traffic[str(d_to_str) + '-' + str(time)] = str((output[0]))
                result_dic_customer[str(d_to_str) + '-' + str(time)] = str((output[-1]))
            elif function_[0]=='traffic':
                result_dic_traffic[str(d_to_str) + '-' + str(time)] = str((output[0]))
            elif function_[0]=='customer':
                result_dic_customer[str(d_to_str) + '-' + str(time)] = str((output[0]))



    if len(function_)>1:
        resp = {"msg": error, "code": 0, "data": {'traffic':result_dic_traffic,'customer':result_dic_customer}}
    elif function_[0]=='traffic':
        resp = {"msg": error, "code": 0, "data": {'traffic':result_dic_traffic}}
    elif function_[0]=='customer':
        resp = {"msg": error, "code": 0, "data": {'customer':result_dic_customer}}
    logging.info('ok')
    return jsonify(resp)


def get_reslut(d_to_str, time, storeId, pred):
    args = dict()
    args['storeId'] = storeId
    args['starttime'] = time
    args['preds'] = pred  # 人流客流特征参数 'traffic'/'customer'
    args['day'] = d_to_str

    args_pref_features = data_helper.data_loader(train=False, args=args)
    model = joblib.load('train_model.m')
    return model.predict([args_pref_features])


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
