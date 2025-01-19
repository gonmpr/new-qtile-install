#!/bin/sh

echo '-------------------------------------------------' &&
echo '----------------# INSTALACIONES #----------------' &&
echo '-------------------------------------------------' &&
sudo pacman -S xorg-server xorg-xinit xorg-apps xorg-fonts-misc &&
sudo pacman -S qtile alacritty vim &&
sudo pacman -S arandr dmenu j4-dmenu-desktop alsa-utils pipewire pipewire-pulse pipewire-alsa wireplumber picom firefox python-psutil &&
sudo pacman -S --needed git base-devel && git clone https://aur.archlinux.org/yay.git && cd /home/gonmpr/yay && makepkg -si && cd .. && rm -rf yay/ &&
sudo pacman -S ly &&

echo '----------------#FONTS => 28, 52, 53, 58, 64, 65#----------------' &&

sudo pacman -S nerd-fonts &&


echo '---------------------------------------------------' &&
echo '----------------# CONFIGURACIONES #----------------' &&
echo '---------------------------------------------------' &&

mkdir /home/gonmpr/.config/picom &&
mkdir /home/gonmpr/.config/alacritty &&
mkdir /home/gonmpr/.config/qtile &&
cd &&
chmod -R +x new-qtile-install/ &&

rm .xinitrc &&

rm .config/qtile/config.py &&
cp new-qtile-install/.xinitrc /home/gonmpr/.xinitrc &&
cp new-qtile-install/.vimrc /home/gonmpr/.vimrc &&

cp new-qtile-install/config/qtile/config.py /home/gonmpr/.config/qtile/config.py && cp new-qtile-install/config/qtile/autostart.sh /home/gonmpr/.config/qtile/autostart.sh && 
cp new-qtile-install/config/picom/picom.conf /home/gonmpr/.config/picom/picom.conf &&
cp new-qtile-install/config/alacritty/alacritty.toml /home/gonmpr/alacritty/alacritty.toml &&
cp new-qtile-install/wallpapers/01wallpaper.png /home/gonmpr/qtile/01wallpaper.png  &&
systemctl enable ly.service &&
echo '-------------------------------------FINALIZADO-------------------------------------'
