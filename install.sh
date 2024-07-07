#!/bin/bash
#mi qtile config en archlinux minimal install

#instala todo lo necesario
cd &&
sudo pacman -S xorg-server xorg-xinit xorg-apps xorg-fonts-misc &&
sudo pacman -S qtile alacritty vim code &&
sudo pacman -S --needed git base-devel && git clone https://aur.archlinux.org/yay.git && cd yay && makepkg -si && cd && rm -rf yay &&
sudo pacman -S rofi pulseaudio pavucontrol ranger arandr cowfortune unclutter &&

#descargo de mi github las configuraciones
sudo git clone 'https://github.com/gonmpr/qtile-config/' &&
cd &&
sudo chmod -R +x qtile-config &&


#creo las carpetas que no existen
mkdir -p ~/.config/qtile/.wallpaper/ &&
mkdir -p /home/gonmpr/.local/share/rofi/themes/ &&

#copio cada archivo de configuracion a su lugar
#&&
#&&