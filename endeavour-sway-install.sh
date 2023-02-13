#this script is for a minimal install of endeavour os (arch linux)


n=" --noconfirm "
p=" pacman "
s=" sudo "
nn=" --needed "
eval "$s $p -Syu $n"

eval '$s  $p -S --needed git clang sway neofetch xorg egl-wayland mesa go mkinitcpio nano sl discord dbus htop base-devel  wget curl make gcc jdk8-openjdk steam zsh "  + n +" && cd /tmp/ && git clone https://aur.archlinux.org/yay.git && cd yay && makepkg -si $nn $n'

mkdir ~/.dotfiles
eval "cd ~/ && git clone https://bitbucket.org/joshylphd/dotfiles ~/.dotfiles"
eval "yay -Syu   $n"
eval "yay -S $nn wayland xwayland wayland-protocols xorg-xwayland  wayland-utils inetutils fusepak blueman bluez virt-manager qemu-tools qemu-system-x86 vscodium-bin qemu-img jdk17-openjdk partitionmanager firewalld podman brave-bin dolphin ark konsole jre17-openjdk brave-bin kcalc  filelight plasma-systemmonitor prismlauncher-bin  timeshift-bin   $n"

eval "curl https://sh.rustup.rs -sSf | sh -s -- -y"
eval "rustup update"
eval "rustup toolchain install nightly"
eval "rustup component add rust-src"
eval "rustup target install x86_64-pc-windows-gnu"

eval "$s rm -fr ~/.oh-my-zsh"
eval 'sh -c "$(wget -O- https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended'
eval "$s git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions"
eval "rm ~/.zshrc && rm ~/.zshenv"
eval "ln -s ~/.dotfiles/.zshrc ~/.zshrc && ln -s ~/.dotfiles/zshenv ~/.zshenv"
eval "$s chsh -s $(which zsh)"
eval "$s modprobe nbd max_part=8 "
echo "you should reboot"

#pluginsgit 
#         extract rust sudo python zsh-autosuggestions
#ZSH_THEME
#         gnzh
