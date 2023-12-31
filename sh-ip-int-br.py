
import json
from getpass import getpass

from connection import connection_to_device
from outputToExel import toExcelFile
import connection
import constants 
from getpass import getpass

from getUserDetails import getUserDetail
import getUserDetails

getUserDetail()

constants.connection_profiles['username']=getUserDetails.user
constants.connection_profiles['password']=getUserDetails.password
constants.connection_profiles['secret']=getUserDetails.sec
constants.connection_profiles['ipadd']=getUserDetails.ip
constants.connection_profiles['port']=getUserDetails.port

try:
    connection_to_device(**constants.connection_profiles)
    interfaces = connection.connect.send_command('show ip int brief',use_textfsm=True)
    #print('interfaces which are up \n')
    print(json.dumps(interfaces,indent=2))
    toExcelFile(json.dumps(interfaces),"shIPintBR")
    connection.connect.close()
except Exception as e:
    print(e)
finally:
    print('connection closed')
    
