import csv
import time
# import urllib
import click
# from bs4 import BeautifulSoup
import pickle
from Report.Recorder import lookup
from prettytable import PrettyTable


with open('data.pickle', 'rb') as data:
    a = pickle.load(data)


click.echo('Write File Output? [Y/n]')
c = str(input())
if c == 'y' or c == 'Y':
    p_table = PrettyTable(['省级行政区', '确诊', '疑似', '治愈', '死亡'])
    c_table = PrettyTable(['市', '确诊', '疑似', '治愈', '死亡'])
    with open('provinces_' + str(time.strftime('%m-%d')) + '.csv', 'w+') as p:
        info = lookup()
        p.write(time.ctime(time.time()) + '\n')
        p_writer = csv.writer(p)
        p_writer.writerow(['', '确诊', '疑似', '治愈', '死亡'])
        p_writer.writerow(['全国', info[0], info[1], info[2], info[3]])
        p_writer.writerow(['省级行政区', '确诊', '疑似', '治愈', '死亡'])
        pCount = 0
        cCount = 0
        with open('cities_' + str(time.strftime('%m-%d')) + '.csv', 'w+') as c:
            c.write(time.ctime(time.time()) + '\n')
            c_writer = csv.writer(c)
            c_writer.writerow(['市', '确诊', '疑似', '治愈', '死亡'])

            for province in a:
                pCount += 1
                # print(province)
                row = [province['provinceName'], province['confirmedCount'], province['suspectedCount'],
                       province['curedCount'], province['deadCount']]
                p_writer.writerow(row)
                p_table.add_row(row)
                for city in province['cities']:
                    cCount += 1
                    # print(city)
                    c_row = [city['cityName'], city['confirmedCount'], city['suspectedCount'],
                             city['curedCount'], city['deadCount']]
                    c_writer.writerow(c_row)
                    c_table.add_row(c_row)
                    # print(city['cityName'] + ' OK')
                # print(province['provinceName'] + ' OK')

            print(str(pCount) + ' provinces and ' + str(cCount) + ' cities in total')
else:
    p_table = PrettyTable(['省级行政区', '确诊', '疑似', '治愈', '死亡'])
    c_table = PrettyTable(['市', '确诊', '疑似', '治愈', '死亡'])
    info = lookup()
    pCount = 0
    cCount = 0
    for province in a:
        pCount += 1
        row = [province['provinceName'], province['confirmedCount'], province['suspectedCount'],
               province['curedCount'], province['deadCount']]
        p_table.add_row(row)
        for city in province['cities']:
            cCount += 1
            c_row = [city['cityName'], city['confirmedCount'], city['suspectedCount'],
                     city['curedCount'], city['deadCount']]
            c_table.add_row(c_row)

    print(str(pCount) + ' provinces and ' + str(cCount) + ' cities in total')

click.echo(p_table)
click.echo()
click.echo(c_table)
