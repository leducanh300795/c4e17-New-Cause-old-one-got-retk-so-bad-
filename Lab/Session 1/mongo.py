from pymongo import MongoClient

# 1.Connect to database
uri = "mongodb://admin:admin@ds157089.mlab.com:57089/c4e17"
client = MongoClient(uri)

# 2.Get default database server
db = client.get_default_database()
# 3.Get blog collection
blog = db["blog"]
# 4.Write a new blog
post = {
    'title':" Hôm nay trời đẹp",
    'content':"Tôi ở nhà code"
}
blog.insert_one(post)

all_post = blog.find()
for post in all_post:
    print(post)
