import sys
import os
import requests
sys.path.append(os.getcwd())
from lib import Util
from bs4 import BeautifulSoup

if __name__ == '__main__':
    results = []
    page = 0
    url = 'https://movie.douban.com/top250?start={}'.format(25*page)
    headers = {
        'User-Agent':Util.Get_UserAgent()
    }
    response = requests.get(url=url,headers=headers)
    soup = BeautifulSoup(response.text,'lxml')
    li_list = soup.select('div.article li')
    for li in li_list:
        title = li.select('div.info div.hd a')[0].text
        title = Util.Replace_Space(title, ['\n','\xa0'])
        results.append([title])
    print(results)
    