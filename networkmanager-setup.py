from os import system
from time import sleep
s= "sudo "
xi="xbps-install -S "
system(s+"ln -s /etc/sv/NetworkManager /var/service/")
system()
sleep(3)
system("reboot")
