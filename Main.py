# vlan_creator.py
#Zaid Laffta
#11/11/2024

import paramiko
import time

def create_vlans(ip, username, password):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(ip, username=username, password=password, look_for_keys=False, allow_agent=False)

        shell = client.invoke_shell()
        time.sleep(1)

        shell.send('enable\n')
        time.sleep(1)
        shell.send('configure terminal\n')
        time.sleep(1)

        for vlan_id in range(1, 101):
            shell.send(f'vlan {vlan_id}\n')
            shell.send(f'name VLAN_{vlan_id}\n')
            time.sleep(0.2)

        shell.send('end\n')
        shell.send('write memory\n')
        time.sleep(2)

        output = shell.recv(5000).decode('utf-8')
        print(output)

        client.close()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    ip = input("Enter the switch IP address: ")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    create_vlans(ip, username, password)
