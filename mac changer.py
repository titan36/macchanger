#!/usr/bin/python2

# please don't use python 2, it is deprecated!
# use python 3 instead
import subprocess
import optparse

def arg():
    par = optparse.OptionParser()
    par.add_option("-i","--interface",dest="interface",help="This is interface to change") #this is on argment
    par.add_option("-m","--macaddress",dest="mac",help="This is interface to change") #this is on argment
    (option,arguments) = par.parse_args()
    if not option.interface:  #if the interface is not enterd properly
        par.error("[-] please specify the interface  use --help for more info")
    elif not option.mac:   #if the interface is not enterd properly
        par.error("[-] please specify the mac address use --help for more info")    
    return option;
def maccha(inter,mac):
    subprocess.call("ifconfig " + inter + " down",shell=True)
    subprocess.call("ifconfig " + inter + " hw ether " + mac,shell=True)
    subprocess.call("ifconfig " + inter + " up",shell=True)

option = arg()
maccha(option.interface,option.mac)
