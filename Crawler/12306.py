#coding:utf-8
import sys
import requests
import json

requests.packages.urllib3.disable_warnings()
from prettytable import PrettyTable
table = PrettyTable(["车次", "出发站","目的地","出发时间","到达时间","总时间","一等座","二等座","软卧","硬卧","硬座","无座"])
from stations import stations_dict
code_dict = {v: k for k, v in stations_dict.items()}
def getUrl(args):
    try:
        date = args[1]#'2017-10-28'
        from_station_name = args[2]#'大连'
        to_station_name = args[3]#'北京'
        from_station=stations_dict[from_station_name]
        to_station = stations_dict[to_station_name]
    except:
        date,from_station,to_station='--','--','--'


    url = (
        'https://kyfw.12306.cn/otn/leftTicket/query?'
        'leftTicketDTO.train_date={}&'
        'leftTicketDTO.from_station={}&'
        'leftTicketDTO.to_station={}&'
        'purpose_codes=ADULT'
    ).format(date, from_station, to_station)
    # print(url)

    return url

def getInfo(url):

    try:
        r = requests.get(url, verify=False)

        raw_trains = r.json()['data']['result']

        for raw_train in raw_trains:

            data_list = raw_train.split('|')
            # print (data_list)
            # 车次号码
            train_no = data_list[3]
            # 出发站
            from_station_code = data_list[6]
            from_station_name = code_dict[from_station_code]
            # 终点站
            to_station_code = data_list[7]
            to_station_name = code_dict[to_station_code]
            # 出发时间
            start_time = data_list[8]
            # 到达时间
            over_time = data_list[9]
            # 总耗时
            times = data_list[10]
            # 一等座
            yideng = data_list[31] or '--'
            # 二等座
            erdeng = data_list[30]or '--'
            # 软卧
            ruanwo = data_list[23]or '--'
            # 硬卧
            yingwo = data_list[28]or '--'
            # 硬座
            yingzuo = data_list[29]or '--'
            # 无座
            wozuo = data_list[26]or '--'

            # info = ('车次:{}\t出发站:{}\t目的地:{}\t出发时间:{}\t到达时间:{}\t总时间:{}\t一等座：「{}」 \t二等座：「{}」\t软卧：「{}」\t硬卧：「{}」\t硬座：「{}」\t无座：「{}」\t\n'.format(
            #     train_no, from_station_name, to_station_name, start_time, over_time, times, yideng,
            #     erdeng, ruanwo, yingwo, yingzuo, wozuo))
            # print (train_no, from_station_name, to_station_name, start_time, over_time, times, yideng,erdeng, ruanwo, yingwo, yingzuo, wozuo)
            info = [train_no, from_station_name, to_station_name, start_time, over_time, times, yideng,erdeng, ruanwo, yingwo, yingzuo, wozuo]
            # print (info)
            table.add_row(info)
    except:
        return ' Error'


if __name__ == '__main__':
    getInfo(getUrl(sys.argv))
    table.border=True
    # table.align["车次"] = "l"
    # print('\033[1;31;40m')
    print(table)