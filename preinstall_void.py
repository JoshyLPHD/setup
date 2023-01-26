from os import system
from time import sleep
s= "sudo "
xi="xbps-install -S "
system("cd ~/ && mkdir Download && mkdir Dokumente")
system(s+"xbps-install -Su -y")
##alacritty
system(s+xi+ "flatpak helix sweeper mesa bluez plasma-firewall ufw dolphin sl  sddm gcc konsole timeshift partitionmanager filelight pulseaudio dbus xorg kde5 zsh wget curl nano htop -y")
system("cd ~/ && git clone https://bitbucket.org/joshylphd/dotfiles ~/.dotfiles")
system("rm ~/.zshrc && rm ~/.zshenv")
system("ln -s ~/.dotfiles/.zshrc ~/.zshrc && ln -s ~/.dotfiles/zshenv ~/.zshenv")

system(s+"flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo")

system(s+" ln -s /etc/sv/dbus /var/service")
system(s+" ln -s /etc/sv/sddm /var/service ")
system(s+"chsh -s $(which zsh)")
system(s+" Xorg -configure")
system("curl https://sh.rustup.rs -sSf | sh -s -- -y")
system("rustup update")
system("rustup toolchain install nightly")
system("rustup component add rust-src")
system("rustup target install x86_64-pc-windows-gnu ")

sleep(3)
system("sudo reboot")
