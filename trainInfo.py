# -*- coding: utf-8 -*-
import requests
import urllib3
import stations
import json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 获得列车信息 例：get_trainInfo('2018-10-13','北京','上海')，返回2018年10月13日从北京到上海的info_list包含数据
def get_trainInfo(train_date,from_station,to_station):
    # train_date="2018-10-13"
    from_station=stations.get_stationCode(from_station)     #转为地点代码
    to_station=stations.get_stationCode(to_station)

    url = " https://kyfw.12306.cn/otn/leftTicket/queryO?leftTicketDTO.train_date=%s&leftTicketDTO.from_station=%s&leftTicketDTO.to_station=%s&purpose_codes=ADULT" % (
    train_date, from_station, to_station)
    # print(url)
    response = requests.get(url, verify=False)  # verify=False 跳过证书
    json_code = response.text
    # print(response.text)
    info_dict = dict(json.loads(json_code))  # json解析
    train_list=info_dict['data']['result']
    return train_list
