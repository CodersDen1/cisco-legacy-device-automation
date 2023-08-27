import os
from netmiko import ConnectHandler
import json
from getpass import getpass

from connection import connection_to_device
import connection 

user= input ("Enter Username : ")
password= getpass ("Enter Password : ")
sec=password
ip =input ("Enter Device IP : ")

try:
    connection_to_device(username=user,password=password,secret=sec,ipadd=ip,port=23)
    interfaces = connection.connect.send_command('show ip int brief')
    print('interfaces which are up \n')
    print(interfaces)
    connection.connect.close()
except Exception as e:
    print(e)
finally:
    print('connection closed')
