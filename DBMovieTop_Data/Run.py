import sys
import os
sys.path.append(os.getcwd())
from lib import Util

if __name__ == '__main__':
    results = []
    page = 0
    url = 'https://movie.douban.com/top250?start={}'.format(25*page)
    headers = {
        'User-Agent':Util.Get_UserAgent()
    }
    response = Util.Get_Response(url=url,headers=headers)
    soup = Util.Get_Soup(response)
    li_list = soup.select('div.article li')
    for li in li_list:
        title = li.select('div.info div.hd a')[0].text.strip().replace('\n','').replace('\xa0',' ')
        # star = li.select('div.star span')[0].text.split('-')[0].replace('rating','')
        results.append([title])
    print(results)