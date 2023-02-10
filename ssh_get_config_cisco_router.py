import paramiko
import io
import os
from cred import username, password


def get_config(host, command):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=username, password=password)

    stdin, stdout, stderr = ssh.exec_command(command)
    output = io.StringIO(stdout.read().decode('utf-8')).getvalue()
    ssh.close()
    return output

aa = 'ttt'
commands_list = list()
with open('commands.txt', 'r') as commands:
    line = commands.readline()
    while line:
        commands_list.append(line.strip())
        line = commands.readline()

print(commands_list)

hosts_list = list()
with open('host.txt', 'r') as hosts:
    line = hosts.readline()
    while line:
        hosts_list.append(line.strip())
        line = hosts.readline()

print(hosts_list)

hosts_name = list()
with open('hostname.txt', 'r') as hostnames:
    line = hostnames.readline()
    while line:
        hosts_name.append(line.strip())
        line = hostnames.readline()

print(hosts_name)

final = str()
i = 0
for host in hosts_list:
    name = hosts_name[i]
    print(f"===> {name}_{host}")

    for command in commands_list:
        print(command)
        final += get_config(host, command)

    with open(f"{os.getcwd()}/config/{name}_{host}.txt", "w") as file:
        file.write(final)
        i += 1
