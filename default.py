def default_request(radm):
    
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
    # radm = random.randint(0, 50)
    output=function[0]+':'+str(int(result1+radm[0]))+','+function[-1]+':'+str(int(result2+radm[0]))
    result_dic = dict()
    result_dic[str(d_to_str) + ',' + str(time)] = str(output)
    # df=pd.DataFrame()
    time_p=str(d_to_str) + ',' + str(time)

    resp = {"msg": error, "code": 0, "data": \
        # {'traffic': {time_p: str(int(result1))}, 'custmoer': {time_p: str(int(result2))}}}
            {str(storeId):\
            {'traffic':{time_p:str(int(result1+radm[0]))},'custmoer':{time_p:str(int(result2+radm[0]))}}}}
    logger.info('ok')

    return jsonify(resp)
