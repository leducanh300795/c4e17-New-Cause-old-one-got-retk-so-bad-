from designe.video import Video
import mlab
from faker import Faker
from random import randint,choice

fake = Faker()


mlab.connect()

for i in range(5):
    print("Saving new data", i + 1, "....")
    video = Video(title= "ten video" ,
                        thumbnail= "Anh Video" ,
                        view= randint(1,10),
                        youtubeid= randint(1,10),
                        )
#
    video.save()
