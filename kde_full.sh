

plasma=" wayland-protocols mesa xorg xorg-xwayland dolphin kcalc plasma-systemmonitor ark konsole wayland-utils plasma-wayland-session wayland plasma sddm  egl-wayland  "
n=" --noconfirm "
p=" pacman "
s=" sudo "
nn=" --needed "
eval "$s $p -Syu $n"
test=0

if [ $1 == "" ]
then
exit 1 
fi

if [ $1 == "nvidia" ]
then 
eval "sudo pacman -S nvidia-utils lib32-nvidia-utils $n"
test=1
fi
if [ $1 == "amd" ]
then 
eval "sudo pacman -S amdvlk lib32-amdvlk $n"
test=1
fi

if [ $1 == "vm" ]
then
eval "sudo pacman -S vulkan-virtio xf86-video-qxl lib32-vulkan-virtio lib32-vulkan-mesa-layers $n"
test=1

fi

if [ test == 0 ]
then 
echo "please give amd,nvidia or vm as arguments"
exit 1
fi

#set keyboard to german
sudo localectl set-keymap de-latin1-nodeadkeys

#installs things to build yay 
eval "$s $p -S  fakeroot make go gcc cmake pkgconf $n"

#install yay (for aur)
eval "cd /tmp/ && git clone https://aur.archlinux.org/yay.git && cd yay && makepkg -si  $n"

#build tools
eval '  yay -S $nn git which clang wget curl make ttf-liberation cmake mkinitcpio nano dbus htop base-devel wget curl make gcc jdk8-openjdk zsh $n '

#install sound
eval "yay -S $nn  pipewire-alsa wireplumber pipewire-jack  $n "


echo "[KSplash]" > ~/.config/ksplashrc
echo "Theme=org.kde.breeze.desktop" >> ~/.config/ksplashrc

#install plasma
eval "yay -S $nn $plasma  $n"

#install random
eval "yay -S $nn neofetch gamemode inetutils sl htop fusepak $n"

#install some desktop programs
eval " yay -S $nn podman  vscodium-bin prismlauncher-bin  discord dbus sddm   jdk8-openjdk steam zsh blueman bluez  jdk17-openjdk partitionmanager firewalld jre17-openjdk timeshift-bin"


mkdir ~/.local
mkdir ~/.local/bin
mkdir ~/.dotfiles


#installs oh-my-zsh, config files for it
eval "cd ~/ && git clone https://bitbucket.org/joshylphd/dotfiles ~/.dotfiles"
eval "$s rm -fr ~/.oh-my-zsh"
eval 'sh -c "$(wget -O- https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended'
eval "$s git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions"
eval "rm ~/.zshrc && rm ~/.zshenv"
eval "ln -s ~/.dotfiles/.zshrc ~/.zshrc && ln -s ~/.dotfiles/zshenv ~/.zshenv"
#setting zsh to default
eval "$s chsh -s $(which zsh)"
eval "echo 'exec zsh' >> ~/.bashrc "


#install rust with extra
echo 'curl https://sh.rustup.rs -sSf | sh -s -- -y && rustup toolchain install nightly && rustup target install x86_64-unknown-linux-musl &&  rustup target install x86_64-unknown-none && rustup target install wasm32-unknown-unknown && rustup component add rust-src && rustup target install x86_64-pc-windows-gnu ' > kekw.tmp
zsh --exec  $(pwd)/kekw.tmp
rm kekw.tmp -f


eval "sudo systemctl enable sddm.service && sudo systemctl enable NetworkManager.service"
echo "you should reboot"

#pluginsgit 
#         extract rust sudo python zsh-autosuggestions
#ZSH_THEME
#         gnzh
