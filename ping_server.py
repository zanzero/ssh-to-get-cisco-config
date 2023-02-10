import pythonping
import json

ip_list = []
with open('host.txt', 'r') as host:
    line = host.readline()
    while line:
        ip_list.append(line.strip())
        line = host.readline()

response = {}
for ip in ip_list:
    try:
        res = pythonping.ping(ip, timeout=2)
        if res.success():
            response[ip] = 'reachable'
        else:
            response[ip] = 'XXXXXXXXXXX'
    except Exception as e:
        response[ip] = 'error'

print(json.dumps(response, indent=4))
