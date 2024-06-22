# qtileconfig
mi configuracion de qtile con archlinux(en proceso)

Lo primero que hago es hacer una instalacion minima de archlinux con el comando archinstall sin ningun paquete que no sea estrictamente necesario o no sepa para que sirve
luego de instalar y reniciar, compruebo que tarjeta grafica tengo con el comando                          
"lspci -v | grep -A1 -e VGA -e 3D"

posteriormente, busco los mejores controladores para mi tarjeta de video en la lista mostrada con el comando                      
"sudo pacman -Ss xf86-video"

idealmente ahora que tengo una tarjeta amd, instalo los drivers de amd                                                     
"sudo pacman -Ss xf86-video-amdgpu"

posterior a esto, instalo el servidor grafico ademas de xinit para iniciar el servidor grafico y las apps para distintas utilidades                                                                         
"sudo pacman -S xorg-server xorg-xinit xorg-apps"

ahora, instalo qtile y la terminal alacritty                                                                            
"sudo pacman -S qtile alacritty"

ademas, instalo vim                                                                                            
"sudo pacman -S vim"

y configuro el archivo de xinit, el cual no existe y hay que crearlo                                                                    
"vim .xinitrc"                                                                                      
(adjunto una copia de este archivo)
