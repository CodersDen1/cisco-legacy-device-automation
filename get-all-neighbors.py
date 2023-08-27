from connection import connection_to_device;
import connection
import constants
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
    
except Exception as e:
    print(e)
finally:
    print('Connection is closed')




