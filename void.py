from os import system
from time import sleep
s= "sudo "
xi="xbps-install -S "
#system(s+"xbps-install -Su -y")
#system(s+xi+ "flatpak plasma-firewall ufw dolphin sl sddm gcc konsole timeshift partitionmanager filelight pulseaudio dbus xorg kde5 zsh wget curl nano htop -y")

#system(s+"flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo")
system(s+"flatpak install flathub com.discordapp.Discord -y")
system(s+"flatpak install flathub com.valvesoftware.Steam -y ")
system(s+"flatpak install flathub com.brave.Browser -y ")
system(s+"flatpak install flathub org.prismlauncher.PrismLauncher -y ")
system(s+"flatpak install flathub com.visualstudio.code -y ")
system(s+"flatpak install flathub nz.mega.MEGAsync -y")
system(s+"flatpak install flathub com.github.tchx84.Flatseal -y")
system(s+"flatpak install flathub net.davidotek.pupgui2 -y")
system(s+"flatpak install flathub com.obsproject.Studio -y")
system(s+"flatpak install flathub com.usebottles.bottles -y")
system(s+"flatpak install flathub dev.lapce.lapce -y")
#system(s+"")

#system(s+"chsh -s $(which zsh)")
system('sh -c "$(wget -O- https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended')
system(s+"git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions")
#system(s+" ln -s /etc/sv/dbus /var/service")
#system(s+" ln -s /etc/sv/sddm /var/service ")
sleep(3)
system("sudo reboot")

#
#pluginsgit 
#         zsh-autosuggestions extract rust sudo python
#ZSH_THEME
#         gnzh
