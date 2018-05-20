from pymongo import MongoClient
from matplotlib import pyplot

uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(uri)

db = client.get_default_database()
customers = db["customers"]

events_count=0
ad_count=0
wom_count=0

all_posts = customers.find()
for post in all_posts:
    if post["ref"] == "events":
        events_count+=1
    elif post["ref"] == "ads":
        ad_count+=1
    elif post["ref"]=="wom":
        wom_count+=1
print(events_count, ad_count, wom_count)
# total_refs= sum(events_count, ad_count, wom_count)
# print(total_refs)
ref_counts = [events_count, ad_count, wom_count]
ref_names = ["Events", "Ads", "Word of mouth"]

pyplot.pie(ref_counts, labels=ref_names, autopct="%.1f%%", shadow =True, explode =[0,0.2,0])
pyplot.axis("equal")
pyplot.title("The percentage of costumers")

pyplot.show()
