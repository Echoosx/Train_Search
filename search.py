# -*- coding: utf-8 -*-
from prettytable import PrettyTable
import trainInfo
import stations

train_list=[]

def get_needInfo(num):
    global train_list
    info_list = train_list[num].split('|')
    need_list = []
    s = ""
    # 车次
    need_list.append(info_list[3])
    # 出发站
    if (info_list[4] == info_list[6]):
        s = "(始)"
        s+=stations.get_stationName(info_list[6])
    else:
        s = "(过)"
        s+= stations.get_stationName(info_list[6])

    # 到达站
    if (info_list[5] == info_list[7]):
        s +="\n(终)"
        s+= stations.get_stationName(info_list[7])
    else:
        s += "\n(过)"
        s+=stations.get_stationName(info_list[7])
    need_list.append(s)

    # 出发时间
    s=info_list[8]
    # 到达时间
    s+='\n'
    s+=info_list[9]
    need_list.append(s)
    # 历时
    need_list.append(info_list[10])
    # 特等座
    need_list.append(info_list[32])
    # 一等座
    need_list.append(info_list[31])
    # 二等座
    need_list.append(info_list[30])
    # 高级软卧
    need_list.append(info_list[21])
    # 软卧
    need_list.append(info_list[23])
    # 动卧
    need_list.append(info_list[33])
    # 硬卧
    need_list.append(info_list[28])
    # 软座
    need_list.append(info_list[24])
    # 硬座
    need_list.append(info_list[29])
    # 无座
    need_list.append(info_list[26])
    # 其他
    need_list.append(info_list[22])
    # 备注
    temp=info_list[1].find('<br/>')
    if(temp>=0):
        temp_string=info_list[1][:temp]+info_list[1][temp+5:]
        need_list.append(temp_string)
    else:
        need_list.append(info_list[1])

    for i in range(len(need_list)):
        if need_list[i]=='':
            need_list[i]="--"

    return need_list

def search_start(train_date, from_station, to_station):

    # print("正在查询%s到%s的火车信息。。。" %(str(from_station),str(to_station)))
    global train_list

    train_list = trainInfo.get_trainInfo(train_date, from_station, to_station)

    print("共%d条火车信息\n正在生成图表，请稍候。。。" % len(train_list))
    table = PrettyTable(('车次 车站 时间 历时 特等座 一等 二等 高级软卧 软卧 动卧 硬卧 软座 硬座 无座 其他 备注').split())
    for num in range(len(train_list)):
        table.add_row(get_needInfo(num))

    print(table)


if __name__=="__main__":
    # train_date="2018-12-18"
    # from_station="北京"
    # to_station="上海"

    train_date=input("输入日期：")
    from_station=input("输入出发站：")
    to_station=input("输入目的地：")
    print("正在查询。。。")

    train_list = trainInfo.get_trainInfo(train_date, from_station, to_station)

    print("共%d条火车信息\n正在生成图表，请稍候。。。" %len(train_list))
    table = PrettyTable(('车次 车站 时间 历时 特等座 一等 二等 高级软卧 软卧 动卧 硬卧 软座 硬座 无座 其他 备注').split())
    for num in range(len(train_list)):
        table.add_row(get_needInfo(num))

    print(table)
