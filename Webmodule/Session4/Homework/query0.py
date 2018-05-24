# from module.service import Service
# import mlab
#
#
# mlab.connect()
# all_service = Service.objects(gender=1)
#
#
# for index, service in enumerate(all_service):
#     print(service['name'])
#     if index == 9:
#         break
from module.user import *
import mlab
from random import *
mlab.connect()
all_user = User.objects()
list_user=[]
for index, user in enumerate(all_user):
    a = user['idsignin']
    list_user.append(a)
print(list_user)
b = choice(list_user)
print(b)

all_user_password = User.objects(idsignin=b)
print(user_password['password'])
