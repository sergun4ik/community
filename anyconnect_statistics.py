from netmiko import ConnectHandler as ch
from re import search
from datetime import datetime


password = 'PASSWORD_GOES_HERE'             #Credentials 
user = 'USER_NAME_GOES_HERE'                #Credentials
report_file = 'REPORT_FILE_NAME'            #Report file name

device = {'ip': 'x.x.x.x', \                #IP address of the ASA
         'device_type': 'cisco_asa',\
         'username': user, \
         'password': password, \
         'secret': password}

with ch(**device) as ssh:
  ssh.enable()
  line = ssh.send_command('show vpn-sessiondb summary')

val = search('\d+',line.split('\n')[5]).group()

timestamp = datetime.now()
stamp = str(timestamp).split('.')[0]

with open(report_file,'a') as file:
  line = str(stamp) + ',' + str(val) + '\n'
  file.write(line)
