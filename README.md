# QTILE-CONFIG
mi configuracion de qtile en Arch
>[!IMPORTANT]
> Para un paso a paso mas exacto, ver la guia berreta. Tener en cuenta donde debe ser copiado cada archivo para su correcta ejecución,
>el nombre del usuario ```gonmpr``` es importante para varios archivos, pero puede ser cambiado en cada archivo 

                                                                                                                                                                                         
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
                                                                                                                                                                                                                                        
>[!NOTE]
> En mi caso serian los de AMD
```
sudo pacman -Ss xf86-video-amdgpu
```
                                                                                                                                                                                                                                        
Ahora, instalo el xorg con el xinit y las apps y la fuente necesaria para que funcione Qtile
```
sudo pacman -S xorg-server xorg-xinit xorg-apps xorg-fonts-misc
```
                                                                                                                                                                                                                                        

Instalo Qtile y la terminal, en mi caso Alacritty 
```
sudo pacman -S qtile alacritty
```
                                                                                                                                                                                                                                        
Luego instalo vim y Visual Studio Code
```
sudo pacman -S vim code
```
                                                                                                                                                                                                                                        
Y configuro el archivo de xinit, el cual no existe y hay que crearlo                                                                    

```
vim .xinitrc                                                                                      
```
                                                                                                                                                                                                                                        
En este punto ya se puede iniciar Qtile a traves de xorg                                                                                    
```
startx
```
                                                                                                                                                                                                                                        
                                                                                                                                                                                                                                        
## INSTALACIONES NECESARIAS
                                                                                                                                                                                                                                        
                                                                                                                                                                                                                                        
Instalo Yay con el comando    
```
sudo pacman -S --needed git base-devel && git clone https://aur.archlinux.org/yay.git && cd yay && makepkg -si
```
                                                                                                                                                                                                                                        
Instalo las fuentes de ubuntu mono, firacode, simbolos(52 y 53) y roboto mono(58) ya que uso roboto mono nerd font bold                                                                                                                                                       
```
sudo pacman -S nerd-fonts 
```
                                                                                                                                                                                                                                        
### MENU DE BUSQUEDA Y ARRANQUE
Uso Rofi
```
sudo pacman -S  rofi
```
                                                                                                                                                                                
                                                                                                                                                                                                                                        
### AUDIO
                                                                                                                                                                                                                          


En el caso del audio, uso Pulseaudio y Pavucontrol
```
sudo pacman -S pulseaudio pavucontrol
```
                                                                                                                                                                                                                                        
                                                                                                                                                                                                                                        
### NAVEGADOR
                                                                                                                                                                                                                                        
Ya habiendo instalado Yay, puedo instalar Brave
```
yay -S brave-nightly-bin
```
                                                                                                                                                                                                                                        
                                                                                                                                                                                                                                        
### EXPLORADOR DE ARCHIVOS
                                                                                                                                                                                                                                        
Puedo usar tanto Midnight Commander como Ranger
```
sudo pacman -S mc ranger
```
                                                                                                                                                                                                                                        
                                                                                                     
### RESOLUCION DE PANTALLA
                                                                                                                                                                                                                                        
Instalo Arandr para configurar la resolucion                                                                                                                                                                                                                 
```
sudo pacman -S arandr
```                                                                                                                                                                                                                                     
                                                                                                                                                                                                                                                                                                         

## INSTALACIONES ADICIONALES                                                                           
                                                                                                                                                                                                                                        
Instalo CowFortune                                                                                                                                                                                      
```  
sudo pacman -S cowfortune
```
                                                                                                                                                                                                                                        
Instalo Unclutter para el mouse                                                                                                           
```  
sudo pacman -S unclutter
```  
