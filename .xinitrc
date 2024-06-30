#habilita el beep

xset -b


#audio

/usr/bin/pipewire &
/usr/bin/pipewire-pulse &
/usr/bin/pipewire-media-session &


#icono de audio

volumeicon &



#unclutter - oculta el mouse cuando no esta en uso

unclutter --jitter 10 --ignore-scrolling --start-hiden --fork



#inicia qtile

qtile start
