import os
from download_wallpaper import download_apod

def main():
    os.system("gsettings set org.gnome.settings-daemon.plugins.background active true")
    os.system("gsettings set org.gnome.desktop.background picture-uri " + download_apod())
    os.system("gsettings set org.gnome.desktop.background picture-options 'scaled'")

main()
