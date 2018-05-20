from module.customer import Customers
import mlab
from faker import Faker
from random import randint,choice

fake = Faker()


mlab.connect()

for i in range(50):
    print("Saving customer", i + 1, "....")
    customer = Customers(name= fake.name(),
                        gender=randint(0, 1),
                        email=fake.ascii_free_email(),
                        phone_number=fake.phone_number(),
                        job=fake.job(),
                        company=fake.company(),
                        contacted=choice([False,True]))
#
    customer.save()
