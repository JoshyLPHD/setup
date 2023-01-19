from os import system

s= "sudo "
xi="xbps-install -S "

system(s+xi+ "flatpak sl dbus xorg kde5 nano htop -y")
system(s+"flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo")
system("flatpak install flathub com.discordapp.Discord -y")
system("flatpak install flathub com.valvesoftware.Steam -y ")
system("flatpak install flathub com.brave.Browser -y ")
system("flatpak install flathub org.prismlauncher.PrismLauncher -y ")
system("flatpak install flathub com.visualstudio.code -y ")
system("flatpak install flathub nz.mega.MEGAsync -y")
system("")
system("")


