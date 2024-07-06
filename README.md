# qtileconfig
mi configuracion de qtile con archlinux


-----------------------------------                                                                                                                                                                                               
Instalando Qtile                                                                                                                                                                                               
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

ahora, instalo qtile y la terminal alacritty con vim y visual studio code                                                                         
"sudo pacman -S qtile alacritty vim code"

y configuro el archivo de xinit, el cual no existe y hay que crearlo                                                                    
"vim .xinitrc"                                                                                      
(adjunto una copia de este archivo)

en este punto ya se puede iniciar qtile con el comando                                                                                    
"startx"                                                                                                              

pero antes, combiene configurarlo un poco, asi que ejecutemos                                                                                                            
"sudo pacman -S unclutter"                                                                                                      



(en caso de no tener el archivo config.py que vendria por defecto, descargarlo desde mi repositorio)

ahora, instalo el servidor de audio pulse audio y rofi, ademas de configurarlo para la tecla m                                                                                                                            
"sudo pacman -S pulseaudio rofi"

instalo yay con el comando                                                                                                                                                                      
"sudo pacman -S --needed git base-devel && git clone https://aur.archlinux.org/yay.git && cd yay && makepkg -si"                                                                                                                

(luego de instalar yay conviene actualizar con el comando 'yay')                                                                                                                            
e instalo brave con los comandos                                                                                                                                                                  
"yay -S brave-nightly-bin"                                                                                                                                                                                                

y añado su atajo a la 'b' con 'brave-browser-nightly' en este caso

instalo midnight commander(archivos) con 
"sudo pacman -S mc"                                                                                                                                                                                                                      
y añado su atajo a la 'a' con 'alacritty -e mc' ya que si agrego 'mc' sólo, no se ejecutaria.                                                                                                                                                                          

creo y edito el autostart.sh, ademas de agregar su llamada en la configuracion de qtile,                                                                                                                                                    
de momento, queda vacia, pero debo agregarle permisos de ejecucion con el comando 'chmod +x .config/qtile/autostart.sh'                                                                                                                                                                                              
instalo arandr paar configurar la resolucion de la pantalla                                                                                                                                                                                                                    
"sudo pacman -S arandr"                                                                                                                                                                                                                                        

instalo psutil para el widget de net(red) con 
"sudo pacman -S python-psutil"

                                                                                                                                                                                                          
como cliente de audio uso pavucontrol                                                                                                                                                                                                         
'sudo pacman -S pavucontrol'                                                                                                                                                                                                           
y copia al archivo .xinitrc:                                                                                                                                                                                                           
                                                                                                                                                                                                                                                                                                                                                              
instalo fuentes de ubuntu mono, firacode, simbolos(52 y 53) y roboto mono(58) ya que uso roboto mono nerd font bold                                                                                                                                                       
'sudo pacman -S nerd-fonts'                                                                                                                                                                              


cree  configure un tema de rofi(estilo1.rasi), el cual debe ser puesto en el directorio                                                                                                                                                      
~/.local/share/rofi/themes/estilo1.rasi                                                                                                                                                                                                              

y en caso de no encontrarse en la lista de temas, ejecutar:                                                                                                                                                      
'rofi -show run -theme ~/.local/share/rofi/themes/blue.rasi'                                                                                                                                                      


Añado el fondo de pantalla 01wallpaper el cual guardo en '/home/gonmpr/.config/qtile/.wallpaper/01wallpaper.png'                                                                                                                                                            
agrego un menu de reinicio y apago con rofi con un script que guardo en /home/gonmpr/.config/rofi/                                                                        


y con el comando siguiente asociado a la q                                                                                                                                                  
' rofi -show power-menu -modi "power-menu:/home/gonmpr/.config/rofi/rofi-power-menu --choices=shutdown/reboot" '                                                                              

instalo cowfortune  y agrego su ejecucion al .bashrc                                                                                                                                                                                      
'sudo pacman -S cowfortune'                                                                                                                                                                                                                              
