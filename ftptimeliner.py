from ftplib import FTP
from dateutil import parser
import argparse
import sys


aparser = argparse.ArgumentParser()
aparser.add_argument("-s", help="FTP host",required=True, dest="ftphost")
aparser.add_argument("-u", help="FTP usernmame",required=True,dest="username")
aparser.add_argument("-p", help="FTP password",required=True,dest="password")
aparser.add_argument("-d", help="Start directory, defaults to /", default="/",dest="directory")
args = aparser.parse_args()

ftp = FTP(args.ftphost)
ftp.login(user=args.username, passwd = args.password)

entries = []

def list_dir_rec(dir):
    try:
        files = ftp.mlsd(dir)
        for file in files:
            name = dir+"/"+file[0]
            if file[1]['type']== "dir": list_dir_rec(name)
            if file[1]['type']== "file":
                timestamp = file[1]['modify']
                time = parser.parse(timestamp)
                entry = {"name":name,"mtime":time}
                entries.append(entry)
    except:
        sys.stderr.write("Can't access {}. Leaving out that directory".format(dir))
        return

def list_dir(dir):
    list_dir_rec(dir)
            


list_dir(args.directory)

#simple csv output. might add bodyfile support later
print("Time,File")
for entry in entries:
    print("{},{}".format(entry['mtime'],entry['name']))
