import json
from pprint import pprint
json_file='hosts.json'
hosts_file = open('hosts', 'w')
hosts_meta_file = open('hosts_meta', 'w')
json_data=open(json_file)
data = json.load(json_data)
hosts_file.write("127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4\n")
hosts_file.write("::1         localhost localhost.localdomain localhost6 localhost6.localdomain6\n")
for x in data['items']:
    hostname = x['hostname'].split(".")[0]
    hosts_meta_file.write(x['ipAddress'] + "\n")
    if hostname.startswith('master'):
       print(x['ipAddress'] + "  " + x['hostname'].split(".")[0] +".cdh-master.internal " + x['hostname'].split(".")[0])
       hosts_file.write(x['ipAddress'] + "  " + x['hostname'].split(".")[0] +".cdh-master.internal " + x['hostname'].split(".")[0] +"\n")
    else:
       print(x['ipAddress'] + "  " + x['hostname'].split(".")[0] +".cdh-worker.internal " + x['hostname'].split(".")[0])
       hosts_file.write(x['ipAddress'] + "  " + x['hostname'].split(".")[0] +".cdh-worker.internal " + x['hostname'].split(".")[0] +"\n")
json_data.close()
hosts_file.close()
hosts_meta_file.close()
