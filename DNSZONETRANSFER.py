#python DNS zone transfer
import os
 
domain = input('Enter Domain: ')
comm = 'host -t ns {dmn} | cut -d " " -f 4'
command = comm.format(dmn = domain)
 
nameserverprocess = os.popen(command)
nameservers = nameserverprocess.readlines()
nameserverprocess.close()
for server in nameservers:
    zonetransfer_command = "host -l {dmn} {srvr}"
    zonetransfer_commandready = zonetransfer_command.format(dmn = domain, srvr = server)
    process =  os.popen(zonetransfer_commandready)
    output = process.readlines()
    process.close()
    print(*output, sep = "\n") 