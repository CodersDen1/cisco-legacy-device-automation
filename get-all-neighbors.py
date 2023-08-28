from connection import connection_to_device;
import connection
import constants
from getUserDetails import getUserDetail
import getUserDetails
import json

getUserDetail()

constants.connection_profiles['username']=getUserDetails.user
constants.connection_profiles['password']=getUserDetails.password
constants.connection_profiles['secret']=getUserDetails.sec
constants.connection_profiles['ipadd']=getUserDetails.ip
constants.connection_profiles['port']=getUserDetails.port

try:
    connection_to_device(**constants.connection_profiles)
    
    
    print('***********************\n \t \t CDP Neighbors \n ***********************')
    cdp_neighbors=connection.connect.send_command('show cdp neighbors' ,use_textfsm=True)
    print(json.dumps(cdp_neighbors , indent=2))


    print('***********************\n \t \t  IP Routes \n ***********************')
    ip_route=connection.connect.send_command('show ip route' ,use_textfsm=True)
    print(json.dumps(ip_route , indent=2))
except Exception as e:
    print(e)
finally:
    print('Connection is closed')





