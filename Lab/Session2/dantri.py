from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

url = "http://dantri.com.vn"
#1.1 Open connection
conn = urlopen(url)
#1.2 Read data
raw_data= conn.read()
#1.3 Decode
text = raw_data.decode('utf8')
#print
# dan_tri_file= open("dantri.html", "wb") #w la text ko, wb la data thô chưa được giải mã
#
# dan_tri_file.write(raw_data)
#
# dan_tri_file.close()

#2. Find ROI
soup = BeautifulSoup(text, "html.parser") #coi doan van nhu html
# print(soup.prettify()) #ham fonction
ul= soup.find("ul","ul1 ulnew")

# print(ul.prettify())

li_list = ul.find_all("li")
li = li_list[0]
item_list = []
# print(li.prettify())
for li in li_list:
    a= li.h4.a
    title = a.string #hoac title = a['title'] # string or content
    # print(title)
    link = url + a['href']
    # print(link)
    # print("------------------------------------------")
    item = {
        "Title": title,
        "Link": link
    }
    item_list.append(item)
    print(item)
    print("***************************************")
# title = a['title']
# print(tittle)
#3.
print(item_list)
pyexcel.save_as(records=item_list, dest_file_name="dantri2.xlsx")
