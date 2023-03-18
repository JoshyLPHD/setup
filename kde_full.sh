
#this script is for a minimal install of endeavour os (arch linux)


n=" --noconfirm "
p=" pacman "
s=" sudo "
nn=" --needed "
eval "$s $p -Syu $n"

eval '$s  $p -S $nn git clang wget curl make ttf-liberations cmake mesa neofetch  gcc plasma-wayland-session pipewire-alsa wireplumber pipwire-jack xorg   mkinitcpio nano dbus htop base-devel wget curl make gcc jdk8-openjdk zsh $n && cd /tmp/ && git clone https://aur.archlinux.org/yay.git && cd yay && makepkg -si  $n'
mkdir ~/.local/bin

mkdir ~/.dotfiles
eval "cd ~/ && git clone https://bitbucket.org/joshylphd/dotfiles ~/.dotfiles"

eval "yay -Syu   $n"
eval "yay -S $nn wayland 
 plasma  go  egl-wayland   sddm 
neofetch  plasma   egl-wayland podman gamemode vscodium-bin   mkinitcpio prismlauncher-bin plasma-wayland-session 
nano sl discord dbus sddm htop base-devel 
 jdk8-openjdk steam zsh wayland-protocols xorg-xwayland 
wayland-utils inetutils fusepak blueman bluez  jdk17-openjdk partitionmanager firewalld 
dolphin ark konsole jre17-openjdk kcalc plasma-systemmonitor timeshift-bin   $n"

eval "$s rm -fr ~/.oh-my-zsh"
eval 'sh -c "$(wget -O- https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended'
eval "$s git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions"
eval "rm ~/.zshrc && rm ~/.zshenv"
eval "ln -s ~/.dotfiles/.zshrc ~/.zshrc && ln -s ~/.dotfiles/zshenv ~/.zshenv"
eval "$s chsh -s $(which zsh)"
eval "echo 'exec zsh' >> ~/.bashrc "

eval "curl https://sh.rustup.rs -sSf | sh -s -- -y"
eval "rustup toolchain install nightly"
eval "rustup component add rust-src"
eval "rustup target install x86_64-pc-windows-gnu "

eval "sudo systemctl enable sddm.service && sudo systemctl enable NetworkManager.service"
echo "you should reboot"

#pluginsgit 
#         extract rust sudo python zsh-autosuggestions
#ZSH_THEME
#         gnzh
