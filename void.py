from os import system

s= "sudo "
xi="xbps-install -S "

system(s+xi+ "flatpak sl sddm dbus xorg kde5 zsh wget curl nano zsh-autosuggestions htop -y")

system(s+"flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo")
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
system(s+"flatpak install flathub org.gnome.World.PikaBackup -y")
system(s+"flatpak install flathub org.kde.filelight -y")
#system(s+"")
#system(s+"")
#system(s+"")
system(s+"chsh -s $(which zsh)")
system('sh -c "$(wget -O- https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended')


#
#pluginsgit 
#         extract rust sudo python
#ZSH_THEME
#         gnzh
