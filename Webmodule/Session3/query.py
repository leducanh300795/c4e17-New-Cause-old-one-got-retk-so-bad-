from models.service import Service
import mlab

mlab.connect()

# all_service = Service.objects(gender=0)   # Lay tat ca cac object trong collection Service, co the filter cac field trong ()
#
# for index, service in enumerate(all_service):
#     print(service['name'])
#     if index ==9:
#         break
# all_service = Service.objects()
# for service in all_service:
#     service.delete()
id_to_find = '5af59ced8f71f01290889e5a'
# hera= Service.objects(id=id_to_find)
# hera = Service.objects.get(id=id_to_find)
hera = Service.objects.with_id(id_to_find)
if hera is not None:
    # hera.delete()
    print(hera.address)
    hera.update(set__address='Phạm Văn Đồng', set__height=173)
    # print('Deleted')
    hera.reload()
    print(hera.address, hera.height)
else:
    print('Service not found')
# print(hera.to_mongo())
