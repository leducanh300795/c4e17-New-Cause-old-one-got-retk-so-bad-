from module.customer import Customers
import mlab


mlab.connect()
all_service = Customers.objects(gender=1)


for index, customer in enumerate(all_service):
    print(customer['name'])
    if index == 9:
        break
