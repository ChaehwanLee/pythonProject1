# weather.py
from urllib import request;

import bs4


def getdata():
    target = request.urlopen('https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnld=108');
    soup = bs4.BeautifulSoup(target,'html.parser');
    wlist = [];
    for city in soup.select('location'): #for 문에다 담아서 돌린다
        st = '%s:%s(%s~%s)';# 지역의 날씨를 리스트에 담아서 리턴한다
        name = city.select_one('city').string
        wf = city.select_one('wf').string
        tmn = city.select_one('tmn').string
        tmx = city.select_one('tmx').string
        wlist.append(st % (name,wf,tmn, tmx));
    return wlist;

if __name__ == '__main__':
    result = getdata();
    print(result);