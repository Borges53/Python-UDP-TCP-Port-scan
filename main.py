
import argparse
import nmap
import socket
import sys

parser = argparse.ArgumentParser(description="Process some integers.")
parser.add_argument("-i", "--ip", required=True, help="ip for scan")

args = parser.parse_args()

print("SEARCHING FOR MACHINES ON THE NET " + args.ip)
nm = nmap.PortScanner()
nm.scan(args.ip,'1-65535','-O','-v') 
for host in nm.all_hosts():
    print("IP " + host)
    print("===========================")
    print('\t'+ 'TPC:' + '\n')
    for proto in nm[host].all_protocols():
        lport = nm[host][proto].keys()
        for port in lport:
            print("\t \t %s: %s " % (port,nm[host][proto][port]['product']))
    try:
      print('\tUDP:')
      for port in range(1, 65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((host, port))
        if result == 0:
          print("\t \t{}:".format(port))
          s.close()
    except KeyboardInterrupt:
      print("\n Closing the Program !!!")
      sys.exit()
    except socket.error:
      print('\n Host Does Not Respond!!!')
      sys.exit()
    print('- - - - - - - - - - - - - - - \n')
