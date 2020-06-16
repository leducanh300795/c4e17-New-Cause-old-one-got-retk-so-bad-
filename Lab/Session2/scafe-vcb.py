from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
url = "https://s.cafef.vn/bao-cao-tai-chinh/VCB/IncSta/2020/1/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"

html_content= urlopen(url).read().decode('utf8')

# f=open('scafe.html','wb')
# f.write(html_content)
# f.close()
soup = BeautifulSoup(html_content, 'lxml')

table = soup.find('table', id ='tableContent')

trs= table.find_all('tr')

datas = []

for tr in trs:
    tds= tr.find_all('td')
    data = {}

    if tds and tds[0].string is not None:
        data['title'] = (tds[0].string)
        data['3-2019']= (tds[1].string)
        data['4-2019']= (tds[2].string)
        data['1-2020']= (tds[3].string)
        data['2-2020']= (tds[4].string)
    if data:
        datas.append(data)
# print (datas)
# print(datas)
pyexcel.save_as(records=datas, dest_file_name='scafef.xlsx')
