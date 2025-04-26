VLAN Creator for Cisco Switch
Overview
This script (vlan_creator.py) connects to a Cisco switch via SSH and automatically creates VLANs from 1 to 100.

Each VLAN is named VLAN_<number> (e.g., VLAN_1, VLAN_2, etc.)

Requirements
Python 3.x

paramiko library

Install paramiko if you don't have it:

bash
Copy
Edit
pip install paramiko
How to Run
Clone or download this script.

Open a terminal.

Run:

bash
Copy
Edit
python vlan_creator.py
Enter:

Switch IP address

SSH username

SSH password

The script will:

Connect to the switch

Enter configuration mode

Create VLANs 1–100

Save the configuration
