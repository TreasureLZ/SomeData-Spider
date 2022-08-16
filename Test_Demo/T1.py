import requests
if __name__ == '__main__':
    text = requests.get(url='https://movie.douban.com/top250',headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}).text
    print(text)