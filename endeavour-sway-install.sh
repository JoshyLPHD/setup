n=" --noconfirm "
p=" pacman "
s=" sudo "
c="$s $p -Syu $n"
exec $c
c='$s + $p + " -S  --needed git clang sway neofetch xorg egl-wayland mesa go mkinitcpio nano sl discord dbus htop base-devel  wget curl make gcc jdk8-openjdk steam zsh "  + n +" && cd /tmp/ && git clone https://aur.archlinux.org/yay.git && cd yay && makepkg -si --needed "+$n'
exec   $c

cd ~/ && git clone https://bitbucket.org/joshylphd/dotfiles ~/.dotfiles
yay -Syyu " + n
yay -S --needed wayland wayland-protocols wayland-utils inetutils fusepak blueman bluez virt-manager qemu-tools qemu-system-x86 qemu-img jdk17-openjdk partitionmanager firewalld podman brave-bin dolphin ark konsole jre17-openjdk brave-bin kcalc  filelight plasma-systemmonitor prismlauncher-bin  timeshift-bin visual-studio-code-bin " + n

curl https://sh.rustup.rs -sSf | sh -s -- -y
rustup update
rustup toolchain install nightly
rustup component add rust-src
rustup target install x86_64-pc-windows-gnu

s+"rm -fr ~/.oh-my-zsh"
sh -c "$(wget -O- https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended
s+" git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
rm ~/.zshrc && rm ~/.zshenv
ln -s ~/.dotfiles/.zshrc ~/.zshrc && ln -s ~/.dotfiles/zshenv ~/.zshenv
s+"chsh -s $(which zsh)
s+"modprobe nbd max_part=8"
echo you should reboot
#pluginsgit 
#         extract rust sudo python zsh-autosuggestions
#ZSH_THEME
#         gnzh
