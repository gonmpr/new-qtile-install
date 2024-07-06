# QTILE-CONFIG-BORAN
mi configuracion de qtile boran(blue-orange) en Arch
>[!IMPORTANT]
> Para un paso a paso mas exacto, ver la guia berreta. Tener en cuenta donde debe ser copiado cada archivo para su correcta ejecución

                                                                                                                                                                                         
## INSTALANDO QTILE                                                                                                                                                                                            
                                                                                                                                                                                                
                                                                                                                                                                        


luego de instalar y reniciar, compruebo que tarjeta grafica tengo                        
```
lspci -v | grep -A1 -e VGA -e 3D
```


posteriormente, eligo los controladores para mi grafica                      
```
sudo pacman -Ss xf86-video
```
>[!NOTE]
> En mi caso serian los de AMD
```
sudo pacman -Ss xf86-video-amdgpu
```

posterior a esto, instalo el xorg con el xinit y las apps y la fuente necesaria para que funcione qtile
```
sudo pacman -S xorg-server xorg-xinit xorg-apps xorg-fonts-misc
```


ahora, instalo qtile y la terminal, en mi caso alacritty 
```
sudo pacman -S qtile alacritty
```

luego instalo vim y code
```
sudo pacman -S vim code
```

y configuro el archivo de xinit, el cual no existe y hay que crearlo                                                                    
>[!NOTE]
> Ver .xinitrc adjunto al repositorio.
```
vim .xinitrc                                                                                      
```

en este punto ya se puede iniciar qtile a traves de xorg                                                                                    
```
startx
```


## INSTALACIONES NECESARIAS

instalo yay con el comando    
```
sudo pacman -S --needed git base-devel && git clone https://aur.archlinux.org/yay.git && cd yay && makepkg -si                                                                                                              
```

instalo fuentes de ubuntu mono, firacode, simbolos(52 y 53) y roboto mono(58) ya que uso roboto mono nerd font bold                                                                                                                                                       
```
sudo pacman -S nerd-fonts 
```

### MENU DE BUSQUEDA Y ARRANQUE
Uso Rofi
```
sudo pacman -S  rofi
```

###AUDIO
en el caso del audio, uso pulseaudio y pavucontrol
```
sudo pacman -S pulseaudio pavucontrol
```

### NAVEGADOR

ya habiendo instalado yay, puedo instalar brave
```
yay -S brave-nightly-bin
```

### EXPLORADOR DE ARCHIVOS

Puedo usar tanto midnight commander como ranger
```
sudo pacman -S mc ranger
```

                                                                                                     
### RESOLUCION DE PANTALLA

instalo arandr para configurar la resolucion                                                                                                                                                                                                                 
```
sudo pacman -S arandr
```                                                                                                                                                                                                                                     
                                                                 

## INSTALACIONES ADICIONALES                                                                           

instalo cowfortune                                                                                                                                                                                      
```  
sudo pacman -S cowfortune
```

Instalo Unclutter para el mouse                                                                                                           
```  
sudo pacman -S unclutter
```  
