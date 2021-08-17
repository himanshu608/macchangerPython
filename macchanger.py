import subprocess
import optparse
import re
opt = optparse.OptionParser()

opt.add_option("-i","--interface", dest="interface",help="input your interface name of which you want to change mac address.")
opt.add_option("-m","--mac", dest="mac_addr",help="Enter new mac address .")

(user_input,arguments) = opt.parse_args()
user_mac = user_input.mac_addr
user_interface = user_input.interface

ifconfig = subprocess.check_output(["ifconfig",user_interface])

subprocess.call(["ifconfig",user_interface,"down"])
subprocess.call(["ifconfig",user_interface,"hw","ether",user_mac])
subprocess.call(["ifconfig",user_interface,"up"])
outmac = re.search(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w',str(ifconfig));

if outmac.group(0)==user_mac:
    print('macchanger changed your mac address to {}'.format(user_mac))
else:
    print("Error! please check your inputs.")

