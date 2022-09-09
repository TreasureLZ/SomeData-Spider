import sys
sys.path.append('..')
import requests
import time
from lib import Util
from bs4 import BeautifulSoup
import json

def Run(city,page):
    url = 'https://search.51job.com/list/000000,000000,0000,00,9,99,{},2,{}.html'.format(city,page)
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': 'guid=417a461c32e435d62be26e8b1467a0c2; nsearch=jobarea%3D%26%7C%26ord_field%3D%26%7C%26recentSearch0%3D%26%7C%26recentSearch1%3D%26%7C%26recentSearch2%3D%26%7C%26recentSearch3%3D%26%7C%26recentSearch4%3D%26%7C%26collapse_expansion%3D; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22417a461c32e435d62be26e8b1467a0c2%22%2C%22first_id%22%3A%2218315f9262918b3-012ce106f3fd78c-1a525635-1296000-18315f9262a10b0%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTgzMTVmOTI2MjkxOGIzLTAxMmNlMTA2ZjNmZDc4Yy0xYTUyNTYzNS0xMjk2MDAwLTE4MzE1ZjkyNjJhMTBiMCIsIiRpZGVudGl0eV9sb2dpbl9pZCI6IjQxN2E0NjFjMzJlNDM1ZDYyYmUyNmU4YjE0NjdhMGMyIn0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22417a461c32e435d62be26e8b1467a0c2%22%7D%2C%22%24device_id%22%3A%2218315f9262918b3-012ce106f3fd78c-1a525635-1296000-18315f9262a10b0%22%7D; search=jobarea%7E%60000000%7C%21ord_field%7E%600%7C%21recentSearch0%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FApython%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch1%7E%60190200%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FApython%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21; acw_tc=ac11000116626817724023819e00df59d0b9c8c268220331d2c4c21474566f',
        'Host': 'search.51job.com',
        'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
        # 'User-Agent':Util.Get_UserAgent(),
        'sec-ch-ua-platform': '"macOS"',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }
    response = requests.get(url=url,headers=headers)
    text = response.text
    soup = BeautifulSoup(text,'lxml')
    script_lst = soup.select('script')
    script = script_lst[7].text
    script.replace('window.__SEARCH_RESULT__ = ','')
    json_data =json.dumps(script)

def Write(data):
    header = ['岗位名称','薪资待遇']
    fp.write('\t'.join(header)+'\n')
    

if __name__ == '__main__':
    citys = ['长沙']
    for city in citys:
        for page in range(1,2):
            Run(city,page)