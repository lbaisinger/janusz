#!/bin/sh
export DISPLAY=:0
xset -dpms # disable DPMS (Energy Star) features.
xset s off # disable screen saver
xset s noblank # don’t blank the video device
chromium-browser --incognito --start-fullscreen https://bajsi.pythonanywhere.com/
