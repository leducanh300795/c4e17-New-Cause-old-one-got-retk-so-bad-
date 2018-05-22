from random import choice,randint

def tp():
    tps=['An Giang','Bà Rịa-Vũng Tàu','Bạc Liêu','Bắc Kạn','Bắc Giang','Bắc Ninh','Bến Tre','Bình Dương','Bình Định','Bình Phước','Bình Thuận','Cà Mau','Cao Bằng','Cần Thơ (TP)','Đà Nẵng (TP)','Đắk Lắk','Đắk Nông','Điện Biên','Đồng Nai','Đồng Tháp','Gia Lai','Hà Giang','Hà Nam','Hà Nội (TP)']
    tp = choice(tps)
    return(tp)
def sdt():
    s=['096','097','098','086', '0162','0163', '0164', '0165', '0166', '0167', '0168', '0169','091', '094', '088', '0123', '0124']
    d=['0','1','2','3','4','5','6','7','8','9']
    sdt=choice(s)
    for i in range(7):
        t=choice(d)
        sdt=sdt+t
    return(sdt)

def description():
    characters = ['dễ dãi', 'vui vẻ', 'hòa đồng', 'yêu đời',
                  'khéo léo', 'hài hước', 'ngáo đá', 'điên dại',
                  'tình cảm', 'sida', 'hâm', 'cẩn thận',
                  'nổi loạn', 'cầu toàn', 'bốc đồng']
    description = []
    for i in range(randint(3,6)):
        character = choice(characters)
        description.append(character)
    return (description)

def cty():
    from urllib.request import urlopen
    from bs4 import BeautifulSoup

    url="http://s.cafef.vn/danh-sach-tap-doan-doanh-nghiep-lon.chn"
    conn = urlopen(url)
    raw_data=conn.read()
    text = raw_data.decode("utf8")

    soup = BeautifulSoup(text,"html.parser")

    table=soup.find("table",id='table_list')
    tr_list = table.find_all("tr")
    data=[]
    for tr in tr_list:
        list=[]
        td_list=tr.find_all("td")
        for td in td_list:
            a=td.a
            i=a.string
            list.append(i)
        if list:
            d=list[1].strip()
            data.append(d)
    cty=choice(data)
    return(cty)
def job():
    jobs=['Giám đốc','Phó Giám đốc','Chủ tịch Hội đồng quản trị','Trưởng phòng','Phó phòng','Kế toán','Nhân viên','Tạp vụ','Lao công','Bảo vệ','Chủ tịch Công đoàn','Thực tập','Quản lý','Thu ngân','Thư kí']
    job = choice(jobs)
    return(job)

def measurements():
    mesurements = [randint(85,95), randint(55,65), randint(85,95)]
    return (mesurements)


def male_image():
    images=["https://baomoi-photo-3-td.zadn.vn/w300_r3x2/18/02/23/200/25036712/6_96172.jpg","https://baomoi-photo-1-td.zadn.vn/w300_r3x2/18/05/09/61/25966074/1_134733.jpg","https://tinnhanh.dkn.tv/wp-content/uploads/2018/04/doc-dao-y-tuong-khoi-nghiep-bang-coc-cafe-cua-hotboy-dai-hoc-thuong-mai-300x200.jpg"]
    image = choice(images)
    return(image)

def female_image():
    images=["https://s3.amazonaws.com/s3.imagefinder.co/uploads/2017/11/29155815/cute-girl-in-fur-cap-smiling-300x200.jpg","https://baomoi-photo-2-td.zadn.vn/w300_r3x2/17/04/21/200/22076140/1_69153.jpg","http://cachlammoi.com/wp-content/uploads/2017/10/chipu-sinh-nam-bao-nhieu-doi-tu-va-su-nghiep-cua-hot-girl-ha-thanh-300x200-300x200.jpg"]
    image = choice(images)
    return(image)















# def male_name():
#     h=['Nguyễn','Trần','Lê','Phạm','Hoàng','Huỳnh','Phan','Vũ','Võ','Đặng','Bùi','Đỗ','Hồ','Ngô','Dương','Lý','Hà','Đào','Phùng','Trương','Nông','Phương','Cao','Mai','Đinh','Lương','Trịnh','Đoàn']
#     d=['Anh','Tuấn','Hoàng','Phúc','Khải','Phương','Bá','Tuấn','Hữu','Hải','Nhân','Đức','Trọng','Phú','Minh','Xuân','Trung','Tuấn','Đinh','Khôi','Phước','Hoàng','Bảo','Thành','Lâm','Việt','Đức','Đăng','Nhật','Vinh','','']
#     t=['Anh','Tuấn','Hoàng','Phúc','Khải','Phương','Nam','Dũng','Hữu','Hải','Nhân','Đức','Trọng','Phú','Minh','Dương','Trung','Tuấn','Nghĩa','Khôi','Phước','Hoàng','Bảo','Thành','Lâm','Việt','Đức','Nguyên','Nhật','Vinh','Phong','Chung','Quân','Quang','Quốc','Tuấn','Thành','Thiên','Thịnh','Sơn','Việt','Bách','Cường','Đạt','Hiếu','Huy','Hùng','Tuấn Anh']
#     while True:
#         ho = choice(h)
#         dem = choice(d)
#         ten = choice(t)
#         if ho==dem or dem==ten:
#             continue
#         else:
#             name= ho+' '+dem+' '+ten
#             break
#     return(name)
# def female_name():
#     h=['Nguyễn','Trần','Lê','Phạm','Hoàng','Huỳnh','Phan','Vũ','Võ','Đặng','Bùi','Đỗ','Hồ','Ngô','Dương','Lý','Hà','Đào','Phùng','Trương','Nông','Phương','Cao','Mai','Đinh','Lương','Trịnh','Đoàn']
#     d=['Mỹ','Khánh','Kiều','Phúc','Thùy','Mai','Hoa','Ngọc','Diễm','Hải','Bích','Nhã','Thúy','Minh','Xuân','Hoàng','Bảo','','Nhật','']
#     t=['Anh','Ngọc','Châu','Uyên','Linh','Phương','Chi','Nhi','Thư','Hải','Thùy','Mai','Hoa','Ngọc','Minh','Dương','Hiền','Thủy','Quyên','Hà','Phước','Bích','Trâm','Khuê','Tú','Ngân','Trang','Thúy','Tuyết','Ngà','Oanh','Vân Anh','Quỳnh Anh','Phương Anh','Bảo Anh','Tâm','Bình','Ngọc Ánh']
#     while True:
#         ho = choice(h)
#         dem = choice(d)
#         ten = choice(t)
#         if ho==dem or dem==ten:
#             continue
#         else:
#             name= ho+' '+dem+' '+ten
#             break
#     return(name)
