from pymongo import MongoClient

uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(uri)

db = client.get_default_database()

blog = db["posts"]

post = {
    "title": "Dota's life circle",
    "author": "by Sưu tầm",
    "content": '''
        "Tui đã làm trong ngành game F2P 6 năm, lúc thì làm quản lí cộng đồng, còn lúc khác thì làm quản lí sản phẩm. Tui muốn chia sẻ quan điểm của tôi về Doto Plus vì tui thích nói về mấy thứ này mặc dù giờ thì tui khá là ghét việc chuộc lợi từ game F2P
CHIẾN LƯỢC KIẾM TIỀN:
(Để cho tiện thì tui sẽ không nói về steam market hay là giá đồ mà chỉ nói về Battle Pass thui)
Doanh thu từ các trò chơi F2P đến từ một phần rất nhỏ các ông tiêu cực nhiều (Cá Voi). Một phần nhỏ các ông tiêu vừa vừa (Cá Heo), và một phần lớn các ông tiêu ít (Cá Cảnh). Với nhiều game miễn phí khác, doanh thu từ mấy con cá voi kia chiếm hầu hết doanh thu của một trò chơi. ...
    '''
}
