#!/usr/bin/python3
import socket
import argparse
import validators

parser=argparse.ArgumentParser(description="Slappy's Port Scaning tool!")
parser.add_argument('-v','--version',action="version",version='%(prog)s 1.0')
parser.add_argument('url',type=str,help="The url to the Port Scanner")
parser.add_argument('-o','--output',help='To save result in text file')
args=parser.parse_args()
url=args.url
j=0
port_names=["ftp","ssh","telnet","smtp","domain name system","http","pop3","rp-cbind","msrpc","netbios-ssn","imap","https","microsoft-ds","imaps","pop35","pptp","mysql","ms-wbt-server","vnc","http-proxy"]
ports=[21,22,23,25,53,80,110,111,135,139,143,443,445,993,995,1723,3306,3389,5900,8080]
head="Welcome to Slappy's Port Scanner tool!\n"
head+="=====================================\n\n"
head+="Scanning Start...\n"
print(head)
report=''

for i in ports:
	result=-1
	s=socket.socket()
	result=s.connect_ex((url,i))
	if result==0:
		report+=port_names[j]+"port open at:"+str(i)+"\n"
		print(port_names[j]+" port open at: "+str(i))
	else:
		report+=port_names[j]+"port closed at: "+str(i)+"\n"
		print(port_names[j]+" port closed at: "+str(i))
	j+=1
	s.close()

if args.output:
    f=open(args.output,'w')
    f.write(head+report)
    print("Report of result saved successfully as "+args.output)

print("\nThank you for using port Scanner :)")

