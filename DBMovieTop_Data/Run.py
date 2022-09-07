import sys
sys.path.append('..')
import requests
import time
from lib import Util
from bs4 import BeautifulSoup

if __name__ == '__main__':
    results = []
    page = 0
    for page in range(0,25):
        url = 'https://movie.douban.com/top250?start={}'.format(25*page)
        headers = {
            'User-Agent':Util.Get_UserAgent()
        }
        response = requests.get(url=url,headers=headers)
        soup = BeautifulSoup(response.text,'lxml')
        li_list = soup.select('div.article li')
        for li in li_list:
            try:
                title = li.select('div.info div.hd a span.title')[0].text
            except:
                title = ''
            try:
                star = li.select('div.star span.rating_num')[0].text
            except:
                star = ''
            try:
                comment_number = li.select('div.star span')[3].text
            except:
                comment_number = ''
            try:
                content = li.select('p.quote span')[0].text
            except:
                content = ''
            try:
                details = li.select('div.bd p')[0].text
                details = Util.Replace_Space(details, [' ','\n'])
            except:
                details = ''
            try:
                href = li.select('div.info div.hd a')[0].get('href')
            except:
                href = ''
            results.append([title,star,comment_number,details,content,href])
        print("采集第{}页成功！".format(page+1))
        time.sleep(1)
    with open('../DBMovieTop_Data/Data.csv','w+',encoding='utf-8') as fp:
        header = ['标题','评分','评论人数','总结','详情','链接']
        fp.write('\t'.join(header)+'\n')
        for result in results:
            fp.write("\t".join(result)+'\n')
    