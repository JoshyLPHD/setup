from os import system
import time

n = " --noconfirm "
p = "pacman "
s = "sudo "
system(s + p + "-Syyu " + n)
system(
    s
    + p
    + "-S  --needed git neofetch xorg plasma egl-wayland mesa go mkinitcpio plasma-wayland-session nano sl discord dbus sddm htop base-devel  wget curl make gcc jdk8-openjdk steam zsh "
    + n +" && cd /tmp/ && git clone https://aur.archlinux.org/yay.git && cd yay && makepkg -si --needed "+n
)
system("cd ~/ && git clone https://bitbucket.org/joshylphd/dotfiles ~/.dotfiles")
system("yay -Syyu " + n)

system("yay -S --needed fusepak blueman bluez filelight virt-manager qemu-tools qemu-system-x86 qemu-img jdk17-openjdk partitionmanager firewalld podman brave-bin dolphin ark konsole jre17-openjdk brave-bin kcalc  filelight plasma-systemmonitor prismlauncher-bin  megasync-bin timeshift-bin visual-studio-code-bin " + n)

#system(
#    "cd /tmp && wget https://mega.nz/linux/repo/Arch_Extra/x86_64/megasync-x86_64.pkg.tar.zst && sudo pacman -U megasync-x86_64.pkg.tar.zst --needed "
#    + n
#)
system("curl https://sh.rustup.rs -sSf | sh -s -- -y")
system("rustup update")
system("rustup toolchain install nightly")
system("rustup component add rust-src")
system("rustup target install x86_64-pc-windows-gnu ")
system(s+"rm -fr ~/.oh-my-zsh")
system('sh -c "$(wget -O- https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended')
system(s+" git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions")
system("rm ~/.zshrc && rm ~/.zshenv")
system("ln -s ~/.dotfiles/.zshrc ~/.zshrc && ln -s ~/.dotfiles/zshenv ~/.zshenv")
system(s+"chsh -s $(which zsh)")
system(s+"modprobe nbd max_part=8")
system("sudo systemctl enable sddm.service && sudo systemctl enable NetworkManager.service")
system(s+p+ "--remove amdvlk "+n)
print("you should reboot")
#pluginsgit 
#         extract rust sudo python zsh-autosuggestions
#ZSH_THEME
#         gnzh
