# -*- coding: utf-8 -*-
import requests
import re
# from pprint import pprint
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url="https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.8971"
response=requests.get(url,verify=False)     #verify=False 跳过证书
station_list=re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)',response.text)
station_dict=dict(station_list)
station_dict_reverse = {v: k for k, v in station_dict.items()}       # station字典键值反转
# print(station_dict)

def get_stationName(station_code):      # 由地点代码得到地点名称
    station_name=station_dict_reverse[station_code]
    return station_name

def get_stationCode(station_name):      # 由地点名称得到地点代码
    station_code=station_dict[station_name]
    return station_code
