from bs4 import BeautifulSoup
import urllib.request
import click
import os
import re
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

rootUrl = 'http://3g.dxy.cn/newh5/view/pneumonia'


def lookup():
    while True:
        try:
            html = urllib.request.urlopen(rootUrl)
            bs = BeautifulSoup(html, features='html.parser')
        except Exception:
            click.clear()
            click.echo(click.style('Internet Connection ERROR!', blink=True, fg='red'))
            click.echo(click.style('Retry? [y/n]', fg='blue'))
            choice = str(input())
            if choice == 'y' or choice == 'Y':
                continue
            else:
                exit(0)

        script = str(bs.find('script', {'id': 'getStatisticsService'}).text)
        confirmed_pat = re.compile('\"confirmedCount\"\:([0-9]+)')
        suspected_pat = re.compile('\"suspectedCount\"\:([0-9]+)')
        cured_pat = re.compile('\"curedCount\"\:([0-9]+)')
        dead_pat = re.compile('\"deadCount\"\:([0-9]+)')
        confirmed = re.findall(confirmed_pat, script)[0]
        suspected = re.findall(suspected_pat, script)[0]
        cured = re.findall(cured_pat, script)[0]
        dead = re.findall(dead_pat, script)[0]

        result = confirmed, suspected, cured, dead

        return result


def detailed_info():
    while True:
        try:
            html = urllib.request.urlopen(rootUrl)
            bs = BeautifulSoup(html, features='html.parser')
        except Exception:
            click.clear()
            click.echo(click.style('Internet Connection ERROR!', blink=True, fg='red'))
            click.echo(click.style('Retry? [y/n]', fg='blue'))
            choice = str(input())
            if choice == 'y' or choice == 'Y':
                continue
            else:
                exit(0)
        script = str(bs.find('script', {'id': 'getAreaStat'}).text)
        data = script[27:-11]
        # print(os.getcwd())

        with open('temp.py', 'w+') as f:
            f.write('# coding=utf-8\n')
            f.write('import pickle\n')
            f.write('import os\n')
            f.write('a = ')
            f.write(data)
            f.write('\n')
            f.write('with open(\'data.pickle\', \'wb+\') as file:\n')
            f.write('    ')
            f.write('pickle.dump(a, file, 0)\n')
            # f.write('os.system(\'python3 Report/Parser.py\')')
        os.system('python3 temp.py')
        import Report.Parser
        os.system('rm -rf temp.py data.pickle')
        exit(0)

# Debug
