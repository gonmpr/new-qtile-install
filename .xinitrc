#desabilita el beep
xset -b

inicia picom para las visuales lindas :D
picom &

#unclutter - oculta el mouse cuando no esta en uso
unclutter --jitter 10 --ignore-scrolling --start-hiden --fork

#inicia qtile
qtile start
