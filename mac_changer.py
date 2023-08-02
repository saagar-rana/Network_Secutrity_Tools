
import subprocess as sp
from optparse import OptionParser


def get_args():
    parser = OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="write report to FILE")
    parser.add_option("-m", "--mac", dest="macnew", help="New mac")
    (options,arguments)=parser.parse_args()
    if not options.interface:
        parser.error("Incorrect mf, use --help")
    elif not options.macnew:
        parser.error("Incorrect mf, use --help")
    return options


def change_mac (interface,macnew):
    sp.call(["ifconfig", interface, "down"])
    sp.call(["ifconfig", interface, "hw" , "ether" , macnew])
    sp.call(["ifconfig", interface, "up"])


options = get_args()
print(options)
change_mac(options.interface,options.macnew)

print("Mac is changed to "+options.macnew)



