import mlab
from module.service import Service



mlab.connect()

Service.objects.get(id='5af5af80992df1121c2ce2a7').delete()
