# NEW QTILE INSTALL
Como personalizar una nueva instalacion de Qtile, usando Archlinux

                                                                                                                                                                                         
## INSTALANDO QTILE                                                                                                                                                                                            
                                                                                                                                                                                                
                                                                                                                                                                      
>[!NOTE]
> Realizo una instalacion limpia y y de entorno minima con ```archinstall``` solo instalando lo necesario

Compruebo que tarjeta grafica tengo.                     
```
lspci -v | grep -A1 -e VGA -e 3D
```
                                                                                                                                                                                                                                        
Posteriormente, eligo los controladores para mi grafica                      
```
sudo pacman -Ss xf86-video
```
                                                                                                                                                                                    
```
sudo pacman -Ss xf86-video-amdgpu
```
                                                                                                                                                                                                                                        
Ahora, instalo el xorg con el xinit y las apps y la fuente necesaria para que funcione Qtile
```
sudo pacman -S xorg-server xorg-xinit xorg-apps xorg-fonts-misc
```
                                                                                                                                                                                                                                        
Instalo Qtile y la terminal, en mi caso Alacritty, ademas de Vim y Git
```
sudo pacman -S qtile alacritty vim git
```

Copio mis archivos de configuracion de qtile, ssh_login, .xinitrc y autostart.sh, ademas de la configuracion de picom
```
git clone https://github.com/gonmpr/new-qtile-install
```                                                                                                                                                                                                                                      
                                                                                                                                                                                                                                        
Y configuro el archivo de xinit, el cual no existe y hay que crearlo, luego de creado, puedo copiar mi archivo descargado en el paso anterior                                                                    

```
vim .xinitrc                                                                                      
```
                                                                                                                                                                                                                                        
En este punto ya se puede iniciar Qtile a traves de xorg                                                                                    
```
startx
```

Una vez ingresamos a Qtile, lo cerramos y copiamos todos los archivos de configuracion que descargamos a sus respectivos lugares, y seguimos con la descarga de paquetes.                                                                                 
>[!NOTE]
> La configuracion de resolucion que se encuentra en el archivo .xinitrc es segun nuestro monitor, generar y usar  la que generemos con arandr seria lo ideal                                                                                                                                                                                                                                     
                                                                                                                                                                                                                                        
                                                                                                                                                                                                                                        
## INSTALACIONES NECESARIAS
fonts: simbols(52,53), ubuntu mono,firacode,roboto mono(58)
```
sudo pacman -S nerd-fonts 
```                                                                                                                                                                                                                                        

                                                                                                                                                                                                                                        
```
sudo pacman -S rofi ranger arandr dmenu j4-dmenu-desktop alsa-utils pipewire pipewire-pulse pipewire-alsa wireplumber picom-git code firefox

sudo pacman -S --needed git base-devel && git clone https://aur.archlinux.org/yay.git && cd yay && makepkg -si
```

                                                                                                                                                                                                                                        

                                                                                                                                                                                                                                        
                                                                                                                                                                        
                                                                                                                                                                                                                               

                                                                                                                                                                                                                                        
                                                                                                                                                                                                                                        

                                                                                                                                                                                                                                        
                                                                                                     
                                                                                                                                                                                                                  
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
