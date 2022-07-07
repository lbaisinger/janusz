#!/bin/sh
unclutter &
xset -dpms # disable DPMS (Energy Star) features.
xset s off # disable screen saver
xset s noblank # don’t blank the video device
matchbox-window-manager &
chromium-browser –-incognito –-kiosk http://192.168.2.105:5000/