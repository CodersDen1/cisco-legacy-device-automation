import os
from netmiko import ConnectHandler
import json

from connection import connection_to_device
import connection 



user= input('Username')
password='cisco'
sec='cisco'
ip ='11.1.1.1'

try:
    connection_to_device(username=user,password=password,secret=sec,ipadd='192.168.213.131',port=23)
    interfaces = connection.connect.send_command('show ip int brief')
    print('interfaces which are up \n')
    print(interfaces)
    connection.connect.close()
except Exception as e:
    print(e)
finally:
    print('connection closed')
    
