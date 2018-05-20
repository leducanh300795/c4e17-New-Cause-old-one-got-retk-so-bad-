import mlab
from module.service import Service



mlab.connect()

id_to_find = "5af59fd6992df122146b7bc3"

# hera = Service.objects(id=id_to_find)
# hera = Service.objects.get(id=id_to_find)
hera = Service.objects.with_id(id_to_find)

if hera is not None:
    # hera.delete()
    print(hera.address)
    print(hera.height)
    hera.update(set__address="Phạm Văn Đồng", set__height=168 )
    hera.reload()
    print(hera.address)
    print(hera.height)
    # print("Deleted")
else:
    print("Service not found ")

# print(hera.to_mongo())
# hera.to_mongo de print ra ca list
