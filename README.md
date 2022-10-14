# Centrum dowodzenia
![](img/dashboard.png)
## TO-DO:
- dokladniejszy weather module/po lokalizacji wifi/osobny czujnik: geolokacja mozliwa
- automatyczne odswieżanie
- zmiana tapety, dodawanie nowych obrazków, zmiana koloru czcionki/eventow
- host na zdalnym serwerze
- automatyczne odswiezanie strony (kalendarz/temperatura)
### Settings:
- to turn display on/off:
  - vcgencmd display_power 0
  - vcgencmd display_power 1
- For RPI0W install req:
  - xinit
  - xorg
  - matchbox
  - unclutter
  - python3 & pip
  - chromium-browser
  - Flask
  - Git
  - start.sh (+ make executable by sudo chmod x+a)
  - allow anybody via ssh X11
### Startup
1. cd ./janusz --> export FLASK_APP = app.py --> flask run --hostk=0.0.0.0
2. xinit ./janusz/start.sh
