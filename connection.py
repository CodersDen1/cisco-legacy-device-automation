from netmiko import ConnectHandler
connect=''

def connection_to_device(username,password, secret, ipadd,port):
    device_cred={}
   
    device_cred={
            'device_type':'cisco_ios_telnet',
            'ip':ipadd,
            'username':username,
            'password':password,
            'secret':secret,
            'port': port
        }
    global connect    
    connect=ConnectHandler(**device_cred)
    connect.enable()
    

