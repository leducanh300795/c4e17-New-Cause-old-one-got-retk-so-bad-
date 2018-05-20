from module.service import Service
import mlab


mlab.connect()
all_service = Service.objects(gender=1)


for index, service in enumerate(all_service):
    print(service['name'])
    if index == 9:
        break
