# qtileconfig
mi configuracion de qtile con archlinux(en proceso)


-----------------------------------                                                                                                                                                                                               
CONFIGURACION BASE ARCH                                                                                                                                                                                               
-----------------------------------                                                                                                                                                                                                
                                                                                                                                                                                               
Lo primero que hago es hacer una instalacion minima de archlinux con el comando archinstall sin ningun paquete que no sea estrictamente necesario o no sepa para que sirve                                             


luego de instalar y reniciar, compruebo que tarjeta grafica tengo con el comando                          
"lspci -v | grep -A1 -e VGA -e 3D"

posteriormente, busco los mejores controladores para mi tarjeta de video en la lista mostrada con el comando                      
"sudo pacman -Ss xf86-video"

idealmente ahora que tengo una tarjeta amd, instalo los drivers de amd                                                     
"sudo pacman -Ss xf86-video-amdgpu"

posterior a esto, instalo el servidor grafico ademas de xinit para iniciar el servidor grafico y las apps para distintas utilidades y la fuente necesaria para que funcione qtile                                                                         
"sudo pacman -S xorg-server xorg-xinit xorg-apps xorg-fonts-misc"

ahora, instalo qtile y la terminal alacritty                                                                            
"sudo pacman -S qtile alacritty"

ademas, instalo vim                                                                                            
"sudo pacman -S vim"

y configuro el archivo de xinit, el cual no existe y hay que crearlo                                                                    
"vim .xinitrc"                                                                                      
(adjunto una copia de este archivo)

en este punto ya se puede iniciar qtile con el comando                                                                                    
"startx"                                                                                                              

pero antes, combiene configurarlo un poco, asi que ejecutemos                                                                                                            
"sudo pacman -S unclutter"                                                                                                      



(en caso de no tener el archivo config.py que vendria por defecto, descargarlo desde mi repositorio)

ahora, instalo el servidor de audio pulse audio y rofi, ademas de configurarlo para la tecla m                                                                                                                            
"sudo pacman -S audiopulse rofi"

instalo yay con el comando                                                                                                                                                                      
"sudo pacman -S --needed git base-devel && git clone https://aur.archlinux.org/yay.git && cd yay && makepkg -si"                                                                                                                

(luego de instalar yay conviene actualizar con el comando 'yay')                                                                                                                            
e instalo brave con los comandos                                                                                                                                                                  
"yay -S brave-nightly-bin"                                                                                                                                                                                                

y añado su atajo a la 'b' con 'brave-browser-nightly' en este caso



