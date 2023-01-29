from os import system
from time import sleep



s= "sudo "
xi="xbps-install -S "


system(s+"flatpak install flathub com.discordapp.Discord -y")
system(s+"flatpak install flathub com.valvesoftware.Steam -y ")
system(s+"flatpak install flathub com.brave.Browser -y ")
system(s+"flatpak install flathub org.prismlauncher.PrismLauncher -y ")
system(s+"flatpak install flathub com.visualstudio.code -y ")
system(s+"flatpak install flathub nz.mega.MEGAsync -y")
system(s+"flatpak install flathub com.github.tchx84.Flatseal -y")
system(s+"flatpak install flathub net.davidotek.pupgui2 -y")
system(s+"flatpak install flathub com.obsproject.Studio -y")
system(s+"flatpak install flathub org.yuzu_emu.yuzu -y ")
#system(s+"flatpak install flathub com.usebottles.bottles -y")
#system(s+"flatpak install flathub dev.lapce.lapce -y")
sleep(3)
system("reboot")
