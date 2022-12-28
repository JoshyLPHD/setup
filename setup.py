from os import system
import time

n = "--noconfirm "
p = "pacman "
s = "sudo "
system(s + p + "-Syyu " + n)
system(
    s
    + p
    + "-S  --needed git neofetch sl xorg discord dbus libxtst sddm htop base-devel go wget glibc llvm cmake neovim curl make gcc jdk8-openjdk steam zsh "
    + n
)

system(
    "cd /tmp/ && git clone https://aur.archlinux.org/yay.git && cd yay && makepkg -si --needed "
    + n
)

system("yay -Syyu " + n)

system("yay -S prismlauncher-bin timeshift " + n)

system(
    "cd /tmp && wget https://mega.nz/linux/repo/Arch_Extra/x86_64/megasync-x86_64.pkg.tar.zst && sudo pacman -U megasync-x86_64.pkg.tar.zst --needed "
    + n
)
system("curl https://sh.rustup.rs -sSf | sh -s -- -y")
system("rustup update")
system("rustup toolchain install nightly")
system(
    'sh -c "$(wget https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"'
)
system(
    "cd /tmp && git clone https://AUR.archlinux.org/visual-studio-code-bin.git && cd visual-studio-code-bin/ && makepkg -si --needed "
    + n
)
system(
    "cd /tmp && git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions"
)
# copy this two lines to .bashrc
#
#export PATH="/usr/local/go/bin:$PATH"
#export PATH="~/.cargo/bin:$PATH"
#
#
#
#
#zsh /oh_my_zsh setup
#
#pluginsgit 
#         extract rust sudo python zsh-autosuggestions
#ZSH_THEME
#         gnzh

time.sleep(4)
system("reboot")
