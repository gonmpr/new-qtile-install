# ubicado en /home/gonmpr

#deshabilita el beep
xset -b

#unclutter - oculta el mouse cuando no esta en uso
unclutter --jitter 10 --ignore-scrolling --start-hiden --fork

#inicia qtile
qtile start

#resolucion generada por arandr
xrandr --output DisplayPort-0 --off --output DisplayPort-1 --off --output DisplayPort-2 --off --output HDMI-A-0 --primary --mode 1920x1080 --rate 75 --pos 0x0 --rotate normal

