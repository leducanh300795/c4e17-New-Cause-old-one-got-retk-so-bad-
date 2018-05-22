import mlab
from module.service import Service
from faker import Faker
from random import randint, choice
from testdes2 import *
mlab.connect()

fake = Faker()

for i in range(50):
    print('Saving', i+1, '....')
    g=randint(0,1)
    if g==0:
        n=female_name()
        i = female_image()
    elif g==1:
        n=male_name()
        i= male_image()
    service = Service(image=i,
                 name=n,
                 yob=randint(1990,2001),
                 gender=g,
                 email= fake.ascii_email(),
                 height = randint(160,175),
                 measurements = measurements(),
                 phone=sdt(),
                 description = description(),
                 address=tp(),
                 job=job(),
                 company=cty(),
                 status= choice([True,False]))
    service.save()
