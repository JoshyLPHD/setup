
#this script is for a minimal install of endeavour os (arch linux)


n=" --noconfirm "
p=" pacman "
s=" sudo "
nn=" --needed "
eval "$s $p -Syu $n"
test=0

if [ $1=="" ]
then
  exit 1 
fi

if [ $1=="nvidia" ]
then 
 eval "sudo pacman -S nvidia-utils lib32-nvidia-utils $n"
  test=1
fi
if [ $1=="amd" ]
then 
 eval "sudo pacman -S amdvlk lib32-amdvlk $n"
  test=1
fi

if [ $1=="vm"]
then
eval "sudo pacman -S vulkan-virtio lib32-vulkan-virtio $n"
test=1

fi

if [ test==1 ]then 


echo "please give amd,nvidia or vm as arguments"
exit 1
fi

localectl set-keymap de-latin1-nodeadkeys

eval "cd /tmp/ && git clone https://aur.archlinux.org/yay.git && cd yay && makepkg -si  $n"
eval "yay -S sddm-git $n --useask"
eval '  yay -S $nn git clang wget curl make ttf-liberation cmake mesa neofetch  gcc plasma-wayland-session pipewire-alsa wireplumber pipwire-jack xorg   mkinitcpio nano dbus htop base-devel wget curl make gcc jdk8-openjdk zsh $n '
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

echo '#/bin/sh

eval "curl https://sh.rustup.rs -sSf | sh -s -- -y"
eval "rustup toolchain install nightly"
eval "rustup target install x86_64-unknown-linux-musl
eval "rustup target install x86_64-unknown-none
eval "rustup target install wasm32-unknown-unknown
eval "rustup component add rust-src"
eval "rustup target install x86_64-pc-windows-gnu "' > kekw.tmp
zsh --exec  $(pwd)/kekw.tmp
rm kekw.tmp -f

eval "sudo systemctl enable sddm.service && sudo systemctl enable NetworkManager.service"
echo "you should reboot"

#pluginsgit 
#         extract rust sudo python zsh-autosuggestions
#ZSH_THEME
#         gnzh
