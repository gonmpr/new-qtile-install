
import os, subprocess
from libqtile import bar, layout, qtile, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal





#---VARIABLES---#
mod = "mod4"
yellow_heart = '#C69749' #usado en el focus y como active color
barSize = 24
barColor = '#1E222A'
barFont = "RobotoMono Nerd Font Bold"
barFontSize = 12
group_label = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
terminal = 'alacritty'

#81C189 =green
##a681c1 =violet






#---FUNCIONES---#

# PARA RECORTAR NOMBRES EN EL WIDGET WINDOW NAME
def parseLargeNames(text): 
    if '- Brave' in text: return 'Brave'
    else: 
        for string in [" - Code - OSS"]:
            text = text.replace(string, "")
            return text

# WIDGET SEPARADOR
def separator(visible = True, separacion = 5):
    if(visible):
        return widget.Sep(linewidth = 1, padding = separacion, foreground = "#4c566a", background = barColor)
    else:
        return widget.Sep(linewidth = 1, padding = separacion, foreground = barColor, background = barColor)
    
# PARA EL BORDE DE LAS VENTANAS

def layout_theme():
    return {
        "margin": 0,
        "border_width": 1,
        "border_focus": yellow_heart,
        "border_normal": "#20242C",
    }














keys = [
    
    #---ESENCIALES---#
    Key([mod], "Return", lazy.spawn(terminal), desc="abre Alacritty"),
    Key([mod], "m", lazy.spawn('rofi -show drun'), desc="Abre Rofi(menu)"),
    #la direccion seguida de 'power-menu' es el path donde esta el script, y la condicion choices al final se puede quitar para ver todas las opciones
    Key([mod], "q", lazy.spawn('rofi -show power-menu -modi "power-menu:/home/gonmpr/.config/rofi/rofi-power-menu --choices=shutdown/reboot" -theme estilo1-powermenu-only'), desc="Abre Rofi(apagado/reincio)"),
    Key([mod], "b", lazy.spawn('brave-browser-nightly'), desc="Abre Brave"),
    Key([mod], "a", lazy.spawn('alacritty -e ranger'), desc="Abre Ranger (Explorador de archivos)"),






    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),

    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),







    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),

    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
]










for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )


groups = [Group(i) for i in group_label
]

for i,group in enumerate(groups):
    desktopNum = str(i+1)
    keys.extend(
        [
           
            Key(
                [mod],
                desktopNum,
                lazy.group[group.name].toscreen(),
                desc="Switch to group {}".format(group.name),
            ),
           
            Key(
                [mod, "shift"],
                desktopNum,
                lazy.window.togroup(group.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(group.name),
            ),
        ]
    )



layouts = [
    layout.Columns(**layout_theme()),
    layout.Max(),
]








widget_defaults = dict(
    font=barFont,
    fontsize=barFontSize,
    padding=3,
)
extension_defaults = widget_defaults.copy()


screens = [
    Screen(
        top=bar.Bar(
            [
                separator(False, 2),   #separador invisble con 2 de separacion            

                separator(True, 5),     # separador visible con 5 de separacion

                widget.GroupBox(
                    margin_y = 2,
                    margin_x = 3,
                    padding_y = 2,
                    padding_x = 3,
                    borderwidth = 0,
                    disable_drag = True,
                    active = '#767780',
                    inactive = "#2e3440",
                    rounded = False,
                    highlight_method = "text",
                    this_current_screen_border = yellow_heart,
                    background=barColor,
                    foreground = "#4c566a",
                ),

                separator(True, 5),
                
                widget.Prompt(),

                separator(False, 10),

                widget.TextBox('>>', foreground=yellow_heart),

                widget.WindowName(parse_text=parseLargeNames, max_chars = 32), 

                widget.Systray(),
               
                separator(True, 5),
                
                widget.Pomodoro(
                    background='#C15F5F',
                    color_inactive=barColor
                ),

                separator(False, 10),

                widget.Volume(
                    step=1,
                    foreground = barColor,
                    background= '#a681c1'
                ),

                separator(False, 10),

                widget.Clock(
                    background="#81a1c1",
                    foreground = barColor,  
                    fontsize = 12, 
                    format = "%H:%M %p",
                ),

                
                separator(False, 7),

            ],
            barSize,
            background=barColor

        ),
        wallpaper='/home/gonmpr/.config/qtile/.wallpaper/01wallpaper.png',
        wallpaper_mode='fill'
        
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,
    ),
]


mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# xcursor theme (string or None) and size (integer) for Wayland backend
wl_xcursor_theme = None
wl_xcursor_size = 24


wmname = "LG3D"


#Ejecuta autostart.sh
@hook.subscribe.startup_once
def autostart():

        script = os.path.expanduser("~/.config/qtile/autostart.sh")
        subprocess.run([script])
