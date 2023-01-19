from os import system

s= "sudo "
xi="xbps-install -S "

system(s+xi+ "flatpak sl dbus xorg kde5 nano htop -y")
system("flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo")
system("flatpak install flathub com.discordapp.Discord")
system("flatpak install flathub com.valvesoftware.Steam")
system("flatpak install flathub com.brave.Browser")
system("flatpak install flathub org.prismlauncher.PrismLauncher")
system("flatpak install flathub com.visualstudio.code")
system("flatpak install flathub nz.mega.MEGAsync")
system("")
system("")


