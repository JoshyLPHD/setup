from os import system
from time import sleep
s= "sudo "
xi="xbps-install -S "

services=[ "virtqemud" ,"virtlogd" ,"virtstoraged", "virtnetworkd" ,"dnsmasq" ,"iptables", "dbus", "sddm", "ufw" ,"pulseaudio"]
system("cd ~/ && mkdir Downloads && mkdir Dokumente")
system(s+"xbps-install -Su -y")
##alacritty
system(s+xi+ "flatpak helix qbittorrent mesa bluez qemu gimp virt-manager-tools virt-manager plasma-firewall ufw dolphin sl make sddm gcc konsole timeshift partitionmanager filelight pulseaudio dbus xorg kde5 zsh wget curl nano htop -y")
system("cd ~/ && git clone https://bitbucket.org/joshylphd/dotfiles ~/.dotfiles")

system(s+"flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo")

#system(s+" ln -s /etc/sv/dbus /var/service")
#system(s+" ln -s /etc/sv/sddm /var/service ")
system(s+"chsh -s $(which zsh)")
system("curl https://sh.rustup.rs -sSf | sh -s -- -y")
system("rustup update")
system("rustup toolchain install nightly")
system("rustup component add rust-src")
system("rustup target install x86_64-pc-windows-gnu ")

system('sh -c "$(wget -O- https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended')
system(s+"git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions")

system("rm ~/.zshrc && rm ~/.zshenv")
system("ln -s ~/.dotfiles/.zshrc ~/.zshrc && ln -s ~/.dotfiles/zshenv ~/.zshenv")

system(s+"modprobe nbd max_part=8")
system(s+"rm /var/service/wpa_supplicant")
system(s+"rm /var/service/dhcpcd")
#system(s+"ln -s /etc/sv/NetworkManager /var/service/")
for service in services:
  system(s+f"ln -s /etc/sv/{service}   /var/service/")
sleep(3)
system("sudo reboot")
