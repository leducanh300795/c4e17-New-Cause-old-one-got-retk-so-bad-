from module.service import Service
import mlab
from faker import Faker
from random import randint,choice

fake = Faker()


mlab.connect()

for i in range(50):
    print("Saving service", i + 1, "....")
    service = Service(name= fake.name(),
                        yob= randint(1990, 2001 ),
                        gender=randint(0, 1),
                        height=randint(150,190),
                        phone=fake.phone_number(),
                        address=fake.address(),
                        status=choice([False,True]))
#
    service.save()
