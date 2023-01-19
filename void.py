from os import system

s= "sudo "
xi="xbps-install -S "

system(s+xi+ "flatpak sl dbus xorg kde5 nano htop -y")
system(s+"flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo")
system(s+"flatpak install flathub com.discordapp.Discord -y")
system(s+"flatpak install flathub com.valvesoftware.Steam -y ")
system(s+"flatpak install flathub com.brave.Browser -y ")
system(s+"flatpak install flathub org.prismlauncher.PrismLauncher -y ")
system(s+"flatpak install flathub com.visualstudio.code -y ")
system(s+"flatpak install flathub nz.mega.MEGAsync -y")
system("")
system("")


