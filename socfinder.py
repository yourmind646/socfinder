#!/usr/bin/env python3
try:
	import requests, json, colorama
	from colorama import Fore, Back, Style

	colorama.init()

	mgnt = Fore.MAGENTA
	grn = Fore.GREEN
	rd = Fore.RED
	ylw = Fore.YELLOW
	wht = Fore.WHITE

	class nicknameIsEmpty(Exception):
		pass

	class nicknameContainsSpace(Exception):
		pass

	def search(nick):
		print('{}\n[*] Выполняется поиск профилей...{}'.format(Fore.YELLOW, Fore.WHITE))
		for site in data:
			r = requests.get(site + nick)
			if r.ok:
				print('{}[+] {}{}'.format(Fore.GREEN, (site + nick), Fore.WHITE))
			else:
				print('{}[-] {}{}'.format(Fore.RED, (site + nick), Fore.WHITE))

	print(grn + '''
   _____                  ______   _               _               
  / ____|                |  ____| (_)             | |              
 | (___     ___     ___  | |__     _   _ __     __| |   ___   _ __ 
  \___ \   / _ \   / __| |  __|   | | | '_ \   / _` |  / _ \ | '__|
  ____) | | (_) | | (__  | |      | | | | | | | (_| | |  __/ | |   
 |_____/   \___/   \___| |_|      |_| |_| |_|  \__,_|  \___| |_|   

''' + ylw + '\n[*] Версия - 1.0.2.1\n[*] Предназначено для систем Linux/Termux\n[*] Автор скрипта TG @RubySide\n' + Fore.WHITE)

	nickname = input('Введите никнейм, по которому нужно найти профиль (пример: rubyside)\n>>> ')

	if nickname == "":
		raise nicknameIsEmpty()
	elif nickname.find(' ') != -1:
		raise nicknameContainsSpace()

	print('{}\n[*] Загрузка списка с сайтами...{}'.format(Fore.YELLOW, Fore.WHITE))
	with open("data_file.json", "r") as read_file:
		data = json.load(read_file)
	print('{}[+] Список загружен! Сайтов для поиска - {}{}'.format(Fore.GREEN, len(data), Fore.WHITE))

	search(nickname)

except EOFError:
	print('\n{}[*] Выход из программы...{}'.format(Fore.YELLOW, Fore.WHITE))
except KeyboardInterrupt:
	print('\n\n{}[*] Выход из программы...{}'.format(Fore.YELLOW, Fore.WHITE))
except nicknameIsEmpty:
	print('\n{}[-] Никнейм не введен.{}'.format(Fore.RED, Fore.WHITE))
except nicknameContainsSpace:
	print('\n{}[-] Никнейм не должен содержать пробелы.{}'.format(Fore.RED, Fore.WHITE))