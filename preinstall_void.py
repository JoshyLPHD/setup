from os import system

s= "sudo "
xi="xbps-install -S "
system(s+"xbps-install -Su -y")
system(s+xi+ "flatpak plasma-firewall ufw dolphin sl sddm gcc konsole timeshift partitionmanager filelight pulseaudio dbus xorg kde5 zsh wget curl nano htop -y")

system(s+"flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo")

system(s+" ln -s /etc/sv/dbus /var/service")
system(s+" ln -s /etc/sv/sddm /var/service ")
system(s+"chsh -s $(which zsh)")
system("sudo reboot")
