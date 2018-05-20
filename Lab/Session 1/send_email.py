from gmail import GMail, Message
from random import choice
#1
#SMTP
html_template='''<p><em><strong>Ch&agrave;o anh,</strong></em></p>
<p>Em bị bệnh {{x}} </p> '''

sickness_list= ["Thương hàn", "Kiết lị", "Ebola"]
sickness= choice(sickness_list)

html_content = html_template.replace("{{x}}", sickness)
mail = GMail('anhld07.cfe@gmail.com','daica010')
#msg = Message('Test Message',to='xyz <xyz@xyz.com>',text='Hello')
message = Message('Say hi',to='c4e.201708@gmail.com',html=html_content)
mail.send(message)

#msg = Message('Test Message',to='xyz@xyz.com',text="Hello",html="<b>Hello</b>",attachments=['img.jpg'])
